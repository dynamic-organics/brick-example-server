from typing import Any, Callable, Dict, Set

from fastapi.security import HTTPAuthorizationCredentials

from brick_server.minimal.auth.authorization import (
    PermissionType,
    default_auth_logic,
    jwt_security_scheme,
    parse_jwt_token,
)
from brick_server.minimal.interfaces import AsyncpgTimeseries, GraphDB

auth_logic_func_type = Callable[[Set[str], PermissionType], bool]


class DependencySupplier(object):
    auth_logic: Callable[[], auth_logic_func_type]

    # def get_auth_logic(self) -> Callable[[Set[str], PermissionType], bool]:
    #     return self.auth_logic


dependency_supplier = DependencySupplier()
dependency_supplier.auth_logic = default_auth_logic


def update_dependency_supplier(func: Callable[[], auth_logic_func_type]):
    dependency_supplier.auth_logic = func


def get_ts_db() -> AsyncpgTimeseries:
    from brick_server.minimal.dbs import ts_db

    return ts_db


def get_graphdb() -> GraphDB:
    from brick_server.minimal.dbs import graphdb

    return graphdb


def get_actuation_iface():
    from brick_server.minimal.dbs import actuation_iface

    return actuation_iface


def get_grafana():
    from brick_server.minimal.dbs import grafana_endpoint

    return grafana_endpoint


def get_jwt_payload(
    token: HTTPAuthorizationCredentials = jwt_security_scheme,
) -> Dict[str, Any]:
    return parse_jwt_token(token.credentials)
