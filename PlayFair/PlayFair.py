#---------Obtener la matriz (llave)---------
def getKey():
    key=[]
    key_file = open("key.txt", "r")
    for i in range(0,5):    
        line=key_file.readline()
        #print(line.strip()) 
        splitted_line=line.split()    
        #print(splitted_line)
        key.append(splitted_line)    
    key_file.close()
    return (key)

#---------Obtener el texto plano, todo en MAYUS y sin espacios---------
def getPlainText():
    
    plain_text_string=""
    file1 = open('plain_text.txt', 'r')
    Lines = file1.readlines()
    
    count = 0     
    # Strips the newline character
    for line in Lines:
        count += 1
        plain_text_string += "{}".format((line.strip()).replace(" ","").upper())
        
    return plain_text_string

#---------Obtener los pares del texto cifrado---------
def getCypheredPairs():
    
    cyphered_pairs=[]
    file1 = open('encrypted_text.txt', 'r')
    Lines = file1.readlines()
    
    pairs_in_line=None
    for line in Lines:
        line=line.strip()
        pairs_in_line=line.split()
        for pair in pairs_in_line:            
            cyphered_pairs.append(pair)

    return cyphered_pairs


#---------Obtener el texto plano en pares---------
def getPairs(plainText):
    
    pairs=[]
    i=0
    while i<len(plainText):
        
        if(i!=len(plainText)-1):
            if ((plainText[i]=="I" and plainText[i+1]== "J") or 
                (plainText[i]=="J" and plainText[i+1]== "I")):
                pairs.append((plainText[i],"X"))
                i+=1
            
            elif (plainText[i]!=plainText[i+1]):
                pairs.append((plainText[i],plainText[i+1]))
                i+=2
            
            else:
                pairs.append((plainText[i],"X"))
                i+=1
        
        else:
            pairs.append((plainText[i],"X"))
            i+=1
    
    return pairs

#---------Generar diccionario con la psición en la matriz de cada letra---------
def generatePositionDictionary(key):
    
    dict={}
    for i in range(0,5):
        for j in range(0,5):
            if(key[i][j]=="IJ"):
                dict["I"]=(i,j)
                dict["J"]=(i,j)
            else:
                dict[key[i][j]]=(i,j)
    return dict

#---------Encriptar---------
def encrypt(dict, pairs,key):
    texto_cifrado=""
    
    for pair in pairs:
        
        #Si están en la misma fila
        if(dict[pair[0]][0] == dict[pair[1]][0]):
            #print("MISMA FILA")
            #print(f"Fila: {dict[pair[0]][0]}")

            #Coordenadas de las letras con las que se reemplazará                      
            x=dict[pair[0]][0]
            y1=(dict[pair[0]][1]+1)%5
            y2=(dict[pair[1]][1]+1)%5

            #Añadir el cifrado
            texto_cifrado+=key[x][y1]
            texto_cifrado+=key[x][y2]
            texto_cifrado+=" "
            
        #Si están en la misma columna
        elif(dict[pair[0]][1] == dict[pair[1]][1]):
            #print("MISMA COLUMNA")
            #print(f"Columna: {dict[pair[0]][1]}")
            
            #Coordenadas de las letras con las que se reemplazará
            y=dict[pair[0]][1]
            x1=(dict[pair[0]][0]+1)%5
            x2=(dict[pair[1]][0]+1)%5

            #Añadir el cifrado
            texto_cifrado+=key[x1][y]
            texto_cifrado+=key[x2][y]

            texto_cifrado+=" "

        #Si no están ni en la misma fila ni en la misma columna    
        else:

            #Coordenadas de las letras con las que se reemplazará:
            #La fila del primero y la columna del segundo            
            x1=(dict[pair[0]][0])
            y1=dict[pair[1]][1]
            
            #Coordenadas de las letras con las que se reemplazará:
            #La fila del primero y la columna del segundo
            x2=(dict[pair[1]][0])
            y2=dict[pair[0]][1]

            #Añadir el cifrado
            texto_cifrado+=key[x1][y1]
            texto_cifrado+=key[x2][y2]

            texto_cifrado+=" "

    #print(f"Texto cifrado: {texto_cifrado}")
    
    return texto_cifrado
    
#---------Desencriptar---------
def decrypt(dict, pairs,key):
    texto_descifrado=""
    
    #print(f"Pairs: {pairs}")
    for pair in pairs:
        
        #print(pair)
        #Si están en la misma fila
        if(dict[pair[0]][0] == dict[pair[1]][0]):
            #print("MISMA FILA")
            #print(f"Fila: {dict[pair[0]][0]}")

            #Coordenadas de las letras con las que se reemplazará                      
            x=dict[pair[0]][0]
            y1=(dict[pair[0]][1]-1)%5
            y2=(dict[pair[1]][1]-1)%5

            #Añadir el cifrado
            texto_descifrado+=key[x][y1]
            texto_descifrado+=key[x][y2]
            texto_descifrado+=" "
            
        #Si están en la misma columna
        elif(dict[pair[0]][1] == dict[pair[1]][1]):
            #print("MISMA COLUMNA")
            #print(f"Columna: {dict[pair[0]][1]}")
            
            #Coordenadas de las letras con las que se reemplazará
            y=dict[pair[0]][1]
            x1=(dict[pair[0]][0]-1)%5
            x2=(dict[pair[1]][0]-1)%5

            #Añadir el cifrado
            texto_descifrado+=key[x1][y]
            texto_descifrado+=key[x2][y]

            texto_descifrado+=" "

        #Si no están ni en la misma fila ni en la misma columna    
        else:

            #Coordenadas de las letras con las que se reemplazará:
            #La fila del primero y la columna del segundo            
            x1=(dict[pair[0]][0])
            y1=dict[pair[1]][1]
            
            #Coordenadas de las letras con las que se reemplazará:
            #La fila del primero y la columna del segundo
            x2=(dict[pair[1]][0])
            y2=dict[pair[0]][1]

            #Añadir el cifrado
            texto_descifrado+=key[x1][y1]
            texto_descifrado+=key[x2][y2]

            texto_descifrado+=" "

    #print(f"Texto cifrado: {texto_cifrado}")
    
    return texto_descifrado
   
#---------Menu---------
def menu():
    while True:
        print("--------------BIENVENIDO--------------")
        print("ESCRIBA SU KEY EN key.txt")
        print("ESCRIBA SU TEXTO PLANO EN plain_text.txt")
        print("ESCRIBA SU TEXTO CIFRADO EN encrypted_text.txt\n")
        print("0 para encriptar")
        print("1 para desencriptar")
        print("2 para salir")
        
        opcion=input()
        continuar=None
        
        if(int(opcion)==0):
            key=getKey()
            pairs=getPairs(getPlainText())
            positionDictionary=generatePositionDictionary(key)
            
            print("Su texto ENCRIPTADO es:")
            print(encrypt(positionDictionary,pairs,key))
            print("\nPresione enter para continuar")
            continuar=input()        
            
        elif(int(opcion)==1):
            key=getKey()
            cypheredPairs=getCypheredPairs()
            positionDictionary=generatePositionDictionary(key)
            
            print("Su texto DESENCRIPTADO es:")
            print(decrypt(positionDictionary,cypheredPairs,key))
            print("\nPresione enter para continuar")
            continuar=input()
        elif(int(opcion)==2):
            break
        else:
            print("ERROR")


menu()