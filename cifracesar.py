#coding: utf-8
'''
PARA CIFRAS DE CESAR EM INGLÊS, DEVE-SE
REDUZIR OS CARACTERES PARA A-Z, SEM ACENTOS

'''
texto = input('Digite a mensagem a ser cifrada ou decifrada: ')


modo = input("C para cifrar ou D para decifrar: ")

CARACTERES = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÓÚÃÂÊÔ' #todas a letras a serem utilizadas
#CARACTERES = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
totcaracteres = len(CARACTERES) #recebe o total de caracteres

convertido = '' #variável que guardará o texto a ser modificado

texto = texto.upper() #capitaliza mensagem

if (modo == 'C' or modo == 'c'):
  chave = int(input("Digite a chave para cifrar: "))
  if (chave < totcaracteres): #verifica se a chave é maior que o total de caracteres
    for caractere in texto: #para cada caractere na mensagem...
      if caractere in CARACTERES: #se o caractere estiver no alfabeto utilizado
        num = CARACTERES.find(caractere) #recebe a posição do caractere no alfabeto
        novonum = num + chave #nova posição a ser utilizada
        if (novonum >= totcaracteres): #verifica se a nova posição é maior ou igual ao total de caracteres
            novonum = chave - (totcaracteres - num) #fórmula que retorna a posição do caractere cifrado
        convertido += CARACTERES[novonum] #incrementa o caractere cifrado na mensagem
      else:
          convertido += caractere #simplesmente incrementa a mensagem com o caractere normal
    print ("O texto cifrado é %s" % convertido)
  else:
      print ("Chave alta demais!")
else:
    '''
    Bruteforce para decifrar a mensagem

    Basicamente ele cifra a mensagem de todas as formas
    possíveis, sendo assim,  uma hora ele acabará
    replicando a mensagem original
    (utiliza o mesmo algoritmo anterior para cifrar)
    '''
    chave = 1
    possib = 1
    while (chave < totcaracteres):
      for caractere in texto:
        if (caractere in CARACTERES):
            num = CARACTERES.find(caractere)
            novonum = num + chave
            if (novonum >= totcaracteres):
                novonum = chave - (totcaracteres - num)
            convertido += CARACTERES[novonum]
        else:
            convertido += caractere
      print ("%dº possibilidade: %s" % (possib, convertido))
      possib += 1
      chave += 1
      convertido = ''
    print('\nCASO SAIBA A CHAVE, SUBTRAIA DO TOTAL DE LETRAS DO ALFABETO UTILIZADO \nO NÚMERO DA CHAVE, PARA ENCONTRAR A FRASE MAIS RAPIDAMENTE')
