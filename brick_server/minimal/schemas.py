from copy import deepcopy
from enum import Enum
from typing import Any, Dict, List

from pydantic import BaseModel, Field, conlist

from brick_server.minimal.descriptions import Descriptions


class ValueType(str, Enum):
    number = "number"
    text = "text"
    loc = "loc"


class ColumnType(str, Enum):
    number = "number"
    text = "text"
    loc = "loc"
    uuid = "uuid"
    timestamp = "timestamp"


value_types = [val.value for val in ValueType]

# Relationship = List[str] ## [Predicate, Object] for the Subject
TripleModel = conlist(str, min_items=3, max_items=3)
TupleModel = conlist(str, min_items=2, max_items=2)
Relationship = deepcopy(TupleModel)


class Relationships(BaseModel):
    relationships: List[Relationship]


class Entity(BaseModel):
    relationships: List[Relationship] = Field(
        [], description=Descriptions.relationships
    )
    type: str = Field(..., description=Descriptions.type)
    entity_id: str = Field(..., description=Descriptions.entity_id)
    name: str = Field(None, description=Descriptions.name)


class EntityIds(BaseModel):
    entity_ids: List[str] = Field(..., description="The list of `entity_id`s")


class Entities(BaseModel):
    entities: List[Entity] = Field(..., description="The list ot entities")


class TimeseriesData(BaseModel):
    data: List[List[Any]] = Field(..., description=Descriptions.data)
    columns: List[ColumnType] = Field(
        ["uuid", "timestamp", "number"], description=Descriptions.columns
    )


ValueTypes = List[ValueType]

SparqlResult = Dict


class IsSuccess(BaseModel):
    is_success: bool = True
    reason: str = ""


# class ActuationRequest(BaseModel):
#     entity_id: str = Field(..., description=Descriptions.entity_id)
#     value: str = Field(..., description=Descriptions.actuation_value)
#     # scheduled_time: float = Field(None)


class CreateEntityRequest(BaseModel):
    number: int = Field(
        ..., description="The number of instances to create for the Brick Class"
    )
    # ignore_brick_type: bool = Bool(False, description='If true, does not check whether the given type is defined in Brick or not') #TODO: Implement this


BrickClass = str

CreateEntitiesRequest = Dict[
    BrickClass,  # = Field(..., description='A Class name, often defined in Brick'),
    int,  # = Field(...,description='The number of instances to create for the Brick Class')
]

EntitiesCreateResponse = Dict[BrickClass, List[str]]


class GrafanaDashboardResponse(BaseModel):
    url: str = Field(..., description="Grafana dashboard url for the user")
    uid: str = Field(..., description="Grafana dashboard uid for the user")
    grafana_id: str = Field(..., description="Grafana dashboard id for the user")


class GrafanaUpdateRequest(BaseModel):
    grafana: Dict = Field(
        ...,
        description="The complete Grafana Dashboard model as defined in `https://grafana.com/docs/grafana/latest/http_api/dashboard/`",
    )


class TokenResponse(BaseModel):
    token: str = Field(..., description="JWT token")
    name: str = Field(..., description="Associated name with the token")
    exp: int = Field(..., description="The token's expiration time in unix timestamp")


TokensResponse = List[TokenResponse]
