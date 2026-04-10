#CADASTRO de gastos diários de clientes com ficha mensal em mercado.
import time
import func

cadastro = dict()
venda = list()
encerrar = False

print('SEJA BEM-VINDO AO CADASTRAMENTO DE VENDAS DO DIA')
while True:
    while True:
        cadastro = func.cadastrar_cliente()
        print(f'Cliente: {cadastro["cliente"]} - Valor gasto: R${cadastro["valor"]:.2f} - data: {cadastro["dia"]}')
        time.sleep(2)

        resp = str(input('Se os dados estão corretos digite S, para corrigir digite ERRO: ')).upper()
        if resp == "S":
            print(f'Dados cadastrados.')
            venda.append(cadastro.copy())
            break
        elif resp == "ERRO":
            print(f'TENTE NOVAMENTE!')
        else:
            print(f'ERRO, TENTE NOVAMENTE!')
    while True:
        mais = input('Quer cadastrar mais uma venda S=sim e N=não: ').upper()
        if mais == 'S':
            print('Próximo Cadastro de Venda:')
            break
        elif mais == 'N':
            print('Finalizando cadastros do dia...Até logo!')
            time.sleep(2)
            encerrar = True
            break
        else:
            print('Digite apenas S ou N!')

    if encerrar:
        break

func.mostrar_resumo(venda)
