def isLeap(year):
    if (year % 400 == 0):
        return True
    else:
        if ((year % 4 == 0) and (year % 100 != 0)):
            return True
    return False
    
year = int(input("Introduce el año: "))

if isLeap(year):
    print("El año "+ str(year) + " es bisiesto")
else:
    print("El año "+ str(year) + " no es bisiesto")
