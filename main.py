from datos import *
from funcrionsGeneral import *
from functionsA import *
from functionsM import *
from functionsJ import *
from functionsI import *
from menu import *

BASE_DATOS_USERS = "users.json"
datosu = cargar_datos(BASE_DATOS_USERS)


while True:
    menu_principal()
    opc = pedir_opc()

    if opc == 1:
        registro(datosu)
        guardar_datos(datosu, BASE_DATOS_USERS)

    elif opc == 2:
        numtel = (input("Ingrese su número telefónico para ingresar "))
        contra = (input("Ingrese su contraseña"))
        for i in datosu["usuario"]:
            if i["numtelefono"] == numtel  and i["contrasena"] == contra:
                    
                while True:    
                    menu_usuario()
                    opc = pedir_opc()
                    if opc == 1:
                        men_retirar(datosu, numtel)
                    elif opc == 2:
                        print(enviar_dinero(numtel))
                    elif opc == 3:
                        men_recargar(datosu,numtel)
                    
                    # PERFIN USUARIO
                    elif opc == 4:
                        while True:
                            menu_perfil()
                            opc = pedir_opc()
                            if opc == 1:
                                actualizar_datos(datosu, numtel)
                            elif opc == 2:
                                print_movimientos(datosu, numtel)
                            elif opc == 3:
                                delete_cuenta(datosu, numtel)
                            elif opc == 0:
                                print("--> Volviendo al menú de usuario...")
                                break
                    elif opc == 0:
                        print("--> Volviendo al menú de inicio...")
                        break

# INICIO////////////////////////////////////////////////////
    elif opc == 0:
        print("Cerrando QUINE...")
        break

