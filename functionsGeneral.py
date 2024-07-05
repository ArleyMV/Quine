from json import *
from datos import *
from menu import pedir_opc
import random

BASE_DATOS_USERS = "users.json"
datosu = cargar_datos(BASE_DATOS_USERS)


def obtener_numero_usuario(mensaje):
     while True:
         numero = input(mensaje)
         if len(numero) == 10 and numero.isdigit():
             return int(numero)
         else:
             print("El número debe tener exactamente 10 dígitos y solo contener números.")
             
def enviar_dinero(numtel):
     numero_origen = numtel
     numero_destino = str(obtener_numero_usuario("Ingrese el número del usuario de destino: "))
     monto = float(input("Ingrese el monto a transferir: "))

    
     usuario_origen = None
     usuario_destino = None
    
     # Verificar usuarios
     for i in datosu:
         for usuario in datosu[i]:
             if usuario["numtelefono"] == numero_origen:
                 usuario_origen = usuario
             if usuario["numtelefono"] == numero_destino:
                 usuario_destino = usuario
    
     # Verificar que ambos usuarios existan y que el saldo sea suficiente
     if not usuario_origen or not usuario_destino:
         return "Uno o ambos usuarios no existen."
     if usuario_origen["saldo"] < monto:
         return "Saldo insuficiente en la cuenta de origen."
    
     # Realizar la transacción
     usuario_destino["saldo"] += monto
     usuario_origen["saldo"] -= monto
    
     # Registrar la transacción
     usuario_origen["transacciones"].append({
         "destino": numero_destino,
         "valor": -monto  # Registrar la salida de dinero
     })
     usuario_destino["transacciones"].append({
         "destino": numero_origen,
         "valor": monto  # Registrar la entrada de dinero
     })
    
     # Guardar los datos actualizados
     guardar_datos(datosu,BASE_DATOS_USERS)
    
     return "Transacción realizada con éxito."

def registro(datos):
    usuario = {}
    nombre = input("Ingrese su nombre: ")
    usuario["nombre"] = nombre 

    while True:
        documento = input("Ingrese el número de documento (9 o 10 dígitos): ")

        if len(documento) not in (9, 10) or not documento.isdigit():
            print("El número de documento debe tener 9 o 10 dígitos y ser numérico.")
        else:
            print("Número de documento válido.")
            usuario["documento"] = int(documento)
            break

    tel = ""
    while len(tel) != 10 or not tel.isdigit():
        tel = input("Ingrese un número de teléfono válido (10 dígitos): ")
    print("Número de teléfono válido.")
    usuario["numtelefono"] = tel  

    while True:
        contrasena = input("Ingrese una contraseña de 4 dígitos: ")

        if len(contrasena) != 4 or not contrasena.isdigit():
            print("La contraseña debe tener exactamente 4 dígitos y ser numérica.")
        else:
            print("Contraseña válida.")
            usuario["contrasena"] = contrasena
            break

    usuario["saldo"] = float(0)
    usuario["transacciones"] = [{"valor": 0, "destino": 0}]
    datos["usuario"].append(usuario)

opc = int
monto = int
usuario_origen = None

def generar_codigo():
    numeros = []
    for _ in range(6):  
        numeros.append(random.randint(0, 9))
    numeros_como_texto = [str(numero) for numero in numeros]
    codigo = ''.join(numeros_como_texto)
    return codigo

def men_retirar (datos,numtel):  
    numero_origen = numtel
    for i in datos:
        for usuario in datos[i]:
            if usuario["numtelefono"] == numero_origen:
                usuario_origen = usuario
                print("¿Donde desea Retirar?")
                print("1. Cajero")
                print("2. Punto fisico")
                print("0. Volver")
                while True:
                    opc = str(input("digite su opcion : "))
                    if opc == "1":
                        monto = int(input("¿Cuanto desea retirar?"))
                        codigo_aleatorio = generar_codigo()
                        if usuario_origen["saldo"] > monto:
                            print("Tu codigo Para retiro en cajero expira en 30 minutos")
                            print(codigo_aleatorio)
                            usuario_origen["saldo"]-=monto
                            usuario_origen["transacciones"].append({
                            "destino": "Retiro desde cajero",
                            "valor": -monto})    
                            guardar_datos(datos,BASE_DATOS_USERS)
                            break
                        elif usuario_origen["saldo"] < monto:
                            print("Saldo insuficiente")
                    elif opc == "2":
                        monto = int(input("¿Cuanto desea retirar?"))
                        codigo_aleatorio = generar_codigo()
                        if usuario_origen["saldo"] > monto:
                            print("Tu codigo Para retiro en punto fisico expira en 30 minutos")
                            print("Por favor Entrega este codigo a la persona encarga del punto fisico")
                            print(codigo_aleatorio)
                            usuario_origen["saldo"]-=monto
                            usuario_origen["transacciones"].append({
                            "destino": "Retiro desde punto fisico",
                            "valor": -monto})    
                            guardar_datos(datos,BASE_DATOS_USERS)
                            break
                        elif usuario_origen["saldo"] < monto:
                            print("Saldo insuficiente")
                            break
                    elif opc == "0":
                        print("Volviendo")
                        break
                    
                    elif opc != int:
                        print("digito un numero invalido")
                        print("ERROR")
                        print("digite un numero valido")
                        
def men_recargar(datos, numtel):
    numero_origen = numtel
    for i in datos:
        for usuario in datos[i]:
            if usuario["numtelefono"] == numero_origen:
                usuario_origen = usuario
                print("¿Donde desea Recargar?")
                print("1. Banco electronico")
                print("2. Punto fisico")
                print("0. Volver")
                while True:
                    opc = str(input("digite su opcion : "))
                    if opc == "1":
                        monto = int(input("¿Cuanto desea recargar?"))
                        codigo_aleatorio = generar_codigo()
                        print("Ingresa a tu banco electronico")
                        print("Escribe el codigo en pagar")
                        print(codigo_aleatorio)
                        pagar = input("Digite: ")
                        if pagar == codigo_aleatorio:
                            usuario_origen["saldo"]+=monto
                            usuario_origen["transacciones"].append({
                            "destino": "Recarga desde Banco electronico",
                            "valor": +monto})    
                            print("RECARGA REALIZADA")
                            
                            guardar_datos(datos,BASE_DATOS_USERS)
                        elif pagar != codigo_aleatorio:
                            print("ERROR")
                            print("DIGITO MAL EL CODIGO")
                            break
                    elif opc == "2":
                        monto = int(input("¿Cuanto desea recargar?"))
                        codigo_aleatorio = generar_codigo()
                        print("Tu codigo Para retiro en punto fisico expira en 30 minutos")
                        print("Por favor Entrega este codigo a la persona encarga del punto fisico")
                        print(codigo_aleatorio)
                        pagar = input("Digite: ")
                        if pagar == codigo_aleatorio:
                            usuario_origen["saldo"]+=monto
                            usuario_origen["transacciones"].append({
                            "destino": "Recarga desde punto fisico",
                            "valor": +monto})    
                            guardar_datos(datos,BASE_DATOS_USERS)
                            print("RECARGA REALIZADA")
                        elif pagar != codigo_aleatorio:
                            print("ERROR")
                            print("DIGITO MAL EL CODIGO")
                            break
                    elif opc == "0":
                        print("Volviendo")
                        break
                        
                    elif opc != int:
                            print("digito una opcion invalida")
                            print("ERROR")
                            print("digite una opcion valida")
            
def actualizar_datos(datos, numtel):
    while True:
        print("-----------Actualización de datos-----------")  
        print("Digita [1] para --> Actualizar tu nombre")
        print("Digita [2] para --> Actualizar tu número de telefono")
        print("Digita [3] para --> Actualizar tu contraseña")
        print("Digita [0] para --> Volver al menú del perfil")
        print("--------------------------------------")
        opc = pedir_opc()
        if opc == 1:
            for i in datos["usuario"]:
                if i["numtelefono"] == numtel:
                    i["nombre"] = input("Ingresa tu nuevo nombre")
                    guardar_datos(datos,BASE_DATOS_USERS)


        elif opc == 2:
            for i in datos["usuario"]:
                if i["numtelefono"] == numtel:
                    tel = ""
                    while len(tel) != 10 or not tel.isdigit():
                        tel = input("Ingrese un número de teléfono válido (10 dígitos): ")
                    print("Número de teléfono válido.")
                    i["numtelefono"] = tel

                    guardar_datos(datos,BASE_DATOS_USERS)

        elif opc == 3:
            for i in datos["usuario"]:
                if i["numtelefono"] == numtel:
                    while True:
                        contrasena = input("Ingrese una contraseña de 4 dígitos: ")

                        if len(contrasena) != 4 or not contrasena.isdigit():
                            print("La contraseña debe tener exactamente 4 dígitos y ser numérica.")
                        else:
                            print("Contraseña válida.")
                            i["contrasena"] = contrasena
                        guardar_datos(datos,BASE_DATOS_USERS)
        
        elif opc == 0:
            print("--> Volviendo al menú del perfil...")
            break

def print_movimientos(datos, numtel):
    for i in datos["usuario"]:
            if i["numtelefono"] == numtel:
                for u in i["transacciones"]:
                    print("--------------------------------------------------------------")
                    print(f"{u["destino"]}")
                    print(f"{u["valor"]}")
                    print("--------------------------------------------------------------")

def delete_cuenta(datos, numtel):
    for i in range(len(datos["usuario"])):
            if datos["usuario"][i]["numtelefono"] == numtel:
                print(i)
                datos["usuario"].pop(i) 
                guardar_datos(datos, BASE_DATOS_USERS)
