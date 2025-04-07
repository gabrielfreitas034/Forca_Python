def obter_forca(tentativas_restantes=6):
    """
    Retorna o estado atual do boneco da forca com base no número de tentativas restantes.
    :param tentativas_restantes: Número de tentativas restantes (de 0 a 6).
    :return: Uma string representando o estado atual do boneco da forca.
    """
    estados = [
        """
           ------
           |    |
           |
           |
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """
    ]
    return estados[6 - tentativas_restantes]
