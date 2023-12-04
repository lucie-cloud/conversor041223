# https://github.com/felippecardoso7/Pycalcsimple/blob/master/calcgui1.py

# Conversor de Unidades: Graus Celsius e Fahrenheit

# Entrada
def menu_inicial():
    print('Programa para Conversão de Temperaturas')
    print('1. Converter de Celsius para Fahrenheit')
    print('2. Converter de Fahrenheit para Celsius')

# Processamento
def cel_fahr():
    Cel = float(input('Entre com a temperatura em graus Celsius: '))
    Fahr = Cel * (9 / 5) + 32
    print('Valor em Fahrenheit: {0}°F'.format(Fahr))

def fahr_cel():
    Fahr = float(input('Entre com a temperatura em graus Fahrenheit: '))
    Cel = (Fahr - 32) * (5 / 9)
    print('Valor em Celsius: {0}°C'.format(Cel))

# Saida
if __name__=='__main__':
    menu_inicial()
    escolha = input('Escolha o tipo de conversão que deseja realizar: ')

    if escolha == '1':
        cel_fahr()

    if escolha == '2':
        fahr_cel()