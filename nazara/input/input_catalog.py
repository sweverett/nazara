from typing import Type
from abc import ABC, abstractmethod

import pudb

class InputCatalog(ABC):
    '''
    This is an abstract class for any catalog you wish to inject into. It holds any methods that are common or need to be defined for any catalog
    '''

    name = 'input_catalog'

    # this keeps track of any registered input catalog types
    _registry = {}

    def __init__(self) -> None:
        '''
        name: str
            Name of the input catalog type
        '''
        return

    # @classmethod
    # def register(cls: ]) -> None:
    #     '''
    #     Register the input catalog as a valid type for the factory method
    #     '''

    #     InputCatalog._registry[cls.name.lower()] = cls

    #     return

def register_input_catalog(cls: Type[InputCatalog]) -> Type[InputCatalog]:
    '''
    This is a decorator to register a class as a valid input catalog type
    '''

    InputCatalog._registry[cls.name.lower()] = cls

    return cls

# TODO: It would be nice to have an independent registration system, so that other users could add input classes without having to modify this file
# NOTE: This is where you must register a new model
INPUT_CAT_TYPES = {
    # 'default': ('spherex_simulated', 'SPHERExSimulated'),
    # 'spherex_simulated': ('spherex_simulated', 'SPHERExSimulated'),
    # 'spherex_reference': ('spherex_reference', 'SPHERExReference'),
    }

def build_input_catalog(name, kwargs):
    '''
    name: str
        Name of input catalog type
    kwargs: dict
        Keyword args to pass to input catalog constructor
    '''

    name = name.lower()

    if name in InputCatalog._registry.keys():
        # Registered input catalog construction
        input_cat = InputCatalog._registry[name](**kwargs)

    # if name in INPUT_CAT_TYPES.keys():
        # User-defined input catalog construction
        # NOTE: we do the following to avoid circular imports        
        # module_name, class_name = INPUT_CAT_TYPES[name]
        # module = __import__(module_name, fromlist=[class_name])
        # input_cat_class = getattr(module, class_name)
        # input_cat = INPUT_CAT_TYPES[name](**kwargs)
    else:
        raise ValueError(f'{name} is not a registered input!')

    return input_cat