# modulos
import random 
import os

# listas modulo pacientes
pacientes = [] # lista para almacenar pacientes
codPacs = [] # almacena codigos de pacientes
# listas modulo medicos
medicos = [] # almacena médicos
codMeds = [] # almacena los codigos de los medicos
# listas modulo consultas
consultas = [] # almacena las consultas
codCons = []  # almacena codigos de consultas
# listas modulo tratamientos
tratamientos = []
codTrats = []

#funciones pacientes
def codeGenPac(): # generar codigo para paciente
    if len(codPacs) == 0:
        codPacs.append(1000)
    else:
        codPac = max(codPacs) + 1
        codPacs.append(codPac)


def aggPac(canPac): # agregar paciente
    for i in range(canPac):
        namePac = input("Ingrese el nombre completo del paciente: ")
        birthPac = input("Ingrese la fecha de nacimiento del paciente [dd/mm/aa]: ")
        numIdPac = input("Ingrese el número de identificación: ")
        direcPac = input("Ingrese la dirección: ")
        correoPac = input("Ingrese el correo: ")
        telPac = input("Ingrese el número de teléfono: ")
        historialPac = input("Ingrese el historial médico: ")
        codeGenPac()
        print(f"El código del paciente ha sido generado exitosamente. El código es:{max(codPacs)}")
        paciente = {
            "Nombre": namePac,
            "Fecha de nacimiento": birthPac,
            "Identificacion": numIdPac,
            "Direccion": direcPac,
            "Correo": correoPac,
            "Telefono": telPac,
            "Historial": historialPac,
            "Codigo": max(codPacs)
        }
        pacientes.append(paciente) # almacena los datos de los pacientes en la lista pacientes
    filePac = open("Pacientes.txt", "a")
    for paciente in pacientes:
        filePac.write(f"{paciente}\n")
    filePac.close()
    print()


def buscarPac(): # buscar paciente
    if not pacientes:
        print("No existen coincidencias.") 
        return
    solIdPac = input("Ingrese el número de identificación del paciente que desea buscar: ")
    for paciente in pacientes:
        if paciente["Identificacion"] == solIdPac:
            print("Se ha encontrado una coincidencia, a continuación se mostrarán los datos del paciente.")
            print("Datos del paciente:")
            print()
            print("Nombre:", paciente["Nombre"])
            print("Fecha de nacimiento:", paciente["Fecha de nacimiento"])
            print("Numero de identificacion:", paciente["Identificacion"])
            print("Direccion:", paciente["Direccion"])
            print("Correo:", paciente["Correo"])
            print("Numero de telefono:", paciente["Telefono"])
            print("Tratamientos realizados:", paciente["Historial"])
            print("Codigo:", paciente["Codigo"])
        if paciente["Historial"] == "":
            print()
            print("El paciente no tiene tratamiento en su historial.")


def editPac(): # editar paciente
    solIdPac = input("Ingrese el número de identificación del paciente que desea editar: ")
    for paciente in pacientes:
        if paciente["Identificacion"] == solIdPac:
            print()
            print("Se ha encontrado una coincidencia, a continuación se mostrarán los datos actuales del paciente.")
            print("Estos son los datos actuale del paciente: ")
            print()
            print("Nombre:", paciente["Nombre"])
            print("Fecha de nacimiento:", paciente["Fecha de nacimiento"])
            print("Número de identificación:", paciente["Identificacion"])
            print("Direccion:", paciente["Direccion"])
            print("Correo:", paciente["Correo"])
            print("Numero de telefono:", paciente["Telefono"])
            print("Tratamientos realizados:", paciente["Historial"])
            print("Codigo:", paciente["Codigo"])
            print()
            paciente["Nombre"] = input("Ingrese el nuevo nombre completo: ")
            paciente["Fecha de nacimiento"] = input("Ingrese la nueva fecha de nacimiento [dd/mm/aa]: ")
            paciente["Identificacion"] = input("Ingrese el nuevo número de identificación: ")
            paciente["Direccion"] = input("Ingrese la nueva dirección: ")
            paciente["Correo"] = input("Ingrese el nuevo correo: ")
            paciente["Telefono"] = input("Ingrese el nuevo número: ")
            paciente["Historial"] = input("Ingrese el nuevo historial médico: ")
            filePac = open("Pacientes.txt", "w")
            for paciente in pacientes:
                filePac.write(f"{paciente}\n")
            filePac.close()
            print()
            print("Datos del paciente acutalizado exitosamente.")
            return
    print("No hubo coincidencias con ese número de identificación.")
    print()


# funciones medicos 
def codeGenMed(): # generar codigo para medico
    if len(codMeds) == 0:
        codMeds.append(2000)
    else:
        codMed = max(codMeds) + 1
        codMeds.append(codMed)
   
    
def aggMed(canMed): # registrar medico
    for i in range(canMed):
        nameMed = input("Ingrese el nombre completo del médico: ")
        especialidadMed = input("Ingrese la especialidad del médico: ")
        numIdMed = input("Ingrese el número de identificación del médico: ")
        telMed = input("Ingrese el número de teléfono: ")
        correoMed = input("Ingrese el correo: ")
        codeGenMed()
        print(f"El código del médico ha sido generado exitosamente. El código es:{max(codMeds)}")
        medico = {
            "Nombre": nameMed,
            "Especialidad": especialidadMed,
            "Identificacion": numIdMed,
            "Telefono": telMed,
            "Correo": correoMed,
            "Codigo": max(codMeds)
        }
        medicos.append(medico) # almacena los datos de los medicos en la lista medicos
        print()
    fileMed = open("Medicos.txt", "a")
    for medico in medicos: 
        fileMed.write(f"{medico}\n")
    fileMed.close()
    print()
    
        
def buscarMed(): # buscar medico
    if not medicos:
        print("No hay médicos en este momento")
        return
    solIdMed = input("Ingrese el número de identificación del médico que desea buscar: ")
    found = False
    for medico in medicos:
        if medico["Identificacion"] == solIdMed:
            found = True
            print("Hay a continuación se mostrarán los datos del médico.")
            print()
            print("Datos del médico:")
            print("Nombre:", medico["Nombre"])
            print("Especialidad:", medico["Especialidad"])  
            print("Número de identificación:", medico["Identificacion"])
            print("Número de teléfono:", medico["Telefono"])
            print("Correo:", medico["Correo"])
            print("Codigo:", medico["Codigo"])
            print()
    if not found:
        print("No existe medico con esta identificación.")
        print()


def editMed(): # editar medico
    if not medicos:
        print("No hubo coincidencias con ese número de identificación.")
        return
    solIdMed = input("Ingrese el número de identificación del médico que desea buscar: ")
    found = False
    for medico in medicos:
        if medico["Identificacion"] == solIdMed:
            found = True
            print("Hay a continuación se mostrarán los datos del médico.")
            print()
            print("Datos del médico:")
            print("Nombre:", medico["Nombre"])
            print("Especialidad:", medico["Especialidad"])  
            print("Numero de identificacion:", medico["Identificacion"])
            print("Numero de telefono:", medico["Telefono"])
            print("Correo:", medico["Correo"])
            print("Codigo:", medico["Codigo"])
            print()
            medico["Nombre"] = input("Ingrese el nuevo nombre completo: ")
            medico["Especialidad"] = input("Ingrese la nueva especialidad: ")
            medico["Identificacion"] = input("Ingrese el nuevo número de identificación: ")
            medico["Telefono"] = input("Ingrese el nuevo número: ")
            medico["Correo"] = input("Ingrese el nuevo correo: ")
            fileMed = open("Medicos.txt", "w")
            for medico in medicos:
                fileMed.write(f"{medicos}\n")
            fileMed.close()
            print()
            print("Datos del médico acutalizado exitosamente.")
            return
    print()
   
 
# funciones de consulta
def codeGenCon(): # generar codigo para medico
    if len(codCons) == 0:
        codCons.append(3000)
    else:
        codCon = max(codCons) + 1
        codCons.append(codCon)


def regCon(): # registrar consulta
    print("\t\t\t\t   Bienvenido estimado usuario al módulo de consultas.")
    if not medicos:
        print("En este momento no hay médicos disponibles, por lo tanto, no se podrá realizar la consulta.")
        return
    codPacCon = int(input("Ingrese el código del paciente: "))
    found = False
    for paciente in pacientes: 
        if paciente["Codigo"] == codPacCon: 
            found = True
            conDate = input("Ingrese la fecha de la consulta [dd/mm/aa]: ")
            conDesc = input("Ingrese la descripción de la consulta: ")
            codMedCon = random.choice(medicos)["Codigo"]
            codeGenCon()
            print(f"El código del consulta ha sido generado exitosamente. El código es:{max(codCons)}")
            consulta = {
                "Codigo del paciente": codPacCon,
                "Fecha de consulta": conDate,
                "Descripcion": conDesc,
                "Codigo del medico": codMedCon,
                "Codigo de consulta": max(codCons)
            }
            consultas.append(consulta) # almacena las consultas en la lista de consultas
            print("¡Consulta registrada con éxito!")
    if not found:
        print("No existe ningún paciente con ese código.")
        return
    print()   
    fileCon = open("Consultas.txt", "a")
    fileCon.write(f"{consulta}\n")
    fileCon.close()
    print()
    

# funciones de tratamientos
def codeGenTrat(): # generar codigo para medico
    if len(codTrats) == 0:
        codTrats.append(4000)
    else:
        codTrat = max(codTrats) + 1
        codTrats.append(codTrat)
           
        
def regTrat():
    print("\t\t\t\t   Bienvenido estimado usuario al módulo de tratamientos.")
    if not medicos:
        print("En este momento no hay médicos disponibles, por lo tanto, no se podrá realizar el tratamiento.")
        return
    print("A continuación, se le va a solicitar que ingrese datos del paciente.")
    
    solCodPac = int(input("Ingrese el código del paciente: "))
    found = False
    for paciente in pacientes: 
        if paciente["Codigo"] == solCodPac: 
            found = True
            descTrat = input("Ingrese la descriptción del tratamiento: ")
            dateIni = input("Ingrese la fecha de inicio [dd/mm/aa]: ")
            dateFin = input("Ingrese la fecha de finalización previa [dd/mm/aa]: ")
            codMedTrat = random.choice(medicos)["Codigo"]
            codeGenTrat()
            print(f"El código del tratamiento ha sido generado exitosamente. El código es:{max(codTrats)}")
            tratamiento = {
                "Identificacion Solicitada":solCodPac,
                "Descripcion":descTrat,
                "Fecha de inicio":dateIni,
                "Fecha de finalizacion":dateFin,
                "Codigo del medico":codMedTrat,
                "Codigo de Tratamiento":max(codTrats)
            }
            tratamientos.append(tratamiento)
            print("Tratamiento registrado con éxito!")
    if not found: 
        print("No existe ningún paciente con ese código.")
        return
    fileTrat = open("Tratamientos.txt", "a")
    fileTrat.write(f"{tratamiento}\n")
    fileTrat.close()
    
    
# funciones de reportes
def repCon():
    print("A continuación se mostrará información detallada sobre las consultas realizadas.")
    if os.path.exists("Consultas.txt"):
        file = open("Consultas.txt", "r")
        datos = file.read()
        print(datos)
        file.close()
    else: 
        print("No hay consultas en este momento.")
    
    
def repTrat():
    print("A continuación se mostrará información detallada sobre los tratamientos realizados.")
    if os.path.exists("Tratamientos.txt"):
        file = open("Tratamientos.txt", "r")
        datos = file.read()
        print(datos)
        file.close()
    else: 
        print("No hay tratamientos en este momento.")
   
       
def repMed():
    print("A continuación se mostrará información sobre los médicos de la clínica.")
    if os.path.exists("Medicos.txt"):
        file = open("Medicos.txt", "r")
        datos = file.read()
        print(datos)
        file.close()
    else: 
        print("No hay médicos en este momento.")    
   
    
def repPac():
    print("A continuación se mostrará información sobre los pacientes de la clínica.")
    if os.path.exists("Pacientes.txt"):
        file = open("Pacientes.txt", "r")
        datos = file.read()
        print(datos)
        file.close()
    else: 
        print("No hay pacientes en este momento.")    
     
     
#########################################################################################################################

opcion = 0 # Menu de clinica
opmod1 = 0 # opciones dentro del modulo 1 - agregar pacientes / buscar pacientes / editar paciente
opmod2 = 0 # opciones dentro del modulo 2 - agregar médicos / buscar médicos / editar medico
opmod5 = 0 # opciones dentro del modulo 5 - reporte consultas / tratamientos / medicos / pacientes
print("""  /$$$$$$  /$$ /$$           /$$                           /$$    /$$ /$$   /$$               /$$ /$$   /$$              
 /$$__  $$| $$|__/          |__/                          | $$   | $$|__/  | $$              | $$|__/  | $$              
| $$  \__/| $$ /$$ /$$$$$$$  /$$  /$$$$$$$  /$$$$$$       | $$   | $$ /$$ /$$$$$$    /$$$$$$ | $$ /$$ /$$$$$$   /$$   /$$
| $$      | $$| $$| $$__  $$| $$ /$$_____/ |____  $$      |  $$ / $$/| $$|_  $$_/   |____  $$| $$| $$|_  $$_/  | $$  | $$
| $$      | $$| $$| $$  \ $$| $$| $$        /$$$$$$$       \  $$ $$/ | $$  | $$      /$$$$$$$| $$| $$  | $$    | $$  | $$
| $$    $$| $$| $$| $$  | $$| $$| $$       /$$__  $$        \  $$$/  | $$  | $$ /$$ /$$__  $$| $$| $$  | $$ /$$| $$  | $$
|  $$$$$$/| $$| $$| $$  | $$| $$|  $$$$$$$|  $$$$$$$         \  $/   | $$  |  $$$$/|  $$$$$$$| $$| $$  |  $$$$/|  $$$$$$$
 \______/ |__/|__/|__/  |__/|__/ \_______/ \_______/          \_/    |__/   \___/   \_______/|__/|__/   \___/   \____  $$
                                                                                                                /$$  | $$
        Hecho por: Lesly Otavalo, Juan Oviedo, Jin Lin, Hernan Lu                                              |  $$$$$$/
                                                                                                                \______/ """)
while True:
    print()
    print("\t\t\t\t\t//////////////////////////////////////////")
    print("\t\t\t\t\t//\t\t\t\t\t//")
    print("\t\t\t\t\t//\t[1] Módulo de Pacientes\t\t//") 
    print("\t\t\t\t\t//\t[2] Módulo de Médico\t\t//")
    print("\t\t\t\t\t//\t[3] Módulo de Consultas\t\t//")
    print("\t\t\t\t\t//\t[4] Módulo de Tratamientos\t//")
    print("\t\t\t\t\t//\t[5] Módulo de Reportes\t\t//")
    print("\t\t\t\t\t//\t[6] ===== Salir =====\t\t//")
    print("\t\t\t\t\t//\t\t\t\t\t//")
    print("\t\t\t\t\t//////////////////////////////////////////")
    print()
    opcion = int(input("Digite una opción: "))
    print()
    if opcion == 1: # Modulo de pacientes
        print("\t\t\t\t   Bienvenido estimado usuario al módulo de pacientes.")
        print()
        while True: 
            print("\t\t\t\t\t//////////////////////////////////////////")
            print("\t\t\t\t\t//\t\t\t\t\t//")
            print("\t\t\t\t\t//\t[1] Agregar pacientes\t\t//")
            print("\t\t\t\t\t//\t[2] Buscar pacientes\t\t//")
            print("\t\t\t\t\t//\t[3] Editar paciente\t\t//")
            print("\t\t\t\t\t//\t[4] ==== Salir ====\t\t//")
            print("\t\t\t\t\t//\t\t\t\t\t//")
            print("\t\t\t\t\t//////////////////////////////////////////")
            print()
            opmod1 = int(input("Ingrese el número de la opción: "))
            if opmod1 == 1:
                canPac = int(input("Ingrese la cantidad de pacientes que desea registrar: "))
                aggPac(canPac)
            elif opmod1 == 2:
                buscarPac()
            elif opmod1 ==3:
                editPac()     
            elif opmod1 == 4:
                print("Hasta pronto")
            else:
                print("Por favor, digite una opción válida.")
                print()
            break
    elif opcion == 2: # Módulo de médicos
        print("\t\t\t\t   Bienvenido estimado usuario al módulo de médicos.")
        print()
        while True: 
            print("\t\t\t\t\t//////////////////////////////////////////")
            print("\t\t\t\t\t//\t\t\t\t\t//")
            print("\t\t\t\t\t//\t[1] Registrar médico\t\t//")
            print("\t\t\t\t\t//\t[2] Buscar médico\t\t//")
            print("\t\t\t\t\t//\t[3] Editar médico\t\t//")
            print("\t\t\t\t\t//\t[4] ==== Salir ====\t\t//")
            print("\t\t\t\t\t//\t\t\t\t\t//")
            print("\t\t\t\t\t//////////////////////////////////////////")
            print()
            opmod2 = int(input("Ingrese el número de la opción: "))
            if opmod2 == 1:
                canMed = int(input("Ingrese la cantidad de médicos que desea registrar: "))
                aggMed(canMed)   
            elif opmod2 == 2:
                buscarMed()
            elif opmod2 == 3:
                editMed()
            elif opmod2 == 4:
                print("Hasta pronto")     
            else:
                print("Por favor, digite una opción válida.")
                print()
            break
    elif opcion == 3: # Módulo de consultas
        regCon()
        print()
    elif opcion == 4: # Módulo de tratamientos
        regTrat()
        print()  
    elif opcion == 5: # Módulo de reportes
        print("\t\t\t\t   Bienvenido estimado usuario al módulo de reportes.")
        print()
        while True: 
            print("\t\t\t\t\t//////////////////////////////////////////")
            print("\t\t\t\t\t//\t\t\t\t\t//")
            print("\t\t\t\t\t//\t[1] Reporte de Consultas\t//")
            print("\t\t\t\t\t//\t[2] Reporte de Tratamientos\t//")
            print("\t\t\t\t\t//\t[3] Reporte de Médicos\t\t//")
            print("\t\t\t\t\t//\t[4] Reporte de Pacientes\t//")
            print("\t\t\t\t\t//\t[5] ===== Salir =====\t\t//")
            print("\t\t\t\t\t//\t\t\t\t\t//")
            print("\t\t\t\t\t//////////////////////////////////////////")
            print()
            opmod5 = int(input("Ingrese el número de la opción: "))
            if opmod5 == 1:
                repCon()
            elif opmod5 == 2:
                repTrat()
            elif opmod5 ==3:
                repMed()
            elif opmod5 == 4:
                repPac()
            elif opmod5 == 5:
                print("Hasta pronto")
            else:
                print("Por favor, digite una opción válida.")
                print()
            break
    elif opcion == 6: # Salir
        print("Hasta pronto")
        break
    else:
        print("Por favor, digite una opción válida.")
        print()