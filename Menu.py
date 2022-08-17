from Sql import tp
print ('---RISTORANTI LA PAROLACCIA TRATTORIA---')

print ('1-Hacer una reserva..')

print ('2-Ver reservas.')

print ('3-Modificar reserva.')

print ('4-Eliminar reserva.')

print ('5-Salir del programa.')


while True:

    opc = int (input ('Ingrese una opcion: '))

    if opc == 1:
        ver=tp()
        ver.reservar()
        ver.reservar2()

    elif opc == 2:
        ver=tp()
        ver.ver_cliente()
      
    elif opc == 3:
        ver=tp()
        ver.ver_reservas()
        print ('')
        ver.ver_cliente()
        ver.Actualizar_modificar()

    elif opc == 4:
        ver=tp()
        ver.ver_reservas()
        print ('')
        ver.eliminar_reserva()    

    elif opc == 5:
        print ('Fin del programa')
        break

    else: print ('Opcion no valida!. Intentelo nuevamente')   

    continue

