n1 = int(input("Primer numero: "))
n2 = int(input("Segundo numero: "))


if n1 < 100:
    d1 = 100 - n1
else:
    d1 = n1 - 100
#d1 = (100 - n1) if (n1 < 100) else (n1 - 100)

if n2 < 100:
    d2 = 100 - n2
else:
    d2 = n2 - 100

if d1 > d2:
    print(f"{n2} es mas cercano a 100 que {n1}")
else:
    print(f"{n1} es mas cercano a 100 que {n2}")
