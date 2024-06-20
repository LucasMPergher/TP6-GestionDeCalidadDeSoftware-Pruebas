# tests/test_integracion.py

import pytest
from src.funciones import suma, resta, cuadrado_binomio

def test_integracion_suma_resta():
    a = 5
    b = 3
    resultado_suma = suma(a, b)
    resultado_resta = resta(a, b)
    
    # Verificación de la integración de suma y resta
    # La suma de 'a' y 'b' menos 'b' debería ser igual a 'a'
    assert resta(resultado_suma, b) == a
    # La resta de 'a' y 'b' más 'b' debería ser igual a 'a'
    assert suma(resultado_resta, b) == a

def test_integracion_resta_cuadrado_binomio():
    a = 4
    b = 2
    resultado_resta = resta(a, b)
    resultado_cuadrado_binomio = cuadrado_binomio(resultado_resta, b)
    
    # Verificación de la integración de resta y cuadrado del binomio
    # El cuadrado del binomio de (a - b) y b debería ser igual a (a - b)² + 2*(a - b)*b + b²
    assert resultado_cuadrado_binomio == (resultado_resta**2 + 2*resultado_resta*b + b**2)

def test_integracion_compleja():
    a = 7
    b = 3
    c = 2
    
    resultado_suma = suma(a, b)
    resultado_resta = resta(resultado_suma, c)
    resultado_cuadrado_binomio = cuadrado_binomio(resultado_resta, b)
    
    # Verificación de una integración más compleja
    # Realizar una serie de operaciones y verificar el resultado final
    assert resultado_cuadrado_binomio == (resultado_resta**2 + 2*resultado_resta*b + b**2)

