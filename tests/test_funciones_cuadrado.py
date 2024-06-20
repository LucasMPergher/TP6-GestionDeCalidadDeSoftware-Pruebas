"""
import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Importar funciones
from src.funciones import cuadrado_binomio

# Testear la funcion cuadrado_binomio
def test_cuadrado_binomio():
    assert cuadrado_binomio(2, 3) == 25
    assert cuadrado_binomio(0, 0) == 0
    assert cuadrado_binomio(1, 1) == 4

@pytest.mark.parametrize(
    "valor_a, valor_b, resultado",
    [
        (2, 3, 25),              # cuadrado de binomio con dos enteros positivos
        (2, -3, 1),              # cuadrado de binomio con un entero positivo y uno negativo
        (0, 5, 25),              # cuadrado de binomio con cero
        (None, 5, None),         # cuadrado de binomio con None
        (None, None, None),      # ambos valores son None
        (2, None, None),         # uno de los valores es None
        ('2', 3, 25),            # un valor es cadena numérica
        (3, 4, 49),              # cuadrado básico para asegurar funcionamiento
    ]
)
def test_cuadrado_binomio(valor_a, valor_b, resultado):
    assert cuadrado_binomio(valor_a, valor_b) == resultado

    """