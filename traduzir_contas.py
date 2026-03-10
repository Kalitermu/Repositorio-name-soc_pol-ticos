def traduzir_conta(conta):

    mapa = {
        "10": "Saúde",
        "12": "Educação",
        "15": "Urbanismo / Obras",
        "08": "Assistência Social",
        "04": "Administração pública",
        "06": "Segurança pública",
        "18": "Gestão ambiental"
    }

    if conta is None:
        return "Não identificado"

    prefixo = str(conta)[:2]

    return mapa.get(prefixo,"Outros")
