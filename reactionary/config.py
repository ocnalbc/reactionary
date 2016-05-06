
"""
reactionary.config
~~~~~~~~~~~~~~~~~~

config methods/functions
"""

import yaml
import os
import sys


CONFIG_DEFAULT=os.path.join(os.environ['HOME'], '.reactionary.yaml')

def get_config(config=CONFIG_DEFAULT):
    return yaml.load(open(config, 'r').read())
