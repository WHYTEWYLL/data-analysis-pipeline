from Cosas.tools import *
from Cosas.gdata import *
from Cosas.correo import *


parametros=getobjetives() 
print("Parametros guardados, se procede a la busqueda")
respuestapara(parametros.name,parametros.platform)
print("Inicio de la creación del pdf")
if pdfecito(parametros.name,parametros.platform):
    print("PDF creado, chequea tu carpeta OUTPUT")
    respuesta=input("Quieres enviarlo por correo?: (Y/N) ")
    if respuesta=="Y":
        if correo():
            print("Correo enviado!!!")
    else:
        pass
print("!Listo¡ NO DUDES EN VOLVER A USARME!! <3 ")




