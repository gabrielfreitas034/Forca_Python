# Jogo da Forca

Bem-vindo ao **Jogo da Forca**! Este é um jogo clássico onde o jogador tenta adivinhar uma palavra secreta antes que o boneco da forca seja completado.

## Estrutura do Projeto

O projeto está organizado em diferentes módulos para facilitar a manutenção e a expansão do código. Abaixo está a descrição de cada arquivo:

### Arquivos e Funções

#### 1. `core/__init__.py`
Este módulo contém as funções principais para inicializar o jogo, exibir o status, processar letras e chutes, e exibir o menu.

- **Funções**:
  - `inicializar_jogo()`: Inicializa as variáveis do jogo.
  - `exibir_status()`: Exibe o status atual do jogo, incluindo a palavra, tentativas restantes e letras digitadas.
  - `processar_letra()`: Processa a letra digitada pelo jogador.
  - `processar_chute()`: Processa o chute do jogador.
  - `exibir_menu()`: Exibe o menu de opções para o jogador.

#### 2. `forca/__init__.py`
Este módulo é responsável por exibir o estado do boneco da forca com base no número de tentativas restantes.

- **Funções**:
  - `obter_forca(tentativas_restantes)`: Retorna o estado atual do boneco da forca.

#### 3. `palavras/__init__.py`
Este módulo gerencia as palavras e categorias do jogo.

- **Funções**:
  - `escolher_palavra_aleatoria()`: Escolhe uma palavra aleatória de uma categoria aleatória.
  - `obter_letra()`: Solicita ao jogador uma letra válida.

#### 4. `jogarForca.py`
Este é o arquivo principal que executa o jogo. Ele utiliza os módulos `core`, `forca` e `palavras` para gerenciar o fluxo do jogo.

- **Funções**:
  - `jogar()`: Função principal que controla o jogo.

## Como Jogar

1. Execute o arquivo `jogarForca.py`.
2. Escolha uma das opções no menu:
   - Digitar uma letra.
   - Pedir uma dica (categoria da palavra).
   - Chutar a palavra inteira.
3. Continue jogando até adivinhar a palavra ou esgotar as tentativas.

## Requisitos

- Python 3.6 ou superior.

## Como Executar

1. Certifique-se de que você tem o Python instalado em sua máquina.
2. Navegue até o diretório do projeto.
3. Execute o comando:
   ```bash
   python jogarForca.py
   ```

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou novas funcionalidades para o jogo. Basta abrir um pull request ou relatar problemas na seção de issues.

## Licença

Este projeto é de uso livre para fins educacionais e recreativos.

---
Divirta-se jogando! 🎉
