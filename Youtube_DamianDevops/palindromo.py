def reverse(s):
    r = ''
    for i in reversed(range(len(s))):
        r += s[i]
    return r

def isPalindrom(text):
    text = text.lower()
    text = text.replace(' ','')

    if text == reverse(text):
        return True
    else:
        return False

frase = input("Introduce una frase: ")
if isPalindrom(frase):
    print("Es palíndromo")
else:
    print("NO es palíndromo")