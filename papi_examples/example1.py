from pprint import pprint

from papi import Papi
from papi_examples.utils import read_config


def main():
    papi = Papi(name="mypipeline", config=read_config("example1.yaml"))

    # Define nodes
    extract = papi.execution("Batch feature extraction")
    train = papi.task("Train model")
    evaluate = papi.execution("Evaluate")

    # Configure training task node
    train.linear_parameter("learning_rate", min=0, max=1, step=0.1)

    # Configure pipeline
    extract.output("a*").to(train.input("aaa"))
    extract.output("a*").to(train.input("bbb"))
    train.output("*").to(evaluate.input("models"))

    # Get dict suitable for passing to Create Pipeline API
    pprint(papi.to_api())

    # Get Pipeline object for YAML
    papi.to_yaml()


if __name__ == "__main__":
    main()
