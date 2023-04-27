def area_triangulo(base, altura):
    area = (base * altura)/2
    return area
    
def perimetro_triangulo(a, b, c):
    return a + b + c
    
base = float(input("Introduce la base del triangulo: "))
altura = float(input("Introduce la altura del triangulo: "))

area = triangulo.area_triangulo(base, altura)
print("El area del triangulo es = " + str(area))

lado1 = float(input("Introduce la longitud del primer lado del triangulo: "))
lado2 = float(input("Introduce la longitud del segundo lado del triangulo: "))
lado3 = float(input("Introduce la longitud del tercer lado del triangulo: "))

perimetro = triangulo.perimetro_triangulo(lado1, lado2, lado3)
print("El perimetro del triangulo es = " + str(perimetro))

