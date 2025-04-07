from random import choice

palavras = {
    "tecnologia": [
        "python", "programacao", "computador", "teclado", "monitor",
        "internet", "software", "hardware", "algoritmo", "dados"
    ],
    "animais": [
        "elefante", "girafa", "tigre", "jacare", "golfinho",
        "cachorro", "gato", "abelha", "tatu", "coruja"
    ],
    "frutas": [
        "banana", "maca", "uva", "morango", "laranja",
        "abacaxi", "melancia", "cereja", "kiwi", "pera"
    ],
    "objetos": [
        "cadeira", "geladeira", "telefone", "luminaria", "mochila",
        "capacete", "escova", "relógio", "janela", "prateleira"
    ],
    "cidades_do_brasil": [
        "sao paulo", "rio de janeiro", "belo horizonte", "curitiba", "salvador",
        "fortaleza", "manaus", "recife", "goiania", "florianopolis"
    ]
}

def escolher_palavra_aleatoria():
    """
    Escolhe uma palavra aleatória de uma categoria aleatória.
    :return: Uma tupla contendo a categoria e a palavra escolhida.
    """
    categoria = choice(list(palavras.keys()))
    palavra = choice(palavras[categoria])
    return categoria, palavra

def obter_letra():
    """
    Solicita ao usuário uma letra válida.
    :return: Uma única letra válida.
    """
    while True:
        letra = input('Digite uma letra: ').lower().strip()
        if len(letra) != 1 or not letra.isalpha():
            print("⚠ Entrada inválida! Digite apenas uma única letra.")
        else:
            return letra