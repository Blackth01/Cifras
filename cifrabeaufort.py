#coding: utf-8
#alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÓÚÃÂÊÔ" #Variável com letras do alfabeto
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
escolha = input("Digite C para cifrar ou D para decifrar: ")
chave = input("Digite a chave: ")
if (escolha == "C" or escolha == "c"):
    mensagem = input("Digite a mensagem a ser cifrada: ")
else:
    mensagem = input("Digite a mensagem a ser decifrada: ")

modificada = "" #Variável que representa a mensagem a ser modificada

mensagem = mensagem.upper() #Capitaliza mensagem
chave = chave.upper() #Capitaliza chave

ctrmsg = 0 #Posição do caractere atual da mensagem
ctrcv = 0 #Posição do caractere atual da chave

'''
O algoritmo abaixo é utilizado para cifrar
ou decifrar a mensagem
'''
while (ctrmsg < len(mensagem)): #Enquanto ainda não forem usados todos os caracteres da msg
    posictrmg = alfabeto.find(mensagem[ctrmsg]) #Retorna a posição do caractere atual da msg no alfabeto
    posictrcv = alfabeto.find(chave[ctrcv]) #Retorna a posição do caractere atual da chave no alfabeto
    if (escolha == "C" or escolha == "c"): #Verifica se a escolha foi cifrar ou decifrar

        '''Cifrando mensagem...
        ctrcif = posição do caractere cifrado no alfabeto'''

        '''O If abaixo verifica se a posição do caractere da chave é maior ou
        igual ao do caractere da msg e então aplica as fórmulas
        para extrair a posição do caractere a ser utilizado'''

        if (posictrcv >= posictrmg):
            ctrcif = posictrcv - posictrmg
        else:
            ctrcif = len(alfabeto) - (posictrmg - posictrcv) #35=número de letras na variável alfabeto
    else:
        '''Decifrando mensagem...
        ctrcif = posição do caractere decifrado no alfabeto'''

        '''O If abaixo verifica se a posição do
        caractere da mensagem é maior que a do
        caractere da chave e então aplica as fórmulas para
        extrair a posição do caractere a ser
        utilizado'''
        if (posictrmg > posictrcv):
            ctrcif = (posictrmg - len(alfabeto) - posictrcv)*-1 #35=número de letras na variável alfabeto
        else:
            ctrcif = posictrcv - posictrmg
    if (posictrcv < 0): #Verifica se posição do caractere da chave é inválida
        print ("Sua chave possui caracteres inválidos, tente com outra chave")
        ctrmsg = len(mensagem)+1 #Termina o while
        modificada = "DIGITE A PORRA DE UMA CHAVE COM APENAS CARACTERES SIMPLES!!"
    else: #Se não for inválida...
        if (posictrmg < 0): #Verifica se a posição do caractere da msg é válida
            modificada += mensagem[ctrmsg] #Incrementa a msg modificada com o próprio caractere utilizado
            ctrmsg += 1
        else: #Se for...
            modificada += alfabeto[ctrcif] #Incrementa a msg modificada com o caractere do alfabeto retornado da fórmula
            ctrmsg += 1
            ctrcv += 1
    if (ctrcv == len(chave)):
        '''Coloca a posição do caractere da chave para zero
        caso tenham sido usados todos os caracteres da chave'''
        ctrcv = 0
if (escolha == "C" or escolha == "c"):
    print ("A mensagem cifrada é %s" % modificada)
else:
    print ("A mensagem decifrada é %s" % modificada)
