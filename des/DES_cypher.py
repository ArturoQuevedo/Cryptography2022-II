import base64
import os
from matplotlib import pyplot as plt
import pyDes
import io
import os
import PIL.Image as Image

#lectura
def readimage(path):
    count = os.stat(path).st_size/2
    with open(path,"rb") as f:
        return bytearray(f.read())

rta=int(input("Bienvenido\nSe necesita un archivo image.jpg\nCifrar 1\nDescifrar 2\n"))
if (rta==1):
    bytes = readimage("image.jpg")
    key=input("Ingrese la llave (8 caracteres):\n")    
    des = pyDes.des(key.encode(), pyDes.CBC,b"\0\0\0\0\0\0\0\0",pad=None,padmode=pyDes.PAD_PKCS5)

    #encriptar
    encrypted=des.encrypt(bytes)

    #encode base64
    encoded=base64.b64encode(encrypted)
        
    image=open("cyphered_image.txt","wb")
    image.write(encoded)
    image.close()
    print(f"El archivo cifrado se guardó en cyphered_image.txt")
else:    
    key=input("Ingrese la llave (8 caracteres):\n")
    
    with open ("cyphered_image.txt","r") as cyphered_file:
        base64_image=base64.b64decode(cyphered_file.read())
        
    bytes= bytearray(base64_image)
    
    des = pyDes.des(key.encode(), pyDes.CBC,b"\0\0\0\0\0\0\0\0",pad=None,padmode=pyDes.PAD_PKCS5)
    
    decrypted=des.decrypt(bytes) 
    
    image=open("decrypted_image.jpg","wb")
    image.write(decrypted)
    image.close()
    print(f"El archivo descifrado se guardó en decrypted_image.jpg")
    