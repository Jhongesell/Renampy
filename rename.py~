# script que modifica el nombre de todos los archivos, anteponiendo el cero en
# nuestras imágenes
# Renampy V 1.0
import os
for nameinit in os.listdir("."):
    if nameinit[-4:]==".png":
        nombre=nameinit[0:-4:]
        newname=""
        newname='0'+nombre+'.png'
        os.rename(nameinit,newname)
