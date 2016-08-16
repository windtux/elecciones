def elecciones():

    import random
    candidato1 = (input('introduzca el nombre del primer candidato '))
    candidato2 = (input('introduzca el nombre del segundo candidato '))
    total1 = 0
    total2 = 0
    votos = int(input('introduzca numero total de votantes '))
    for a in range (votos):
        valor = random.randint(1,2)
        if valor == 1:
            total1+=1
        elif valor == 2:
            total2+=1
        elif valor == 3:
            total3+=1
    ganar1 = total1 * 100/votos
    ganar2 = total2 * 100/votos
    if total1 > total2 and total1:
        print ('ha ganado ',candidato1, ' con un total de ',total1,' votos obteniendo un ',ganar1,'%. entre tanto ',candidato2,'ha obtenido un total de ',total2,' votos obteniendo el ',ganar2,'%.')
    elif total2 > total1:
        print('ha ganado ',candidato2, 'con un total de ', total2,
          ' votos obteniendo un ', ganar2, '%. entre tanto ',candidato1, 'a ha obtenido un total de ', total1, ' votos obteniendo el ', ganar1, '%')
    return 0


import asamblea
print ('bienvenidos(as) al juego de emulacion electoral, la primera fase del juego consistirá en elegir un presidente entre dos candidatos que usted añadirá, y luego se pasará a la fase de eleccion de la asamblea o parlamento. Comencemos pues con las elecciones')
elecciones()
from asamblea import *
asamblea()
print ('hasta luego')