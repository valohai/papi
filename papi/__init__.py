from collections import Counter
from typing import Dict, List, Optional, TypeVar

from valohai_yaml.objs import Config, Step

from papi.base import PapiObject
from papi.contexts import APIContext, YAMLContext
from papi.edges import Edge, EdgeDescriptor
from papi.nodes import ExecutionNode, Node, TaskNode

__all__ = ["Papi"]

SomeNode = TypeVar("SomeNode", bound=Node)


class Papi:
    nodes: Dict[str, Node]
    edges: List[Edge]
    counters: Counter

    def __init__(self, config: Config):
        self.config = config
        self.nodes = {}
        self.edges = []
        self.counters = Counter()

    def _count(self, key: str) -> str:
        self.counters[key] += 1
        key_l = key.lower().replace(" ", "_")
        return f"{key_l}_{self.counters[key]}"

    def _register_node(self, node: SomeNode) -> SomeNode:
        if node.name in self.nodes:
            raise ValueError(f"Duplicate node {node}")
        self.nodes[node.name] = node
        node.papi = self
        return node

    def execution(self, step: str, name: str = None):
        step_object = self._get_step(step)
        return self._register_node(
            ExecutionNode(
                step=step_object, name=(name or self._count(step_object.name))
            )
        )

    def _get_step(self, name) -> Step:
        step_object: Step = self.config.get_step_by(name=name)
        if not step_object:
            raise ValueError(f"no such step {name} in config")
        return step_object

    def task(self, step: str, name: str = None) -> TaskNode:
        step_object = self._get_step(step)
        return self._register_node(
            TaskNode(step=step_object, name=(name or self._count(step_object.name)))
        )

    def to_api(self, api_context: Optional[APIContext] = None):
        if not api_context:
            api_context = APIContext()
        return {
            "nodes": [n.to_api(api_context=api_context) for n in self.nodes.values()],
            "edges": [e.to_api(api_context=api_context) for e in self.edges],
        }
