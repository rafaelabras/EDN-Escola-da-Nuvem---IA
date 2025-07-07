def eh_palindromo(texto: str) -> str:
    texto_filtrado = ''.join(c.lower() for c in texto if c.isalnum())
    return "Sim" if texto_filtrado == texto_filtrado[::-1] else "Não"

frase = input("Digite uma palavra ou frase: ")
print("É palíndromo?", eh_palindromo(frase))
