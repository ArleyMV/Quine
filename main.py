from datos import *
from funcrionsGeneral import *
from functionsA import *
from functionsM import *
from functionsJ import *
from functionsI import *
from menu import *

BASE_DATOS_USERS = "users.json"
datosu = cargar_datos(BASE_DATOS_USERS)

run = True
while run == True:
    opc = pedir_opc()
    if opc == 1:
        
    elif opc == 0:
        run = False





guardar_datos(datosu, BASE_DATOS_USERS)
