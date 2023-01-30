"""Crear una funció on demanarà a l’usuari que indiqui
 un número i aquest li indicarà si és parell o senar.
"""
def parellSenar ():
    x = int(input("Escriu en valor per x: "))
    if x % 2 == 0:
        print('{x} es parell'.format(x=x))
    else:
        print('{x} es senar'.format(x=x))

parellSenar()