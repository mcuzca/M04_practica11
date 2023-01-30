"""Crear una funció on demanarà a l’usuari l’edat i els ingressos que té mensuals.
Si la resposta de l’edat és ser igual o major de 18 anys i els ingressos son majors de 1200,
sortira per pantalla el següent misatge: “És necessari que facis la declaració d’hisenda”.
En cas que alguna de les dues opcions no es compleixi, sortira per pantalla el següent misatge: “Encara no pots fer la declaració”.
"""
def ingressos ():
    edad = int(input("Quina edad tens? "))
    ingressos = int(input("Quin sons els teus ingresos? "))
    if (edad >= 18 and ingressos > 1200):
        print('És necessari que facis la declaració d’hisenda. Tens {edad} anys i els teus ingressos son de {ingressos}€'.format(edad=edad,ingressos=ingressos))
    else:
        print('Encara no pots fer la declaració. Tens {edad} anys i els teus ingressos son de {ingressos}€'.format(edad=edad,ingressos=ingressos))


ingressos()