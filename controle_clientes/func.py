from datetime import date

#cadastrar dados
def cadastrar_cliente():
    cadastro = {}

    cadastro['cliente'] = input('Digite o nome do cliente: ').upper()
    cadastro['valor'] = float(input('Digite o valor gasto: R$ '))
    cadastro['dia'] = date.today()

    return cadastro

#resumo das vendas do dia
def mostrar_resumo(venda):
    print('\nRESUMO DO DIA:')
    total = 0

    for c in venda:
        print(f"{c['cliente']} - R${c['valor']:.2f}")
        total += c['valor']

    print(f"\nTOTAL DO DIA: R${total:.2f}")