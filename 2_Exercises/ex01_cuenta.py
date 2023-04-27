class Compte():
    def __init__(self,titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def ingressar (self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad

    def retirar (self, cantidad):
        if cantidad > 0:
            self.saldo -= cantidad
            if self.saldo < 0:
                self.saldo = 0

titular = input("Titular del compte: ")
saldo_inicial = float(input("Saldo inicial: "))
compte1 = Compte(titular,saldo_inicial)

quantitat_ing = float(input("Quantitat a ingressar: "))
compte1.ingressar(quantitat_ing)
print("Saldo =", compte1.saldo)

quantitat_ret = float(input("Quantitat a retirar: "))
compte1.retirar(quantitat_ret)
print("Saldo =", compte1.saldo)
