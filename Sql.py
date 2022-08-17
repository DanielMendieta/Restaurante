import mysql.connector 

class tp():
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = '',
                database = 'ristoranti'
                                    )

            if self.conexion.is_connected():
                print ('Conexion Exitosa!')

        except:
            print ('No se pudo realizar la conexion') 

    
    def reservar (self):
        try:
            cursor = self.conexion.cursor ()
            dni = int (input('Ingrese Numero de DNI: '))
            nombre = input ('Ingrese Nombre: ')
            apellido = input ('Ingrese Apellido: ')
            tel = int (input ('Ingrese un celular: '))
            sql = "INSERT INTO CLIENTE  (dni, nombre, apellido, telefono)  values ({0},'{1}','{2}',{3})".format(dni, nombre, apellido, tel )    
            cursor.execute (sql)
            self.conexion.commit()
        except:('Fallo')    
    
    def reservar2 (self):
        try:
            cursor = self.conexion.cursor ()
            dni = int (input('Ingrese número de dni: '))  #0
            id_reserva = int (input ('Ingrese Codigo de reserva: '))  #1 
            dia = input('Ingrese fecha que desea hacer la reserva: ') #2
            hora = input ('Ingrese hora de la reserva: ') #3
            cantidad = int (input('¿Cuantos comensales son?: '))  #4
            sqll = "INSERT INTO RESERVA (dni, id_reserva, dia, hora ,cantidad_Comensales) values ({0}, {1}, '{2}', '{3}', {4})".format (dni, id_reserva, dia, hora, cantidad)
            cursor.execute (sqll)
            self.conexion.commit()
            print ('Reserva exitosa!')

        except: print ('No se pudo hacer la reserva intentelo nuevamente')            
    
    """
    def ver_reservas(self):

        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT * FROM RESERVA")
            respuesta = cursor.fetchall()
            for fila in respuesta:
                print ('',"\n",'Datos de la reserva: ', "\n",'Dni: ',fila [0],"\n", 'Id_Reserva: ',fila [1],"\n", 'Dia: ', fila [2],"\n", 'Hora: ', fila [3],"\n", 'Cantidad de comensales: ', fila [4],'')

        except:
            print ('Ocurrio un error')
    """

    def ver_cliente(self):

        try:
            cursor = self.conexion.cursor()
            cursor.execute("select * from cliente INNER JOIN reserva on cliente.dni = reserva.dni")
            respuesta = cursor.fetchall()
            for fila in respuesta:
                print ('',"\n",'Datos del cliente: ', "\n",'DNI: ',fila [0],"\n", 'Nombre: ',fila [1],"\n", 'Apellido: ', fila [2],"\n", 'Telefono: ', fila [3],"\n",'DNI: ', fila [4],"\n", 'id_reserva: ', fila [5],"\n", 'Día: ', fila [6],"\n", 'Hora: ', fila [7],"\n", 'Cantidad_Comensales: ', fila [8])

        except:
            print ('Ocurrio un error')

    

    def Actualizar_modificar (self):

        try:
            cursor = self.conexion.cursor ()
            print('¿Que desea modificar?"\n"1-Día"\n"2-Hora"\n"3-Cantidad De Comensales"\n"4-Nombre"\n"5-Apellido')
            opcion = int (input('Ingrese la opcion deseada: '))  
            if opcion == 1:
                id = int (input('Ingrese el codigo de reserva: '))
                diaNuevo = input ('Ingrese el nuevo día: ') 
                sql = "Update reserva set dia = '{}' where id_reserva = {}; ".format (diaNuevo, id)
                cursor.execute (sql)
                self.conexion.commit()
                print ('Se cambio la fecha correctamente!')
            
             
            elif opcion == 2:
                id = int (input('Ingrese el codigo de reserva: '))
                Horanuevo = input ('Ingrese el nuevo horario: ')
                sql = "Update reserva set hora = '{}' where id_reserva = {}; ".format (Horanuevo, id)
                cursor.execute (sql)
                self.conexion.commit()
                print ('Se cambio la hora correctamente!')
            

            elif opcion == 3: 
                id = int (input('Ingrese el codigo de reserva: '))
                comensales = int (input ('Cuantos comensales son? : '))
                sql = "Update reserva set cantidad_comensales = {} where id_reserva = {}; ".format (comensales, id)
                cursor.execute (sql)
                self.conexion.commit()
                print ('Cambio realizado con exito!')

            elif opcion == 4:    
                dni = int (input('Ingrese el dni: '))
                nombre = input ('Ingrese el nombre nuevo : ')
                sql = "Update cliente set nombre = '{}' where dni = {}; ".format (nombre, dni)
                cursor.execute (sql)
                self.conexion.commit()
                print ('Se cambio el nombre correctamente!')

            elif opcion == 5:    
                dni = int (input('Ingrese el dni: '))
                apellido = input ('Ingrese el nombre nuevo : ')
                sql = "Update cliente set apellido = '{}' dni = {}; ".format (apellido, dni)
                cursor.execute (sql)
                self.conexion.commit()
                print ('Se cambio el apellido correctamente!')    
            else:print ('Nose puedo realizar el cambio intentelo nuevamente!')      

        except: print ('Ocurrio un error intentelo nuevamente')     
    
    def eliminar_reserva (self):
        try:
            cursor = self.conexion.cursor ()
            dni = int (input('DNI por favor: '))
            confirmar = input ('¿Esta seguro? si o no: ').lower ()
            if confirmar == 'si':
                sql = "delete from reserva where dni = {}".format (dni)
                cursor.execute (sql)
                self.conexion.commit()
                print ('Reserva Eliminada!')
            else: print ('No se pudo eliminar la reserva')

        except: print ('ocurrio un error ')        