import json

from papi import Papi
from papi_examples.utils import read_config


def test_task_parameter_options():
    papi = Papi(read_config("example1.yaml"))
    t1 = papi.task("Train model")
    t1.linear_parameter("learning_rate", min=0, max=1, step=0.1)
    t1.random_parameter("temperature", min=0, max=1, count=10)
    json.dumps(papi.to_api())
