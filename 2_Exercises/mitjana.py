n1 = float(input("Primer numero: "))
n2 = float(input("Segon numero: "))
n3 = float(input("Tercer numero: "))

media = (n1 + n2 + n3) / 3

mayor = n1
if n2 > mayor:
     mayor = n2
if n3 > mayor:
    mayor = n3

menor = n1
if n2 < menor:
     menor = n2
if n3 < menor:
    menor = n3

print(f"media = {media}, mayor = {mayor}, menor = {menor}")
