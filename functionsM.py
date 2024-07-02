# import random
# from datos import * 
# opc = int
# monto = int
# usuario_origen = None
                            
# def generar_codigo():
#     numeros = []
#     for _ in range(6):  
#         numeros.append(random.randint(0, 9))
#     numeros_como_texto = [str(numero) for numero in numeros]
#     codigo = ''.join(numeros_como_texto)
#     return codigo

# def men_retirar (datos):  
#     numero_origen = int(input("Ingrese su numero telefonico: "))
#     for i in datos:
#         for usuario in datos[i]:
#             if usuario["numtelefono"] == numero_origen:
#                 usuario_origen = usuario
#                 print("¿Donde desea Retirar?")
#                 print("1. Cajero")
#                 print("2. Punto fisico")
#                 print("0. Volver")
#                 while True:
#                     opc = str(input("digite su opcion : "))
#                     if opc == "1":
#                         monto = int(input("¿Cuanto desea retirar?"))
#                         codigo_aleatorio = generar_codigo()
#                         if usuario_origen["saldo"] > monto:
#                             print("Tu codigo Para retiro en cajero expira en 30 minutos")
#                             print(codigo_aleatorio)
#                             usuario_origen["saldo"]-=monto
#                             usuario_origen["transacciones"].append({
#                             "destino": "Retiro desde cajero",
#                             "valor": -monto})    
#                             guardar_datos(datos)
#                             break
#                         elif usuario_origen["saldo"] < monto:
#                             print("Saldo insuficiente")
#                     elif opc == "2":
#                         monto = int(input("¿Cuanto desea retirar?"))
#                         codigo_aleatorio = generar_codigo()
#                         if usuario_origen["saldo"] > monto:
#                             print("Tu codigo Para retiro en punto fisico expira en 30 minutos")
#                             print("Por favor Entrega este codigo a la persona encarga del punto fisico")
#                             print(codigo_aleatorio)
#                             usuario_origen["saldo"]-=monto
#                             usuario_origen["transacciones"].append({
#                             "destino": "Retiro desde punto fisico",
#                             "valor": -monto})    
#                             guardar_datos(datos)
#                             break
#                         elif usuario_origen["saldo"] < monto:
#                             print("Saldo insuficiente")
#                             break
#                     elif opc == "0":
#                         print("Volviendo")
#                         break
                    
#                     elif opc != int:
#                         print("digito un numero invalido")
#                         print("ERROR")
#                         print("digite un numero valido")
                        
# def men_recargar(datos):
#     numero_origen = int(input("Ingrese su numero telefonico: "))
#     for i in datos:
#         for usuario in datos[i]:
#             if usuario["numtelefono"] == numero_origen:
#                 usuario_origen = usuario
#                 print("¿Donde desea Recargar?")
#                 print("1. Banco electronico")
#                 print("2. Punto fisico")
#                 print("0. Volver")
#                 while True:
#                     opc = str(input("digite su opcion : "))
#                     if opc == "1":
#                         monto = int(input("¿Cuanto desea recargar?"))
#                         codigo_aleatorio = generar_codigo()
#                         print("Ingresa a tu banco electronico")
#                         print("Escribe el codigo en pagar")
#                         print(codigo_aleatorio)
#                         pagar = input("Digite: ")
#                         if pagar == codigo_aleatorio:
#                             usuario_origen["saldo"]+=monto
#                             usuario_origen["transacciones"].append({
#                             "destino": "Recarga desde Banco electronico",
#                             "valor": +monto})    
#                             print("RECARGA REALIZADA")
                            
#                             guardar_datos(datos)
#                         elif pagar != codigo_aleatorio:
#                             print("ERROR")
#                             print("DIGITO MAL EL CODIGO")
#                             break
#                     elif opc == "2":
#                         monto = int(input("¿Cuanto desea recargar?"))
#                         codigo_aleatorio = generar_codigo()
#                         print("Tu codigo Para retiro en punto fisico expira en 30 minutos")
#                         print("Por favor Entrega este codigo a la persona encarga del punto fisico")
#                         print(codigo_aleatorio)
#                         pagar = input("Digite: ")
#                         if pagar == codigo_aleatorio:
#                             usuario_origen["saldo"]+=monto
#                             usuario_origen["transacciones"].append({
#                             "destino": "Recarga desde punto fisico",
#                             "valor": +monto})    
#                             guardar_datos(datos)
#                             print("RECARGA REALIZADA")
#                         elif pagar != codigo_aleatorio:
#                             print("ERROR")
#                             print("DIGITO MAL EL CODIGO")
#                             break
#                     elif opc == "0":
#                         print("Volviendo")
#                         break
                        
#                     elif opc != int:
#                             print("digito una opcion invalida")
#                             print("ERROR")
#                             print("digite una opcion valida")
            
