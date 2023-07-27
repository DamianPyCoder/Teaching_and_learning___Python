# comprueba el tipo de dato, ejercicio para practicar 

def obtener_tipo_dato(valor):
    if valor.isdigit():
        return "int"
    try:
        float_valor = float(valor)
        if float_valor.is_integer():
            return "int"
        else:
            return "float"
    except ValueError:
        if valor.lower() in ('true', 'false'):
            return "bool"
        if len(valor) == 1:
            return "char"
        try:
            list_valor = eval(valor)
            if isinstance(list_valor, list):
                return "list"
        except:
            pass
        if valor.startswith("[") and valor.endswith("]"):
            return "array"
        if valor.lower().startswith("arraylist[") and valor.endswith("]"):
            return "arraylist"
        return "str"

def main():
    entrada = input("Ingresa un valor: ")
    tipo_dato = obtener_tipo_dato(entrada)
    print(f"El valor '{entrada}' corresponde al tipo de dato: {tipo_dato}")

if __name__ == "__main__":
    main()
