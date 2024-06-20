import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.funciones import resta     # Importar funciones

# Testear la funcion resta
def test_resta():
    assert resta(5, 3) == 2
    assert resta(0, 0) == 0
    assert resta(-1, -1) == 0

#decorador para parametrizar los test de resta
@pytest.mark.parametrize(
    "valor_a, valor_b, resultado",
    [
        #probando con valores nulos
        (None, 5, None),         # resta con None
        (None, None, None),      # ambos valores son None
        (2, None, None),         # uno de los valores es None

        (2, 3, -1),              # resta de dos enteros positivos
        (2, -3, 5),              # resta de un entero positivo y uno negativo
        (0, 5, -5),              # resta con cero
        ('2', 5, -3),            # un valor es cadena numérica
        (5, 2, 3),               # resta básica para asegurar funcionamiento
    ]
)
def test_resta(valor_a, valor_b, resultado):
    assert resta(valor_a, valor_b) == resultado

