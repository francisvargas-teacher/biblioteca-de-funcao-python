def somar(a, b):
    pass
def subtrair(a, b):
    pass

def multiplicar(a, b):
    pass

def dividir(a, b):
    pass
def eh_par(numero):
    pass
def calcular_media(numeros):
    pass
def maior_valor(numeros):
    pass

def calcular_fatorial(numero):
    pass

def gerar_tabuada(numero):
    tabuada = f"Aqui está a tábuada de {numero}\n"
    for i in range(1, 11):
        tabuada += f'{i} x {numero} é {i*numero}\n'
    return tabuada

print(gerar_tabuada(2))
