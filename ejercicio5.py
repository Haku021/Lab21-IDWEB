tipo=input("Tipo de archivo (1=texto, 2=binario): ")
archivo_origen=input("Archivo origen: ")
archivo_destino=input("Archivo destino: ")
if tipo=="1":
    with open(archivo_origen,'r') as origen:
        contenido=origen.read()
    with open(archivo_destino,'w') as destino:
        destino.write(contenido)
    print("Archivo de texto copiado")
else:
    with open(archivo_origen,'rb') as origen:
        contenido=origen.read()
    with open(archivo_destino,'wb') as destino:
        destino.write(contenido)
    print("Archivo binario copiado")
    