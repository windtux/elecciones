def asamblea():
    import random
    print ('Ahora se elegirá la asmablea o parlamento, aqui veremos como se comportará el ente encargado de elaborar leyes y aprobar presupuestos entre otras cosas importantes. Veremos si tendrás una asamblea ultra izquierdista, izquierdista, centro-izquierda, centro-derecha, derechista, o ultra derecha')
    partido1 = (input('ingrese el nombre del partido político de la ultra-izquierda '))
    partido2 = (input('ingrese el nombre del partido politico de la izquierda '))
    partido3 = (input('ingrese el nombre del partido politico de la centro izquierda '))
    partido4 = (input('ingrese el nombre del partido politico de la centro derecha '))
    partido5 = (input('ingrese el nombre del partido de la derecha '))
    partido6 = (input('ingrese el nombre del partido de la ultra derecha '))
    total1 = 0
    total2 = 0
    total3 = 0
    total4 = 0
    total5 = 0
    total6 = 0
    votos = int(input('introduzca el numero total de votantes '))
    for a in range (votos):
        valor = random.randint(1,6)
        if valor == 1:
            total1+= 1
        elif valor == 2:
            total2+= 1
        elif valor == 3:
            total3+= 1
        elif valor == 4:
            total4+= 1
        elif valor == 5:
            total5+= 1
        elif valor == 6:
            total6+= 1
    ganar1 = total1 * 100/votos
    ganar2 = total2 * 100/votos
    ganar3 = total3 * 100/votos
    ganar4 = total4 * 100/votos
    ganar5 = total5 * 100/votos
    ganar6 = total6 * 100/votos
    print ('asi quedo tu parlamento o asamblea: ',partido1,' obtuvo ',total1,' votos para un ',ganar1,' %')
    print (partido2,' obtuvo ',total2,' votos para un ',ganar2,' %')
    print (partido3,' obtuvo ',total3, ' votos para un ',ganar3,' %')
    print (partido4,' obtuvo ',total4, ' votos para un ',ganar4,' %')
    print (partido5,' obtuvo ',total5, ' votos para un ',ganar5,' %')
    print (partido6,' obtuvo ',total6,' votos para un ',ganar6,' %')
    if total1 > total2 or total1 > total3 or total1 > total4 or total1 > total5 or total1 > total6:
        print ('el parlamento esta dominado por la faccion de la ultra-izquierda')
    elif total2 > total1 or total2 > total3 or total2 > total4 or total2 > total5 or total2 > total6:
        print ('el parlamento esta dominado por la faccion de la izquierda')
    elif total3 > total1 or total3 > total2 or total3 > total4 or total3 > total5 or total3 > total6:
        print ('el parlamento esta dominado por la faccion de la centro-ezquierda')
    elif total4 > total1 or total4 > total2 or total4 > total3 or total4 > total5 or total4 > total6:
        print ('el parlamento esta dominado por la faccion de centro derecha')
    elif total5 > total1 or total5 > total2 or total5 > total3 or total5 > total4 or total5 > total6:
        print ('el parlamento esta dominado por la faccion de derecha')
    elif total6 > total1 or total6 > total2 or total6 > total3 or total6 > total4 or total6 > total5:
        print ('el parlamento esta dominado por la faccion de la extrema derecha')
    return 0
