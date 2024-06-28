def pedir_opc():
    opc = 0
    try:
        opc = int(input("Ingresa el número de la opción a elegir"))
        return opc
    except Exception:
        print("Valor inválido")
        return 0
    
