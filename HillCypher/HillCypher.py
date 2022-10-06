from tokenize import String
from matplotlib.pyplot import get
import numpy as np
import math

def getKey():
    '''
    Devuelve la matriz llave en "key.txt" como un arreglo de Numpy
    '''    
    key=[]
    key_file = open("key.txt", "r")
    for i in range(0,2):    
        line=key_file.readline()
        #print(line.strip()) 
        splitted_line=line.split()    
        #print(splitted_line)
        key.append(splitted_line)      

    key_file.close()
    
    integers_key=[]

    for row in key:
        integer_row = [int(x) for x in row]
        integers_key.append(integer_row)
    
    return (np.array(integers_key))

def eea(a:int,b:int):
    '''
    Returns d,w,y
    '''
    if(b==0):
        return (a,1,0)
    q=math.floor(a/b)
    (dp,xp,yp)=eea(b,a%b)
    (d,x,y)=(dp,yp,xp-q*yp)
    return(d,x,y)

def getInverse(key:np.array):
    '''
    Returns: True si la matriz key es invertible
            False si la matriz key no es invertible
    '''
    det=key[0][0]*key[1][1]-key[0][1]*key[1][0]
    adjA=np.array([[key[1][1],(-1)*key[0][1]],[(-1)*key[1][0],key[1][1]]])
    
    if(det!=0):
        euclides=eea(det,26)
        if(euclides[0]==1):
            
            adjA=np.array([[key[1][1],(-1)*key[0][1]],[(-1)*key[1][0],key[0][0]]])
            
            inv_A=adjA.copy()
            inv_A[0][0]=(euclides[1]*adjA[0][0]) % 26
            inv_A[0][1]=(euclides[1]*adjA[0][1]) % 26
            inv_A[1][0]=(euclides[1]*adjA[1][0]) % 26
            inv_A[1][1]=(euclides[1]*adjA[1][1]) % 26
            
            return inv_A
    return None

def getText(x:int):
    '''
    If x==0 returns the plain text from plain_text.txt in one string, in upperclass
    if x==1 returns the cyphered text from encrypted_text.txt in one string, in upperclass
    '''
    text_string=""
    if x==0:        
        file1 = open('plain_text.txt', 'r')
    else:
        file1 = open('encrypted_text.txt', 'r')
    Lines = file1.readlines()
    
    count = 0     
    # Strips the newline character
    for line in Lines:
        count += 1
        text_string += "{}".format((line.strip()).replace(" ","").upper())
        
    return text_string

def getNumPairs(text_string:String):
    '''
    From one string, returns its content in a list of pairs of ints
    Ej: ABCD -> [[0,1],[2,3]]
    '''
    #Partir en string en pares
    if(len(text_string)%2!=0):
        text_string+='X'

    listOfPairs=[]
    currentPair=[]

    for i in range(len(text_string)):
        if (i%2==0):
            if(len(currentPair)!=0):
                listOfPairs.append(currentPair)
            currentPair=[]
            currentPair.append((ord(text_string[i])-65)%26)

        else:
            currentPair.append((ord(text_string[i])-65)%26)
            if(i==len(text_string)-1):
                listOfPairs.append(currentPair)        
    
    return listOfPairs

def modMultiplication(pairs:list,A):
    
    new_list=[]
    for pair in pairs:
        new_pair=[]
        new_pair=np.matmul(pair,A)
        pair_mod_26=[x%26 for x in new_pair]
        new_list.append(pair_mod_26)    
    
    return new_list

def getStringFromIntList(int_pairs:list):
    string=""
    for pair in int_pairs:
        for character in pair:
            string+=(chr(character+65))
    return string

#def getInverseMatrix(A):


def menu():
    
    while True:    
        print("--------------HILL CYPHER--------------")
        print("--------------BIENVENIDO--------------")    
        print("ESCRIBA SU TEXTO PLANO EN plain_text.txt")
        print("ESCRIBA SU TEXTO CIFRADO EN encrypted_text.txt\n")
        print("0 para encriptar")
        print("1 para desencriptar")
        print("2 para salir")        
        
        opcion=input()
        continuar=None
        A=getKey()
        invA=getInverse(A)
        
        if(int(opcion)==0):
            
            plainText = getText(0)
            print("Su texto ENCRIPTADO es:")
            toencrypt=getNumPairs(getText(0))
            precyphered=modMultiplication(toencrypt,A)
            new_string=getStringFromIntList(precyphered)
            print(new_string)
            print("\nPresione enter para continuar")
            continuar=input()        
            
        elif(int(opcion)==1):
            cypheredText = getText(1)
                        
            print("Su texto DESENCRIPTADO es:")
            toDecypher=getNumPairs(getText(1))
            predecyphered=modMultiplication(toDecypher,invA)
            new_string=getStringFromIntList(predecyphered)
            print(new_string)            
            print("\nPresione enter para continuar")
            continuar=input()
        elif(int(opcion)==2):
            break
        else:
            print("ERROR")

menu()