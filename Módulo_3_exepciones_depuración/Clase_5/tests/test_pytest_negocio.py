import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from negocio import VendedorBase, VendedorPremium

import pytest

def test_calcular_comision_base():
    vendedor_base = VendedorBase('Juan', 1000)
    assert vendedor_base.calcular_comision() == 100

def test_calcular_comision_premium():
    vendedor_premium = VendedorPremium('Pedro', 2000)
    assert vendedor_premium.calcular_comision() == 300