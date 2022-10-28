import numpy as np

def getKey():
    '''
    Recieves n: the size of the square matrix
    Returns the matrix from key.txt
    '''    
    with open('key.txt', 'r') as f:
        l = [[int(num) for num in line.split()] for line in f]
    return np.array(l)

def getText(x:int):
    '''
    Recieves x: which text file should be readed
        x==0 -> plain_text.txt
        x==1 -> cypher_text.txt
    Returns the string in the file
    '''
    filename=None
    if (x==0):
        filename='plain_text.txt'
    else:
        filename='cypher_text.txt'
    
    with open(filename, 'r') as file:
        text = file.read().rstrip().replace(' ','')
    return text

def rotateMatrix(x:int,matrix):
    '''
    Recieves x: the direction the matrix has to be rotated
        x==0 -> Rotate right
        x==1 -> Rotate left
    Returns: A numpy array (matrix); the new matrix
    '''
    if (x==0):
        return rotateMatrixRight(matrix)
    elif(x==1):
        return rotateMatrixLeft(matrix)
    
    return None

def rotateMatrixRight(matrix:np.ndarray):
    '''    
    '''    
    n=np.shape(matrix)[0]
    newMatrix=np.empty([n, n], dtype=int)    
    j=0
    
    for i in range(n-1,-1,-1):    
        newMatrix[:,i]=matrix[j]
        j+=1 
    
    return newMatrix

def rotateMatrixLeft(matrix:np.ndarray):
    '''    
    '''    
    n=np.shape(matrix)[0]
    newMatrix=np.empty([n, n], dtype=int)    
    j=0
    
    for i in range(n-1,-1,-1):    
        newMatrix[j]=matrix[:,i]
        j+=1 
    
    return newMatrix

def listToString(aList:list):
    string=''
    for _ in aList:
        string+=_
    return string

def listToStringWithSpaces(aList:list):
    string=''
    for _ in aList:
        string+=_
    return string

def encrypt(rotation:int):
    
    text=getText(0)
    keyMatrix=getKey()        
    n=keyMatrix.shape[0]
    key = keyMatrix.flatten()
    encrypted = key.copy().tolist()

    j=0
    for _ in range(n):
        for i in range(len(key)):
            if key[i]==1:
                encrypted[i]=text[j]
                #text.replace(text[j],'',1)
                j+=1
        keyMatrix=rotateMatrix(rotation,keyMatrix)
        key=keyMatrix.flatten()    
    
    return listToString(encrypted)

def decrypt(rotation:int):
    
    text=getText(1)
    keyMatrix=getKey()
    n=keyMatrix.shape[0]
    key = keyMatrix.flatten()
    decrypted = key.copy().tolist()

    j=0
    for _ in range(n):
        for i in range(len(key)):
            if key[i]==1:
                decrypted[j]=text[i]
                #text.replace(text[j],'',1)
                j+=1
        
        keyMatrix=rotateMatrix(rotation,keyMatrix)
        key=keyMatrix.flatten()
    
    return listToString(decrypted)


def menu():
    
    while True:    
        print("--------------TURNING GRILLE CYPHER--------------")
        print("--------------BIENVENIDO--------------")    
        print("ESCRIBA SU TEXTO PLANO EN plain_text.txt")
        print("ESCRIBA SU TEXTO CIFRADO EN encrypted_text.txt\n")
        print("0 para encriptar")
        print("1 para desencriptar")
        print("2 para salir")        
        
        opcion=input()
        continuar=None
        
        if(int(opcion)==0):
            
            print('Escriba  0 para cifrar hacia la derecha')
            print('Escriba  1 para cifrar hacia la izquierda')
            rotacion=int(input())
            if(rotacion==0 or rotacion==1):
                encrypted=encrypt(rotacion)
                print(f'Su texto encriptado es: {encrypted}')
            else:
                print('Entrada incorrecta')
                break
            
            print("\nPresione enter para continuar")
            continuar=input()
            
        elif(int(opcion)==1):
            
            print('Escriba  0 para descifrar hacia la derecha')
            print('Escriba  1 para descifrar hacia la izquierda')
            rotacion=int(input())
            
            if(rotacion==0 or rotacion==1):
                decrypted=decrypt(rotacion)
                print(f'Su texto desencriptado es: {decrypted}')
            else:
                print('Entrada incorrecta')
                break
            
            print("\nPresione enter para continuar")
            continuar=input()
            
        elif(int(opcion)==2):
            break
        else:
            print("ERROR")

menu()

#print(encrypt(1))
#print(decrypt(1))