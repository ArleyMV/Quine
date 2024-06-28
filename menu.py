def menu_principla():
    print("---Menu principal---")   
    print("1. Registrarse")
    print("2. Iniciar sesión")

def menu_usuario():
    print("---Menu Usuario---")
    print("1. Retirar dinero")
    print("2. Enviar dinero")
    print("3. Recargar saldo")
    print("4. Perfil de usuario")

def pedir_opc():
    opc = 0
    try:
        opc = int(input("Ingresa el número de la opción a elegir"))
        return opc
    except Exception:
        print("Valor inválido")
        return 0
    