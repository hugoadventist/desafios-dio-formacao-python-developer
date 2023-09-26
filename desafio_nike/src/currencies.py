def parser_currencies(currencies="BRL-USD,BRL-EUR,BRL-INR"):
    if not isinstance(currencies, str):
        raise TypeError("Favor inserir uma lista com os parâmetros válidos!")
    return currencies


parser_currencies()
