import os

import asyncpg
from fastapi import FastAPI
from fastapi_rest_framework import config, logging
from loguru import logger
from starlette.middleware.sessions import SessionMiddleware
from fastapi.middleware.cors import CORSMiddleware


from brick_server.minimal.config import FastAPIConfig

settings = config.init_settings(FastAPIConfig)

API_V1_PREFIX = "/brickapi/v1"

logging.init_logging()
logging.intercept_all_loggers()
app = FastAPI(title="Brick Server", openapi_url="/docs/openapi.json")

origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.logger = logger


async def initialization() -> None:
    from brick_server.minimal.dbs import graphdb, ts_db

    await graphdb.init_repository()
    await graphdb.import_schema_from_url("https://brickschema.org/schema/Brick")

    # logger.info("Brick SPARQL load schema")
    # await brick_sparql.load_schema()

    try:
        logger.info("Init timescale tables")
        await ts_db.init()
    except asyncpg.exceptions.DuplicateTableError:
        logger.info("Timescale tables have been already created.")


@app.on_event("startup")
async def startup_event() -> None:
    await initialization()


from .auth.auth_server import auth_router
from .services.actuation import actuation_router
from .services.data import data_router
from .services.entities import entity_router
from .services.grafana import grafana_router
from .services.queries import query_router

app.include_router(data_router, prefix="/brickapi/v1/data")
app.include_router(entity_router, prefix="/brickapi/v1/entities")
app.include_router(query_router, prefix="/brickapi/v1/rawqueries")
app.include_router(actuation_router, prefix="/brickapi/v1/actuation")
app.include_router(grafana_router, prefix="/brickapi/v1/grafana")
app.include_router(auth_router, prefix="/brickapi/v1/auth")
# app.include_router(dummy_frontend_router, prefix='/dummy-frontend')

app.secret_key = os.urandom(24)
app.add_middleware(SessionMiddleware, secret_key=os.urandom(24))
