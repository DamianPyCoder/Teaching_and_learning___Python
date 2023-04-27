def reverse(s):
    r = ''
    #for i in range(len(s)):
    #    r += s[len(s) - 1 - i ]
    for i in reversed(range(len(s))):
        r += s[i]
    return r
    #return s[::-1]

def isPalindrom(text):
    text = text.lower()
    text = text.replace(' ', '')

    if text == reverse(text):
        return True
    else:
        return False

frase = input("Introduce una frase: ")
if isPalindrom(frase):
    print("Es palindromo.")
else:
    print("No es palindromo.")