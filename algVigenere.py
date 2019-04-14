import string

modo = input("Digite E para encriptar ou D para descriptar: ")

chave = input("Digite a palavra chave: ")

mensagem = input("Digite a mensagem: ")

caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

convertido = ""

chave = chave.upper()
mensagem = mensagem.upper()
mensagem = mensagem.replace(" ","")
modo = modo.upper()

n = len(chave)
lista = [mensagem[i:i+n] for i in range(0, len(mensagem), n)]

for palavra in lista:
	i=0
	for caractere in palavra:
		numcara = caracteres.find(caractere)
		numchave = caracteres.find(chave[i])
		
		i += 1
		if modo == 'E':
			num = (numcara+numchave) % 26 
		elif modo == 'D':
			
			num = (numcara-numchave) % 26
	
		convertido = convertido + caracteres[num]

if modo == 'E':
	print("O texto encriptado é "+ convertido)
if modo == 'D':
	print("O texto descriptado é "+ convertido)