import pyaes
import base64

def encrypt(plaintext,key):
    if plaintext:
        aes=pyaes.AESModeOfOperationCTR(key)
        return(base64.b64encode(aes.encrypt(plaintext)))
    return None

def decrypt(encrypted,key):
    if encrypted:
        aes=pyaes.AESModeOfOperationCTR(key)
        return(aes.decrypt(base64.b64decode(encrypted)))
    return None

rta=int(input("Bienvenido\nSe necesita el archivo image.jpg\nCifrar 1\nDescifrar 2\n"))
if(rta==1):
    key=input("Ingrese la llave. El modo de operación depende de su longitud:\n16 caracteres ->128 bits\n24 caracteres -> 192\n32 caracteres -> 256\n")
    with open("image.jpg","rb") as file:
        mybytes=file.read()
        
    encrypted=encrypt(mybytes,bytes(key,'utf-8'))    
    encoded=base64.b64encode(encrypted)
    
    image=open("cyphered_image.txt","wb")
    image.write(encoded)
    image.close()
    print(f"El archivo cifrado se guardó en cyphered_image.txt")
        
elif(rta==2):
    key=input("Ingrese la llave. El modo de operación depende de su longitud:\n16 caracteres ->128 bits\n24 caracteres -> 192\n32 caracteres -> 256\n")
    
    with open("cyphered_image.txt","rb") as file:
        mybytes=file.read()
    
    decoded=base64.b64decode(mybytes)
    decrypted=decrypt(decoded,bytes(key,'utf-8'))
    
    image=open("decrypted_image.jpg","wb")
    image.write(decrypted)
    image.close()
    print(f"El archivo cifrado se guardó en decrypted_image.jpg")

