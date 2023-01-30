''''
 En aquest arxiu s’hi crearà una funció on demanarà a l’usuari que inserti 2 números i
 el programa li dirà quin és el més gran i quin el més petit. Si son iguals sortirà que son iguals.
'''

def numero_mayor():
    a = int(input("Escribe a:  "))
    b = int(input("Escribe b:  "))
    if a > b:
     print ('{a} es mayor que {b}'.format(a=a,b=b))
    elif b < a:
     print ('{b} es mayor que {a}'.format(a=a,b=b))
    else:
     print('{b} son iguales {a}'.format(a=a,b=b))



