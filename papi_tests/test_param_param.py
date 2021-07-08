from papi import Papi
from papi_examples.utils import read_config


def test_param_param_edge():
    papi = Papi(name="mypipeline", config=read_config("example1.yaml"))
    t1 = papi.task("Train model")
    t2 = papi.task("Train model")
    t1.parameter_edge("learning_rate").to(t2.parameter_edge("learning_rate"))
    assert len(papi.edges) == 1
