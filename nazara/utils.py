import os

def get_base_dir():
    '''
    base dir is parent repo dir
    '''
    module_dir = get_module_dir()
    return os.path.dirname(module_dir)

def get_module_dir():
    return os.path.dirname(__file__)

def get_test_dir():
    base_dir = get_base_dir()
    return os.path.join(base_dir, 'tests')

BASE_DIR = get_base_dir()
MODULE_DIR = get_module_dir()
TEST_DIR = get_test_dir()