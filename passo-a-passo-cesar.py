from string import ascii_uppercase

alfabeto = list(ascii_uppercase)

def codifica(mensagem, chave):
    """Recebe uma string com a mensagem e uma chave de codificação e retorna uma mensagem cifrada"""
    cifra = ""
    for letra in mensagem:
        indice = ord(letra)-65
        cifra+= alfabeto[(indice+chave) % len(alfabeto)] if letra in alfabeto else letra
    return cifra

def decodifica(mensagem, chave):
    """Recebe uma string com a mensagem codificada e a chave de decodificação e retorna uma mensagem decodificada""" 
    return codifica(mensagem, len(alfabeto)-chave)

if __name__ == "__main__":
	mensagem = "AMADOR PROGRAMA EM LINUX"
	chave = 4
	codigo = codifica(mensagem, chave)
	print("Mensagem:", mensagem)
	print("Código:", codigo)
	print("Código decodificado:", decodifica(codigo, chave))
