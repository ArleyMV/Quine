# import json
# from datos import *

# def obtener_numero_usuario(mensaje):
#     while True:
#         numero = input(mensaje)
#         if len(numero) == 10 and numero.isdigit():
#             return int(numero)
#         else:
#             print("El número debe tener exactamente 10 dígitos y solo contener números.")
# # enviar dinero
# def enviar_dinero():
#     numero_origen = obtener_numero_usuario("Ingrese el número del usuario de origen: ")
#     numero_destino = obtener_numero_usuario("Ingrese el número del usuario de destino: ")
#     monto = float(input("Ingrese el monto a transferir: "))

#     datos = cargar_datos()
    
#     usuario_origen = None
#     usuario_destino = None
    
#     # Verificar usuarios
#     for i in datos:
#         for usuario in datos[i]:
#             if usuario["numtelefono"] == numero_origen:
#                 usuario_origen = usuario
#             if usuario["numtelefono"] == numero_destino:
#                 usuario_destino = usuario
    
#     # Verificar que ambos usuarios existan y que el saldo sea suficiente
#     if not usuario_origen or not usuario_destino:
#         return "Uno o ambos usuarios no existen."
#     if usuario_origen["saldo"] < monto:
#         return "Saldo insuficiente en la cuenta de origen."
    
#     # Realizar la transacción
#     usuario_destino["saldo"] += monto
#     usuario_origen["saldo"] -= monto
    
#     # Registrar la transacción
#     usuario_origen["transacciones"].append({
#         "destino": numero_destino,
#         "valor": -monto  # Registrar la salida de dinero
#     })
#     usuario_destino["transacciones"].append({
#         "destino": numero_origen,
#         "valor": monto  # Registrar la entrada de dinero
#     })
    
#     # Guardar los datos actualizados
#     guardar_datos(datos)
    
#     return "Transacción realizada con éxito."
