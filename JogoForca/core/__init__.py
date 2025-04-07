import palavras, forca

def inicializar_jogo():
    """
    Inicializa as variáveis do jogo.
    :return: categoria, palavra, tentativas, letra_correta, letra_digitada
    """
    categoria, palavra = palavras.escolher_palavra_aleatoria()
    tentativas = 6
    letra_correta = [' ' if char == ' ' else '_' for char in palavra]
    letra_digitada = []
    return categoria, palavra, tentativas, letra_correta, letra_digitada

def exibir_status(tentativas, letra_correta, letra_digitada, dica=None):
    """
    Exibe o status atual do jogo.
    """
    print(forca.obter_forca(tentativas))
    print("\nPalavra: ", ' '.join(letra_correta))
    print(f"\nLetras tentadas: {', '.join(letra_digitada) if letra_digitada else 'Nenhuma'}")
    print(f"Tentativas restantes: {tentativas}")
    if dica:  # Exibe a dica se ela existir
        print(f"📌 Dica: {dica}")
    print("=" * 30)

def processar_letra(letra, palavra, letra_correta, letra_digitada):
    """
    Processa a letra digitada pelo jogador.
    :return: True se a letra está na palavra, False caso contrário.
    """
    letra_digitada.append(letra)
    if letra in palavra:
        for i, v in enumerate(palavra):
            if v == letra:
                letra_correta[i] = letra
        return True
    return False

def processar_chute(chute, palavra):
    """
    Processa o chute do jogador.
    :return: True se o chute está correto, False caso contrário.
    """
    return chute.lower() == palavra.lower()

def exibir_menu():
    """
    Exibe o menu de opções para o jogador.
    :return: A escolha do jogador.
    """
    print("\nEscolha uma opção:")
    print("1. Digitar uma letra")
    print("2. Pedir uma dica (categoria)")
    print("3. Chutar a palavra")
    while True:
        escolha = input("Digite o número da sua escolha: ").strip()
        if escolha in ['1', '2', '3']:
            return escolha
        print("⚠ Escolha inválida! Tente novamente.")