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
    ganar1 = total1 * 100/votos
    ganar2 = total2 * 100/votos
    if total1 > total2:
        print ('ha ganado ',candidato1, ' con un total de ',total1,' votos obteniendo un ',ganar1,'%. entre tanto ',candidato2,'ha obtenido un total de ',total2,' votos obteniendo el ',ganar2,'%')
    elif total2 > total1:
        print('ha ganado ',candidato2, 'con un total de ', total2,
          ' votos obteniendo un ', ganar2, '%. entre tanto ',candidato1, 'a ha obtenido un total de ', total1, ' votos obteniendo el ', ganar1, '%')
    continuar = (input('¿desea realizar una nueva elección? Si(s) No(n) '))
    if continuar == 's':
        return elecciones()
    elif continuar == 'n':
        return 0

elecciones()
print ('hasta luego')