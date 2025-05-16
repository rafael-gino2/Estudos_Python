# 8. Organiza número. Faça uma rotina que organize os números recebidos em: crescente,
# decrescente e reverso.
# Por exemplo:
# recebido: 293
# ● crescente: 239
# ● decrescente: 932
# ● reverso: 392
numero = 293
def organiza_numero(numero):
    # Converte o número para string para poder acessar cada dígito
    str_numero = str(numero)

    # Crescente: ordena os dígitos do menor para o maior
    crescente = ''
    for digito in sorted(str_numero):
        crescente += digito

    # Decrescente: ordena os dígitos do maior para o menor
    decrescente = ''
    for digito in sorted(str_numero, reverse=True):
        decrescente += digito

    # Reverso: inverte a ordem dos dígitos
    reverso = ''
    for i in range(len(str_numero)-1, -1, -1):
        reverso += str_numero[i]

    return int(crescente), int(decrescente), int(reverso)

crescente, decrescente, reverso = organiza_numero(numero)

print(f"Recebido: {numero}")
print(f"● crescente: {crescente}")
print(f"● decrescente: {decrescente}")
print(f"● reverso: {reverso}")