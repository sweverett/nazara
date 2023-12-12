'''
This file will contain classes that encapsulate the fiducial SPHEREx reference catalog and how it interacts with the injector
'''

from nazara.input.input_catalog import InputCatalog, register_input_catalog

@register_input_catalog
class SPHERExReferenceCatalog(InputCatalog):

    # config registry name
    name = 'spherex_reference'

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)