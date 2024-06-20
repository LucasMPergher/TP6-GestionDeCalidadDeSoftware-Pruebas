# features/steps/steps.py

from behave import given, when, then
from src.funciones import resta

@given('que tengo los números {a:d} y {b:d}')
def step_given_tengo_los_numeros(context, a, b):
    context.a = a
    context.b = b

@when('resto los dos números')
def step_when_resto_los_dos_numeros(context):
    context.resultado = resta(context.a, context.b)

@then('el resultado debe ser {esperado:d}')
def step_then_el_resultado_debe_ser(context, esperado):
    assert context.resultado == esperado, f"Esperado {esperado}, pero fue {context.resultado}"

