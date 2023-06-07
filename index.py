#index
lista = [1,2,3,4,3]
#indice = lista.index(3)
#print(indice)
num=int(input("Digite o numero: "))
if num in lista:
  print(f"Primeira ocorrencia do valor {num}: {lista.index(num)}")
else:
  print(f"valor não encontrado: {num}")
