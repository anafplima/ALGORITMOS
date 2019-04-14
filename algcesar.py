import string

modo = input("Digite E para encriptar ou D para descriptar: ")

chave = int(input("Digite o valor da chave: "))

mensagem = input("Digite a mensagem: ")

caracteres = "ABCDEFGHIJKLMNOPQRSTUVXWYZ"

convertido = ""

mensagem = mensagem.upper()
modo = modo.upper()

for caractere in mensagem:
	if caractere in caracteres:
		num = caracteres.find(caractere)
		if modo == 'E':
			num = (num+chave) % 26 
		elif modo == 'D':
			num = (num-chave) % 26
	
	convertido = convertido + caracteres[num]


if modo == 'E':
	print("O texto encriptado é ", convertido)
if modo == 'D':
	print("O texto descriptado é ", convertido)
