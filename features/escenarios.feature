Feature: Resta de dos números
  Para asegurarme de que la función de resta funciona correctamente,
  como desarrollador,
  quiero probar diferentes casos para la operación de resta.

  Scenario: Resta de dos números positivos
    Given que tengo los números 7 y 3
    When resto los dos números
    Then el resultado debe ser 4

  Scenario: Resta de un número positivo y un número negativo
    Given que tengo los números 7 y -3
    When resto los dos números
    Then el resultado debe ser 10

  Scenario: Resta de un número y cero
    Given que tengo los números 7 y 0
    When resto los dos números
    Then el resultado debe ser 7

  Scenario: Resta de cero y un número
    Given que tengo los números 0 y 5
    When resto los dos números
    Then el resultado debe ser -5

  Scenario: Resta de dos números negativos
    Given que tengo los números -7 y -3
    When resto los dos números
    Then el resultado debe ser -4
