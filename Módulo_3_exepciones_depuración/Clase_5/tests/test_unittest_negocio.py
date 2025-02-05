import sys
import os

# Agregar la ruta del directorio src donde está negocio.py y __init__.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from negocio import VendedorBase, VendedorPremium
import unittest

class TestVendedorBase(unittest.TestCase):
    def setUp(self):
        self.vendedorBase = VendedorBase('Juan', 1000)
        self.vendedor_premium = VendedorPremium('Pedro', 2000)
    
    def test_calculo_comision_vendedor_base(self):
        self.assertEqual(self.vendedorBase.calcular_comision(), 100)
    
    def test_calculo_comision_vendedor_premium(self):
        self.assertEqual(self.vendedor_premium.calcular_comision(), 300)

if __name__ == '__main__':
    unittest.main()