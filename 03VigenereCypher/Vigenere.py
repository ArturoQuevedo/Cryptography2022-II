def getText(filename):
    
    text=""
    file1 = open(filename, 'r')
    Lines = file1.readlines()
    
    count = 0     
    # Strips the newline character
    for line in Lines:
        count += 1
        text += "{}".format((line.strip()).replace(" ","").upper())
        
    return text

def splitInSegments(text,t):
    new_text=""
    count=0
    for character in text:
        if(count<t):
            new_text+=character
        
        else:
            new_text+=" "
            new_text+=character
            count=0
        
        count+=1
    
    return new_text


def encrypt(plaintext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in plaintext]
    ciphertext = ''
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
        ciphertext += chr(value + 65)
        
    return ciphertext


def decrypt(ciphertext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        plaintext += chr(value + 65)
    
    return plaintext

#---------Menu---------
def menu():
    while True:
        print("--------------VIGENERE CYPHER--------------")
        print("--------------BIENVENIDO--------------")
        
        print("ESCRIBA SU TEXTO PLANO EN plain_text.txt")
        print("ESCRIBA SU TEXTO CIFRADO EN encrypted_text.txt\n")
        print("0 para encriptar")
        print("1 para desencriptar")
        print("2 para salir")
        
        opcion=input()
        continuar=None
        key=None
        t=None
        
        if(int(opcion)==0):
            
            key = (input("Valor de KEY: ")).upper()
            t = int(input("Valor de t: "))
            
            plainText = getText("plain_text.txt")
            print("Su texto ENCRIPTADO es:")
            print(splitInSegments(encrypt(plainText,key),t))
            print("\nPresione enter para continuar")
            continuar=input()        
            
        elif(int(opcion)==1):
            
            key = (input("Valor de KEY: ")).upper()
            t = int(input("Valor de t: "))
            cypheredText = getText("encrypted_text.txt")
            
                        
            print("Su texto DESENCRIPTADO es:")
            print(splitInSegments(decrypt(cypheredText,key),t))
            
            print("\nPresione enter para continuar")
            continuar=input()
        elif(int(opcion)==2):
            break
        else:
            print("ERROR")
            

menu()