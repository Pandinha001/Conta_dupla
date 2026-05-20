class Conta:
  def __init__(self, saldo):
    self.saldo = saldo
  def sacar(self, valor):
    self.saldo -= valor
    print(f' seu saldo atual é: {self.saldo}')
  def depositar(self, valor):
    self.saldo += valor
    print(f' seu saldo atual é: {self.saldo}')
  def calcular_rend(self):
    rend = self.saldo * 0.1
    print(f"Seu rendimento foi: {rend}")

dinheiro = Conta(100)
dinheiro.sacar(50)
dinheiro.depositar(20)
dinheiro.calcular_rend()
