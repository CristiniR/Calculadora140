# Biblioteca...................................................................................................................

import pytest

# Funções que serão testadas...................................................................................................

from Calculadora.calculadora import somar_dois_numeros, subtrair_dois_numeros, multiplicar_dois_numeros, dividir_dois_numeros, calcular_area_do_retangulo, calcular_area_do_triangulo
from utils.utils import ler_csv

# Tests........................................................................................................................

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

    
def teste_dividir_por_zero():
    num1 = 10
    num2 = 0
    resultado_esperado = 'Erro: Não é possível dividir por zero' 

    resultado_obtido = dividir_dois_numeros(num1, num2)

    assert resultado_esperado == resultado_obtido


def testar_calcular_area_do_retangulo():
    largura = 5
    comprimento = 10
    resultado_esperado = 50  

    resultado_obtido = calcular_area_do_retangulo(largura, comprimento)

    assert resultado_esperado == resultado_obtido


def testar_calcular_area_do_triangulo():
    largura = 5
    comprimento = 10
    resultado_esperado = 25  

    resultado_obtido = calcular_area_do_triangulo(largura, comprimento)

    assert resultado_esperado == resultado_obtido
 

# Data Driven Tests (TDD).......................................................................................................

@pytest.mark.parametrize('num1, num2, resultado_esperado',
                         [
                           (5, 7, 12),
                           (0, 8, 8),
                           (10, -15, -5),
                           (6, 0.75, 6.75),
                         ]
                        )

def test_somar_dois_numeros_lista(num1, num2, resultado_esperado):    

    resultado_obtido = somar_dois_numeros(num1, num2)

    assert resultado_esperado == resultado_obtido


@pytest.mark.parametrize('largura, comprimento, resultado_esperado',
                         [
                           (5, 7, 35),
                           (6, 8, 48),
                           (10, 15, 150),
                           (6, 0.75, 4.50),
                         ]
                        )

def testar_calcular_area_do_retangulo(largura, comprimento, resultado_esperado):
    
    resultado_obtido = calcular_area_do_retangulo(largura, comprimento)

    assert resultado_esperado == resultado_obtido


# Usando massa de dados CSV.....................................................................................................

@pytest.mark.parametrize('num1, num2, resultado_esperado',
                        ler_csv('./fixtures/massa_somar.csv')
                        )

def test_somar_dois_numeros_csv(num1, num2, resultado_esperado):    

    resultado_obtido = somar_dois_numeros (float(num1), float(num2))

    assert float(resultado_esperado) == resultado_obtido


@pytest.mark.parametrize('largura, comprimento, resultado_esperado',
                        ler_csv('./fixtures/massa_retangulo.csv')
                        )

def testar_calcular_area_do_retangulo(largura, comprimento, resultado_esperado):
    
    resultado_obtido = calcular_area_do_retangulo(float(largura), float(comprimento))

    assert float(resultado_esperado) == resultado_obtido
