"""
import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Importar funciones
from src.funciones import suma

# Testear la funcion suma
def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0
    assert suma(0, 0) == 0

#decorador para parametrizar los test de suma
@pytest.mark.parametrize(
    "valor_a, valor_b, resultado",
    [
        # testear con valores nulos
        (None, -2, None),    
        (10, None, None), 
        (None, None, None),

        (1, 1, 2),                # suma de dos enteros positivos
        (3, -2, 1),               # suma de un entero positivo y uno negativo
        (7, 0, 7),                # suma con cero
        ('6', 6, 12),             # un valor es cadena numérica
        (5, 5, 10),               # suma básica para asegurar funcionamiento      
    ]
)
# parametrizar los test de suma 
def test_suma_parametros(valor_a,valor_b,resultado):
    assert suma(valor_a, valor_b) == resultado


def test_suma_str_letras():
    assert suma('a',2) == None

    """