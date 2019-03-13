import os

import yaml


def test_readdata():
    file=os.getcwd()+os.sep+"user.yml"
    with open(file, "r") as f:
       return yaml.load(f)