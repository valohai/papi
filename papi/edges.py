import dataclasses
from typing import TYPE_CHECKING

from papi import YAMLContext
from papi.base import PapiObject
from papi.contexts import APIContext

if TYPE_CHECKING:
    from papi.nodes import Node


@dataclasses.dataclass(frozen=True)
class Edge(PapiObject):
    source_node: str
    source_type: str
    source_key: str
    target_node: str
    target_type: str
    target_key: str
    configuration: dict = dataclasses.field(default_factory=dict)

    def to_api(self, api_context: APIContext):
        payload = dataclasses.asdict(self)
        if not payload.get("configuration"):
            del payload["configuration"]
        return payload

    def to_yaml(self, yaml_context: YAMLContext):
        raise NotImplementedError(f"{self}.to_yaml() has not been implemented")


@dataclasses.dataclass(frozen=True)
class EdgeDescriptor:
    node: "Node"
    type: str
    key: str

    def to(self, dest: "EdgeDescriptor"):
        # TODO: add validation
        assert self.node.papi is dest.node.papi
        self.node.papi.edges.append(
            Edge(
                source_node=self.node.name,
                source_type=self.type,
                source_key=self.key,
                target_node=dest.node.name,
                target_type=dest.type,
                target_key=dest.key,
            )
        )
