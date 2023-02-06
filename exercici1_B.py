"""Crear una funció on demanarà a l’usuari que inserti 2 números.
El programa li dirà quin és el més gran i quin el més petit.
Si son iguals, no sortirà cap missatge.
"""
def mesPetit ():
    x = int(input("Escriu en valor per x: "))
    y = int(input("Escriu en valor per y: "))
    if (x > y):
        print('{x} es mes gran que {y}'.format(x=x,y=y))
    elif(x < y):
        print('{x} es mes petit que {y}'.format(y=y,x=x))
    else:
        pass

mesPetit()