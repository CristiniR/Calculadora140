# Biblioteca...................................................................................................................

import pytest

# Funções que serão testadas...................................................................................................

from Calculadora.calculadora import somar_dois_numeros, subtrair_dois_numeros, multiplicar_dois_numeros, dividir_dois_numeros

# Testes.......................................................................................................................

def test_somar_dois_numeros():
    num1 = 5
    num2 = 7
    resultado_esperado = 12    

    resultado_obtido = somar_dois_numeros(num1, num2)

    assert resultado_esperado == resultado_obtido


def test_subtrair_dois_numeros():
    num1 = 12
    num2 = 6
    resultado_esperado = 6    

    resultado_obtido = subtrair_dois_numeros(num1, num2)

    assert resultado_esperado == resultado_obtido


def test_multiplicar_dois_numeros():
    num1 = 6
    num2 = 6
    resultado_esperado = 36    

    resultado_obtido = multiplicar_dois_numeros(num1, num2)

    assert resultado_esperado == resultado_obtido


def test_dividir_dois_numeros():
    num1 = 10
    num2 = 5
    resultado_esperado = 2    

    resultado_obtido = dividir_dois_numeros(num1, num2)

    assert resultado_esperado == resultado_obtido

