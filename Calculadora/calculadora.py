def somar_dois_numeros(num1, num2):
    return num1 + num2

def subtrair_dois_numeros(num1, num2):
    return num1 - num2

def multiplicar_dois_numeros(num1, num2):
    return num1 * num2

def dividir_dois_numeros(num1, num2):
    try:
        return num1 / num2
    except(ZeroDivisionError):
        return 'Erro: Não é possível dividir por zero'
    
def calcular_area_do_retangulo(largura, comprimento):
    return largura * comprimento

def calcular_area_do_triangulo(largura, comprimento):
    return largura * comprimento / 2
