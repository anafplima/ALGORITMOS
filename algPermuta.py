import string
import random 

modo = input("Digite E para encriptar ou D para descriptar: ")

numchave = int(input("Digite o número da chave: "))

mensagem = input("Digite a mensagem: ")

convertido = ""

modo = modo.upper()

#chave = list(range(1, numchave+1))
#random.shuffle(chave)
chave = [4,1,5,3,2]

mensagem = mensagem.upper().replace(" ","")

lista = [mensagem[i:i+numchave] for i in range(0, len(mensagem), numchave)]

if modo=='D':
	chaveD = []
	i = 1
	for num in chave:
		chaveD.insert((num-1), i)
		i += 1

	chave = chaveD

for palavra in lista:
	for num in chave:
		convertido = convertido + palavra[num-1]

if modo == 'E':
	print("O texto encriptado é "+ convertido)
if modo == 'D':
	print("O texto descriptado é "+ convertido)