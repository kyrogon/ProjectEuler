import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
RESOURCE_DIR = ROOT_DIR + '/resources'


def list2int(array):
    return int(''.join(map(str, array)))