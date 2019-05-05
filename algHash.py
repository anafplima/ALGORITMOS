import collections
import string

maiusculas=collections.deque(string.ascii_uppercase)
minusculas=collections.deque(string.ascii_lowercase)

mensagem=(input("Digite a mensagem: "))
total=0
for i in range (len(mensagem)):

    total+=ord(mensagem[i])

print("\nHASH: "+str(total%100))