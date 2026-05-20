print("1 - sacar")
print("2 - depositar")
print("3 - calcular_rend")

dinheiro = Conta(100)

escolha = int(input('o que deseja fazer?'))
if escolha == 1:
  dinheiro.sacar(50)
elif escolha == 2:
  dinheiro.depositar(20)
elif escolha == 3:
  dinheiro.calcular_rend()
  
  
  




