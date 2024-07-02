# from json import *

# def registro(datos):
#     usuario = {}
#     nombre = input("Ingrese su nombre: ")
#     usuario["nombre"] = nombre 

#     while True:
#         documento = input("Ingrese el número de documento (9 o 10 dígitos): ")

#         if len(documento) not in (9, 10) or not documento.isdigit():
#             print("El número de documento debe tener 9 o 10 dígitos y ser numérico.")
#         else:
#             print("Número de documento válido.")
#             usuario["documento"] = int(documento)
#             break

#     tel = ""
#     while len(tel) != 10 or not tel.isdigit():
#         tel = input("Ingrese un número de teléfono válido (10 dígitos): ")
#     print("Número de teléfono válido.")
#     usuario["numtelefono"] = tel  

#     while True:
#         contrasena = input("Ingrese una contraseña de 4 dígitos: ")

#         if len(contrasena) != 4 or not contrasena.isdigit():
#             print("La contraseña debe tener exactamente 4 dígitos y ser numérica.")
#         else:
#             print("Contraseña válida.")
#             usuario["contrasena"] = contrasena
#             break

#     usuario["saldo"] = float(0)
#     print(usuario)
#     datos["usuario"].append(usuario)