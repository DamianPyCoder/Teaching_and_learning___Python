def fibonacci(n):
    fib_sequence = [0,1]
    for i in range(2,n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

n = int(input("Ingrese el número de términos de la sucesión de Fibonacci: "))

fib_sequence = fibonacci(n)
print("La sucesión de fibonacci con ",n," términos es: ")
print(fib_sequence)