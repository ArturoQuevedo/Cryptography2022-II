def getPlainText():
    
    plain_text_string=""
    file1 = open('plain_text.txt', 'r')
    Lines = file1.readlines()
    
    count = 0     
    # Strips the newline character
    for line in Lines:
        count += 1
        plain_text_string += "{}".format((line.strip()).replace(" ","").upper())
    
    new_plain_text=""
    count=0
    for character in plain_text_string:
        if(count<5):
            new_plain_text+=character
            if (count==4):
                new_plain_text+=" "
        
        else:
            new_plain_text+=character
            count=0
        
        count+=1
        
    return new_plain_text

def getEncryptedText():
    
    plain_text_string=""
    file1 = open('encrypted_text.txt', 'r')
    Lines = file1.readlines()
    
    count = 0     
    # Strips the newline character
    for line in Lines:
        count += 1
        plain_text_string += "{}".format((line.strip()).replace(" ","").upper())
    
    new_plain_text=""
    count=0
    for character in plain_text_string:
        if(count<5):
            new_plain_text+=character
            if (count==4):
                new_plain_text+=" "
        
        else:
            new_plain_text+=character
            count=0
        
        count+=1
        
    return new_plain_text

def decrypt(cypheredText):
    decrypted=""
    for character in cypheredText:
        if(character==" "):
            decrypted+=" "
        else:
            x=((ord(character)-3-65)%26)
            decrypted+=chr(x+65)
    return(decrypted)

def encrypt(cypheredText):
    decrypted=""
    for character in cypheredText:
        if(character==" "):
            decrypted+=" "
        else:
            x=((ord(character)+3-65)%26)
            decrypted+=chr(x+65)
    return(decrypted)

#---------Menu---------
def menu():
    while True:
        print("--------------CAESAR CYPHER--------------")
        print("--------------BIENVENIDO--------------")
        
        print("ESCRIBA SU TEXTO PLANO EN plain_text.txt")
        print("ESCRIBA SU TEXTO CIFRADO EN encrypted_text.txt\n")
        print("0 para encriptar")
        print("1 para desencriptar")
        print("2 para salir")
        
        opcion=input()
        continuar=None
        
        if(int(opcion)==0):
            
            plainText = getPlainText()            
            print("Su texto ENCRIPTADO es:")
            print(encrypt(plainText))
            print("\nPresione enter para continuar")
            continuar=input()        
            
        elif(int(opcion)==1):
            cypheredText = getEncryptedText()
                        
            print("Su texto DESENCRIPTADO es:")
            print(decrypt(cypheredText))
            
            print("\nPresione enter para continuar")
            continuar=input()
        elif(int(opcion)==2):
            break
        else:
            print("ERROR")
            
menu()