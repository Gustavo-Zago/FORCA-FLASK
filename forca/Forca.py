import random
import os

acertos, erros, i = 0, 1, 0
letras_chutadas, escolhe, a = [], ['pera', 'banana', 'zago', 'creatina','isabela','joao','dedo','paralelepipedo','abacaxi'], []

def caso_1():
    return '''
    _____
    |   |
        |
        |
        |
        |
    ---'''

def caso_2():
    return '''
    _____
    |   |
    O   |
        |
        |
        |
    ---'''

def caso_3():
    return '''
    _____
    |   |
    O   |
    |   |
        |
        |
    ---'''

def caso_4():
    return '''
    _____
    |   |
    O   |
   /|   |
        |
        |
    ---'''

def caso_5():
    return '''
    _____
    |   |
    O   |
   /|\\  |
        |
        |
    ---'''

def caso_6():
    return '''
    _____
    |   |
    O   |
   /|\\  |
   /    |
        |
    ---'''

def caso_7():
    return '''
    _____
    |   |
    O   |
   /|\\  |
   / \\  |
        |
    ---'''
def printa():
    return print(" ".join(map(str, a)))
def printaerro():
    return print("Letras CHUTADAS: " + ", ".join(map(str, letras_chutadas)))
switch = {
    1: caso_1,
    2: caso_2,
    3: caso_3,
    4: caso_4,
    5: caso_5,
    6: caso_6,
    7: caso_7,
}
while True:
    x = random.choice(escolhe)
    for i in range(len(x)):
        a.append(' _ ')
    printa()

    while True:
        b = input('Dê um chute:')
        while b in letras_chutadas:
            b = input('Essa letra já foi chutada! Tente novamente: ')

        if x.count(b) > 0:
            for i, letra in enumerate(x):
                if letra == b:
                    a[i] = letra 
                    acertos+=1
            letras_chutadas.append(b)
            printaerro()
            print(switch[erros]())
            printa()
            if len(x) == acertos:
                print(switch[erros]())
                printa()
                print('Você é um campeão!!!')
                print('Acertos:',acertos)
                printaerro()
                break
        else:
            letras_chutadas.append(b)
            printaerro()
            erros+=1
            print(switch[erros]())
            printa()

            if(erros==7):
                print('Acertos:',acertos)
                print('Erros:',erros)
                printa()
                printaerro()
                break
    r = input('Deseja jogar novamente?s/n')
    if r != 's':
        break
    else:
        os.system("cls")
        acertos, erros, i = 0, 1, 0
        letras_chutadas, a = [], []