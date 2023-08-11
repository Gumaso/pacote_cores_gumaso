def funcao_teste(nome):
    """Recebe um nome e o devolve colorido"""
    nome_colorido = f"\033[32m{nome}\033[m"
    return nome_colorido