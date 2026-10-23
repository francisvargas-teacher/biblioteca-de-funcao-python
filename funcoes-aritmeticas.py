#Retornar a soma de dois números.
def somar(a, b):
   resultado = a + b
   return resultado

#Teste com entradas diferentes:
print(somar(2, 3))     
print(somar(-2, 5))
print(somar(0, 0))
print(somar(3, 10))
print(somar(-1.5, 0.5))
print(somar(1.5, 2.5))

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
    print("Aqui está a tábuada de",numero)
    for i in range(1,11):
        print(f'{i} x {numero} é {i*numero}')

gerar_tabuada(1)
gerar_tabuada(2)
gerar_tabuada(3)
gerar_tabuada(4)
gerar_tabuada(5)