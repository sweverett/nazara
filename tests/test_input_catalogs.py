import unittest
from nazara.input.input_catalog import InputCatalog, build_input_catalog
from nazara.input.spherex_simulated import SPHERExSimulatedCatalog
from nazara.input.spherex_reference import SPHERExReferenceCatalog

class TestInputCatalog(unittest.TestCase):

    def setUp(self) -> None:
        self.input_cat = InputCatalog()
        self.spherex_simulated = SPHERExSimulatedCatalog()
        self.spherex_reference = SPHERExReferenceCatalog()
        return

    def test_input_registration(self):
        '''
        If the various input catalog subclasses are correctly registered, then they should be in the InputCatalog registry
        '''

        print('Starting test_input_registration')

        self.assertIn('spherex_simulated', InputCatalog._registry.keys())
        self.assertIn('spherex_reference', InputCatalog._registry.keys())

        self.assertEqual(
            InputCatalog._registry['spherex_simulated'], SPHERExSimulatedCatalog
            )
        self.assertEqual(
            InputCatalog._registry['spherex_reference'], SPHERExReferenceCatalog
            )

        return

if __name__ == '__main__':
    unittest.main()
