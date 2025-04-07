import forca, palavras, core  # Importando os módulos necessários para o jogo
import os  # Import necessário para limpar a tela

def jogar():
    print("\n🎯 **BEM-VINDO AO JOGO DA FORCA!** 🎯\n")
    categoria, palavra, tentativas, letra_correta, letra_digitada = core.inicializar_jogo()
    dica = None  # Variável para armazenar a dica
    mensagem = ""  # Variável para armazenar mensagens de feedback
    primeira_iteracao = True  # Flag para controlar a exibição da mensagem inicial

    while tentativas > 0:
        if not primeira_iteracao:
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela
        else:
            primeira_iteracao = False  # Após a primeira iteração, a flag é desativada

        print(mensagem)  # Exibe a mensagem da última interação
        core.exibir_status(tentativas, letra_correta, letra_digitada, dica)
        escolha = core.exibir_menu()

        if escolha == '1':  # Digitar uma letra
            letra = palavras.obter_letra()
            if letra in letra_digitada:
                mensagem = f'⚠ A letra "{letra}" já foi digitada, tente outra!'
                continue
            if core.processar_letra(letra, palavra, letra_correta, letra_digitada):
                mensagem = f'✅ A letra "{letra}" está na palavra!'
                if "_" not in letra_correta:
                    print(f'\n🎉 Parabéns! Você acertou a palavra: {palavra.upper()} 🎉')
                    break
            else:
                tentativas -= 1
                mensagem = f'❌ A letra "{letra}" não existe na palavra!'

        elif escolha == '2':  # Pedir uma dica
            dica = f'A categoria é "{categoria.upper()}".'  # Salva a dica

        elif escolha == '3':  # Chutar a palavra
            chute = input("Digite sua palavra: ").strip()
            if core.processar_chute(chute, palavra):
                print(f'\n🎉 Parabéns! Você acertou a palavra: {palavra.upper()} 🎉')
                break
            else:
                tentativas -= 1
                mensagem = f'❌ "{chute}" não é a palavra correta!'

    if tentativas == 0:
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela antes de exibir a mensagem final
        print(forca.obter_forca(0))
        print(f'\n💀 Você perdeu! A palavra era: {palavra.upper()}.')

    print("\nObrigado por jogar! 😃")

jogar()