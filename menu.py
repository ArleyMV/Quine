def menu_principal():
    print("---------Menú principal---------")   
    print("Digita [1] para --> Registrarse")
    print("Digita [2] para --> Iniciar sesión")
    print("Digita [0] para --> Cerrar QUINE")
    print("--------------------------------")

def menu_usuario():
    print("-----------Menú de Usuario-----------")  
    print("Digita [1] para --> Retirar dinero")
    print("Digita [2] para --> Enviar dinero")
    print("Digita [3] para --> Recargar tu saldo")
    print("Digita [4] para --> Ingresar al perfil de usuario")
    print("Digita [4] para --> Cerrar sesión")
    print("--------------------------------------")

def menu_perfil():
    print("---------------Mi Perfil---------------")
    print("Digita [1] para --> Actualizar Datos")
    print("Digita [2] para --> Ver movimientos")
    print("Digita [3] para --> Eliminar cuenta")
    print("Digita [0] para --> Volver al inicio")
    print("---------------------------------------")

def pedir_opc():
    opc = 0
    try:
        opc = int(input("-->Digita la opción a elegir: "))
        return opc
    except Exception:
        print("Valor inválido")
        return 0
    