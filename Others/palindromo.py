def palindromo(palabra):
    palabra=palabra.replace(' ','')
    palabra=palabra.lower()
    palabra_invertida= palabra[::-1]

    if palabra == palabra_invertida:
        return True
    else:
        return False


def main():
    palabra=input('Escribe una palabra: ')
    esPalindromo = palindromo(palabra)
    if esPalindromo==True:
        print('Es palindromo')
    else:
        print('No es palindromo')


if __name__ == '__main__':
    main()