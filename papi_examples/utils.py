import os

import yaml
from valohai_yaml.objs import Config


def read_config(filename):
    if not os.path.isabs(filename):
        filename = os.path.join(os.path.dirname(__file__), filename)
    with open(filename) as f:
        data = yaml.safe_load(f)
    return Config.parse(data)
