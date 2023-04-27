num = int(input("Introduce un numero: "))

an1 = 0
an2 = 1
n = 1

while n < num + 1:

    an = an1 + an2
    print("n = " + str(n) + ", an = " + str(an))

    an2 = an1
    an1 = an
    n += 1
