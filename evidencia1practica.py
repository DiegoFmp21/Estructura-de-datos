#Evidencia 1
from datetime import datetime, timedelta
import datetime


registro_de_datos = {}
clave_p = 0
biblioteca_de_citas = {}
folio_cita = 100
biblioteca_de_citas_programadas= {}

def registro_pacientes( registro_de_datos):
    
    #Apellido Paterno
    while True:
        primer_apellido = input("\n¿Cual es tu primer apellido?\n")
        if  primer_apellido == "":
            print("El apellido no debe omitirse. Ingrese de nuevo")            
            continue
        elif primer_apellido.isalpha():
            break
        else:
            print("El dato no puede ser numerico. Ingrese de nuevo")
            continue
        
        
    while True:
        segundo_apellido = input("¿Cual es tu segundo apellido? (puede omitirlo si no lo posee)\n")
        if segundo_apellido.isalpha():
            break
        elif segundo_apellido == "":
            break
        else:
            print("El dato no debe ser numerico. Ingrese de nuevo")
            continue

    #Nombre del paciente
    
    while True:
        nombre = input("¿Cual es tu nombre?\n")
        if nombre == "":
            print("El valor no debe omitirse. Ingrese de nuevo")
        elif nombre.isalpha():
            break
        else:
            print("El dato no puede ser numerico. Ingrese de nuevo")
            continue
    
    #Fecha de nacimiento
    while True:
        try:
            fecha_str = input("Ingrese su fecha de nacimiento con el siguiente formato (mm/dd/aaaa): ")
            fecha_procesada = datetime.datetime.strptime(fecha_str, "%m/%d/%Y").date()
            fecha_actual = datetime.datetime.now().date()

            if fecha_procesada > fecha_actual:
                print("Error: La fecha ingresada debe ser anterior al día actual.")
                continue
            elif fecha_procesada.month > 12:
                print("Error: El mes ingresado es inválido.")
                continue
            else:
                print("Fecha ingresada correctamente")
                fecha_procesada = fecha_procesada.strftime('%m/%d/%Y')
                break
        except ValueError:
            print("Error: Formato de fecha invalido. Por favor, ingrese la fecha en el formato indicado.")

    print(f"La clave del paciente es {clave_p}\n")
    registro_de_datos[clave_p]= [primer_apellido, segundo_apellido, nombre, fecha_procesada]
    print(registro_de_datos)

def registro_citas(biblioteca_de_citas):
            
    #Identificador de claves
    while True:
        seleccion_clave_str = input("\nDigame la clave del paciente: ")
        try:
            seleccion_clave = int(seleccion_clave_str)
            if seleccion_clave in registro_de_datos:
                break
            else:
                print("Su clave no esta registrada")
                continue
        except ValueError:
            print("El dato que ingreso no es de tipo numerico")
            continue
        
    #Registro de fecha
    while True:
        try:
            fecha_limite_print = (datetime.date.today() + timedelta(days = 60))
            print(f"Fecha limite de cita {fecha_limite_print}")
            fecha_cita_str = input("Introduzca la fecha en la que quiera consultar (mm/dd/aaaa): ")
                
            fecha_cita = datetime.datetime.strptime(fecha_cita_str, "%m/%d/%Y").date()
            fecha_actual = datetime.date.today()
            fecha_limite = fecha_actual + timedelta(days = 60)

            if fecha_actual > fecha_cita:
                print("Su fecha no puede ser anterior al dia de mañana")
                continue
            elif fecha_cita <= fecha_limite:
                fecha_cita_print = fecha_cita.strftime('%m/%d/%Y')
                #print("Su fecha es valida")
                break
            else:
                print("Ingrese una fecha no mayor a 60 dias despues del dia de hoy")
                continue
        except ValueError:
            print("La fecha no coincide con el formato indicado")
            continue

    #Horarios
    while True:
        try:
            turno_de_cita = int(input("Introduzca el horario que desea: (1-Mañana 2-Mediodia 3-Tarde) "))
            if turno_de_cita in [1,2,3]:
                print("Su horario se registro correctamente \n")
                break
            else:
                print("Su opcion no coincide con ninguna de las opciones")
        except Exception:
            print("El valor debe ser numerico")
            continue

    print(f"El folio de su cita {folio_cita}\n")

    biblioteca_de_citas[folio_cita]=[seleccion_clave,fecha_cita_print,turno_de_cita] 
    print(biblioteca_de_citas)

def info_cita():
   
    while True:
        seleccion_folio_cita = input("\nIngrese el folio de la cita: ")
        try:
            seleccion_folio_cita = int(seleccion_folio_cita)
            if seleccion_folio_cita in biblioteca_de_citas:
                break
            else:
                print("Su folio no esta registrado")
                continue
        except ValueError:
            print("El folio debe ser un número entero.")

    while True:
        seleccion_clave= input("Digame la clave del paciente: ")
        try:
            seleccion_clave = int(seleccion_clave)
            if seleccion_clave == biblioteca_de_citas[seleccion_folio_cita][0]:
                break
            else:
                print("La clave del paciente no coincide con ningun folio a su nombre")
                continue
        except ValueError:
            print("El dato que ingreso no es de tipo numerico")
            continue
    
    hora_llegada = datetime.datetime.now().strftime("%H:%m:%S")  # Obtener la hora actual del sistema

    while True:
        peso_str = input("Ingrese el peso del paciente en kilogramos: ")
        try:
            peso = float(peso_str)
            if peso <= 0:
                print("El peso no puede ser menor o igual a cero, ingrese nuevamente")
                continue
            else:
                print("Peso registrado")
                break
        except ValueError:
            print("El dato ingresado no es de tipo numerico")
            continue

    while True:
        estatura_str = input("Ingrese la estatura en centimetros: ")
        try:
            estatura = float(estatura_str)
            if estatura <= 0:
                print("La estatura no puede ser menor o igual a cero, ingrese nuevamente")
                continue
            else:
                print("Estatura registrado")
                break
        except ValueError:
            print("El dato ingresado no es de tipo numerico")
            continue
    fecha_cita= biblioteca_de_citas[seleccion_folio_cita][1]

    # Mostrar los datos ingresados
    biblioteca_de_citas_programadas[seleccion_folio_cita] = (seleccion_clave, fecha_cita, hora_llegada, peso, estatura)
    print("Información de la cita actualizada correctamente:")
    print(biblioteca_de_citas_programadas)

def buscar_citas_por_periodo(biblioteca_de_citas, biblioteca_de_citas_programadas, registro_de_datos):
    while True:
        periodo_inicio_str = input("\nIngrese la fecha de inicio del periodo (mm/dd/yyyy): ")
        try:
            periodo_inicio = datetime.datetime.strptime(periodo_inicio_str, "%m/%d/%Y").date()
            break
        except ValueError:
            print("Fecha de inicio invalida. Intente nuevamente.")
            continue

    while True:
        try:
            periodo_fin_str = input("Ingrese la fecha de fin del periodo (mm/dd/yyyy): ")
            periodo_fin = datetime.datetime.strptime(periodo_fin_str, "%m/%d/%Y").date()
            if periodo_fin >= periodo_inicio:
                break
            else:
                print("La fecha de fin debe ser posterior o igual a la fecha de inicio.")
                continue
        except ValueError:
            print("Fecha de fin invalida. Intente nuevamente.")
            continue

    #print(f"Fecha de inicio del periodo: {periodo_inicio}")
    #print(f"Fecha de fin del periodo: {periodo_fin}")

    citas_en_periodo = []

    # Recorre las citas en biblioteca_de_citas
    for folio, cita_info in biblioteca_de_citas.items():
        clave_paciente, fecha_cita, turno_de_cita = cita_info

        fecha_cita_dt = datetime.datetime.strptime(fecha_cita, "%m/%d/%Y").date()
        if periodo_inicio <= fecha_cita_dt <= periodo_fin:
            if folio in biblioteca_de_citas_programadas:
                # Si hay información adicional en biblioteca_de_citas_programadas, se agrega a la lista de citas
                clave_paciente_prog, fecha_cita_prog, hora_llegada, peso, estatura = biblioteca_de_citas_programadas[folio]
                nombre_paciente = " ".join(registro_de_datos[clave_paciente_prog][:3])  
                cita = (folio, clave_paciente_prog, nombre_paciente, fecha_cita_prog, hora_llegada, peso, estatura)
                citas_en_periodo.append(cita)
            else:
                # Si no hay información adicional, se agrega solo la información básica
                nombre_paciente = " ".join(registro_de_datos[clave_paciente][:3])
                cita = (folio, clave_paciente,nombre_paciente, fecha_cita, None, None, None)
                citas_en_periodo.append(cita)

    # Imprimir las citas encontradas
    if citas_en_periodo:
        print("\nCitas encontradas en el periodo indicado:")
        print("{:<25} {:<20} {:<25} {:<25} {:<15} {:<15} {:<15} {:<15}".format("Folio de cita", "Clave del paciente", "Nombre del paciente", "Fecha de la cita", "Hora de llegada", "Peso", "Estatura", "Horario de la cita"))
        print("-" * 140)
        for folio, clave_paciente, nombre_paciente, fecha_cita, hora_llegada, peso, estatura in citas_en_periodo:
            hora_llegada = hora_llegada if hora_llegada is not None else "N/A"
            peso = peso if peso is not None else "N/A"
            estatura = estatura if estatura is not None else "N/A"
            print(f"{folio:<25} {clave_paciente:<20} {nombre_paciente:<25} {fecha_cita:<25} {hora_llegada:<15} {peso:<15} {estatura:<15} {turno_de_cita:<15}")
    else:
        print("No hay citas en el periodo indicado")

def buscar_citas_por_paciente(biblioteca_de_citas, biblioteca_de_citas_programadas, registro_de_datos):  
    #Busqueda de citas por clave de paciente 
    print("\nBusqueda de citas por clave del paciente")
    clave_paciente_str = input("Ingrese la clave del paciente: ")
    try:
        clave_paciente = int(clave_paciente_str)
    except ValueError:
        print("La clave del paciente debe ser numerico. Ingrese de nuevo")
    
    citas_por_clave= []

    # Recorre las citas en biblioteca_de_citas
    for folio, cita_info in biblioteca_de_citas.items():
        clave_paciente_cita, fecha_cita, turno_de_cita = cita_info

        if clave_paciente_cita == clave_paciente:# Si hay información adicional en biblioteca_de_citas_programadas, se agrega a la lista de citas
            if folio in biblioteca_de_citas_programadas:  
                clave_paciente_prog, fecha_cita_prog, hora_llegada, peso, estatura = biblioteca_de_citas_programadas[folio]
                nombre_paciente = " ".join(registro_de_datos[clave_paciente_prog][:3])
                cita = (folio, clave_paciente_prog ,nombre_paciente, fecha_cita_prog, hora_llegada, peso, estatura)
                citas_por_clave.append(cita)
            else:
                nombre_paciente = " ".join(registro_de_datos[clave_paciente][:3])
                cita = (folio, clave_paciente, nombre_paciente, fecha_cita, None, None, None)# Si no hay información adicional, se agrega solo la información básica
                citas_por_clave.append(cita)

    # Imprimir las citas encontradas
    if citas_por_clave:
        print("\nCitas encontradas con la clave del paciente:")
        print("{:<25} {:<20} {:<25} {:<25} {:<15} {:<15} {:<15} {:<15}".format("Folio de cita", "Clave del paciente", "Nombre del paciente", "Fecha de la cita", "Hora de llegada", "Peso", "Estatura", "Horario de la cita"))
        print("-" * 140)
        for folio, clave_paciente, nombre_paciente, fecha_cita, hora_llegada, peso, estatura in citas_por_clave:
            hora_llegada = hora_llegada if hora_llegada is not None else "N/A"
            peso = peso if peso is not None else "N/A"
            estatura = estatura if estatura is not None else "N/A"
            print(f"{folio:<25} {clave_paciente:<20} {nombre_paciente:<25} {fecha_cita:<25} {hora_llegada:<15} {peso:<15} {estatura:<15} {turno_de_cita:<15}")
    else:
        print("No hay citas coincidentes con la clave")

def buscar_paciente_por_clave(registro_de_datos, clave_busqueda):
    pacientes_encontrados = []

    for clave, datos_paciente in registro_de_datos.items():
        if clave == clave_busqueda:
            pacientes_encontrados.append((clave, datos_paciente))

    return pacientes_encontrados

def buscar_paciente_por_nombre(registro_de_datos):
    while True:
        nombre_buscado = input("\nIngrese el nombre del paciente que desea buscar: ").strip().upper()

        while any(char.isdigit() for char in nombre_buscado):
            print("El nombre no puede contener números.")
            nombre_buscado = input("\nIngrese el nombre del paciente que desea buscar: ").strip().upper()
        break
    pacientes_encontrados = []

    for clave, datos_paciente in registro_de_datos.items():
        nombre_completo = f"{datos_paciente[0]} {datos_paciente[1]} {datos_paciente[2]}".upper()
        if nombre_buscado in nombre_completo:
            pacientes_encontrados.append((clave, datos_paciente))

    if pacientes_encontrados:
        print("Busqueda por nombre")
        print("\n------------------REPORTE DE PACIENTES REGISTRADOS------------------")
        print("{:<10} {:<20} {:<20} {:<20} {:<20}".format("Clave", "Primer Apellido", "Segundo Apellido", "Nombre", "Fecha de Nacimiento"))
        print("-" *105)
        for clave, datos_paciente in pacientes_encontrados:
            primer_apellido = datos_paciente[0]
            segundo_apellido = datos_paciente[1] if datos_paciente[2] else ""
            nombre =datos_paciente[2]
            fecha_procesada = datos_paciente[3]
            print (f"{clave:<10} {primer_apellido:<20} {segundo_apellido:<20}{nombre:<20} {fecha_procesada:<20} ")
    else:
        print("No se encontraron pacientes con ese nombre.")


#Aqui inicia el programa
while True:
    print("-------------------------------------------------------------------------") #Menu principal
    print("\nBuen dia, sea bienvenido en nuestro consultorio")
    print("Aqui esta nuestro menu de opciones: \n")
    print("1.- Registro de pacientes\n2.- Programacion de citas\n3.- Realizacion de citas programadas\n4.- Consultas y reportes\n5.- Salir del sistema")

    try:
        opcion_menu= int(input("Ingrese la opcion que desea realizar: "))  
    except:
        print("Debera de ser un valor numerico y dentro del rango de opciones")
        continue

    if opcion_menu == 1:
        clave_p= clave_p + 1 
        registro_pacientes( registro_de_datos)

    elif opcion_menu == 2:
        if clave_p == 0:
            print("\n***Debe de registra un paciente para poder continuar***")
            continue
        
        folio_cita += 1
        registro_citas(biblioteca_de_citas)

    elif opcion_menu == 3:
   
        if folio_cita == 100:
            print("\n***Debio de haber programado una cita primero***")
            continue
        
        datos_cita = info_cita()

    elif opcion_menu == 4:
        if clave_p == 0:
            print("\n***Registrar por lo menos un paciente primero***")
            continue
           
        while True: #Menu de consultas y reportes
            while True:
                print("\n       Consultas y Reportes \nRegistre a que informacion desea acceder") 
                print("1. Reporte de citas")
                print("2. Reporte de pacientes")
                print("3. Si desea salir a las opciones del menu")
                
                submenu_opcion_cuatro_str = input("Ingrese la opcion que desea consultar: ")
                try:
                    submenu_opcion_cuatro = int(submenu_opcion_cuatro_str)
                    if submenu_opcion_cuatro >0 and submenu_opcion_cuatro < 4:
                        break
                    else:
                        print("La opcion no esta disponible. Ingrese de nuevo \n ")
                        continue
                except ValueError:
                    print("Su valor debe ser numerico. Ingrese de nuevo")
                    continue
                
            if submenu_opcion_cuatro == 1: 
                while True:
                    if folio_cita == 100:
                        print("\n***Debio de haber programado una cita primero***")  
                        break #Regresa a Consultas y Reportes
                            
                    while True: #Menu de busqueda de citas o pacientes
                        print("\nComo desea buscar las citas\n1-Por periodo\n2-Por paciente\n3-Salir al menu de Consultas y Reportes")
                        mini_menu_citas_str = input("Ingrese la opcion: ")
                        try:
                            mini_menu_citas = int(mini_menu_citas_str)
                            if mini_menu_citas > 0 and mini_menu_citas < 4:
                                break
                            else:
                                print("La opcion no esta disponible. Ingrese de nuevo")
                                continue
                        except ValueError:
                            print("El valor ingresado no fue un numero. Ingrese de nuevo")
                            continue
                    
                    if mini_menu_citas == 1:
                        print("\nReporte de citas por periodo:")
                        buscar_citas_por_periodo(biblioteca_de_citas, biblioteca_de_citas_programadas, registro_de_datos)

                        
                    elif mini_menu_citas == 2:
                        print("\n Reporte de busqueda por clave del paciente")
                        buscar_citas_por_paciente(biblioteca_de_citas, biblioteca_de_citas_programadas, registro_de_datos)

                        
                    elif mini_menu_citas == 3:
                        break
                    else: 
                        print("Su opcion no es valida. Ingrese de nuevo")

            elif submenu_opcion_cuatro == 2: #Menu para consulta de pacientes

                while True:
                    
                    while True:
                        print("\nComo desea buscar los pacientes\n1-Listado Completo de Pacientes\n2-Busqueda por Clave de Pacientes\n3-Busqueda por Apellidos y Nombre\n4- Salir al menu Consultas y Reportes")
                        mini_menu_pacientes_str = input("Ingrese la opcion: ")
                        try:
                            mini_menu_pacientes = int(mini_menu_pacientes_str)
                            if mini_menu_pacientes < 5 and mini_menu_pacientes > 0:
                                break
                            else:
                                print("La opcion no esta disponible. Ingrese de nuevo \n ")
                            continue
                        except ValueError:
                            print("El valor dado debe ser numerico. Ingrese de nuevo")
                            continue
                    
                    if mini_menu_pacientes == 1:

                        print("Lista de pacientes registrados:\n") #Lista completa de pacientes

                        print("\n------------------REPORTE COMPLETO DE PACIENTES REGISTRADOS------------------")
                        print("{:<10} {:<20} {:<20} {:<20} {:<20}".format("Clave", "Primer Apellido", "Segundo Apellido", "Nombre", "Fecha de Nacimiento"))
                        print("-" *105) 
                            
                        for clave, datos_paciente in registro_de_datos.items():
                            primer_apellido = datos_paciente[0]
                            segundo_apellido = datos_paciente[1] if datos_paciente[2] else ""
                            nombre =datos_paciente[2]
                            fecha_procesada = datos_paciente[3]
                            print (f"{clave:<10} {primer_apellido:<20} {segundo_apellido:<20}{nombre:<20} {fecha_procesada:<20} ")

                    elif mini_menu_pacientes == 2:
                    
                        clave_p_busqueda_str=input("\nIntroduzca la clave del paciente a buscar: ") #Busqueda por clave
                        try: 
                            clave_p_busqueda = int(clave_p_busqueda_str)
                        except ValueError:
                            print("La clave debe ser un numero. Ingrese de nuevo")
                            continue

                        pacientes_encontrados = buscar_paciente_por_clave(registro_de_datos, clave_p_busqueda) #Funcion


                        if clave_p_busqueda in registro_de_datos:
                            print("Busqueda por clave")
                            print("\n------------------REPORTE DE PACIENTES REGISTRADOS------------------")
                            print("{:<10} {:<20} {:<20} {:<20} {:<20}".format("Clave", "Primer Apellido", "Segundo Apellido", "Nombre", "Fecha de Nacimiento"))
                            print("-" *105)
                            for clave, datos_paciente in pacientes_encontrados:
                                clave_p = clave_p
                                primer_apellido = datos_paciente[0]
                                segundo_apellido = datos_paciente[1] if datos_paciente[2] else ""
                                nombre =datos_paciente[2]
                                fecha_procesada = datos_paciente[3]
                            print (f"{clave:<10} {primer_apellido:<20} {segundo_apellido:<20}{nombre:<20} {fecha_procesada:<20} ")
                        else:
                                print("No se encontro un paciente con esa clave. Ingrese de nuevo")
                                break
        
                    elif mini_menu_pacientes == 3:
                        #El listado de pacientes buscando por el nombre
                        buscar_paciente_por_nombre(registro_de_datos)


                    elif mini_menu_pacientes == 4:
                        break 
                    else:
                        print("El valor debe estar dentro de las opciones. Ingrese de nuevo")
                        continue       
            
            elif submenu_opcion_cuatro == 3:
                break
            else:
                print("Su opcion no es valida. Ingrese de nuevo su seleccion") 

    elif opcion_menu == 5:
        seguro = 0
        while True:
            pregunta_seguridad_str = input("Seguro que deseas salir del programa(1: SI) (2: NO): ")
            try:
                pregunta_seguridad = int(pregunta_seguridad_str)
                if pregunta_seguridad == 1:
                    seguro = 1
                    break
                elif pregunta_seguridad == 2:
                    break
                else:
                    print("Opcion no disponible. Ingrese de nuevo")
                    continue
            except ValueError:
                print("El valor debe ser numerico. Ingrese de nuevo")
                continue
        if seguro == 1:
            break
    else:
        print("Tu opcion debe ser alguna de las anteriores mencionadas")
        continue