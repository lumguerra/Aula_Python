mes=["Janeiro", "Marco", "Maio", "Julho", "Setembro","Novembro"]
print (mes)
add=input("Digite um mes para ser adicionado: ")
if add not in mes:
  print(f"Valor adicionado: {add}")
  mes.append(add)
else:
  print(f"Valor ja esta na lista")
