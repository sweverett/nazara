from nazara.input.input_catalog import InputCatalog, register_input_catalog

@register_input_catalog
class SPHERExSimulatedCatalog(InputCatalog):
    # config registry name
    name = 'spherex_simulated'

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        return