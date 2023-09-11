from datetime import date, timedelta
from time import sleep


def linha(char='-', tam=42):
    '''Escreve linhas.
    char: Caracter que deseja. Padrão: -
    tam: Tamanho da linha. Padrão: 42
    '''
    print(char * tam)


def titulo(txt):
    '''Cria um título com o nome desejado.
    txt: Título
    '''
    linha()
    print(txt.center(42))
    linha()


def menu(lista, msg='MENU PRINCIPAL'):
    '''Cria uma lista de menu com as opções desejadas.
    lista: Lista com as opções
    msg: Mensagem que será exibida no menu
    '''
    titulo(msg)
    for _e, item in enumerate(lista):
        print(f'{_e + 1}. {item}')
    linha()
    opc = leiaint('Sua opção: ')
    return opc


def leiaint(msg):
    '''
    Lê um número inteiro pelo teclado.
    Retorna 0 se o número for inválido.'''
    while True:
        try:
            _numb = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um número inteiro válido!\33[m]]')
        except KeyboardInterrupt:
            print('\033[31m\nEntrada de lib interrompida pelo usuário\033[m')
            return 0
        else:
            return _numb


def validade_prod(data=date.today(), dias=0):
    '''
    Calcula a validade de um produto.
    data: Data de fabricação do produto.
    dias: Dias que o produto vai vencer.'''
    val = data + timedelta(days=dias)
    linha()
    print(f'Fabricação: {data.strftime("%d/%m/%Y")}')
    print(f'Validade: {val.strftime("%d/%m/%Y")}')
    linha()


while True:
    RESP = menu(['Consultar validade', 'Inserir manualmente', 'Sair...'])
    if RESP == 1:
        PROD = menu(['Leite UHT ( 1Lt)',
                    'Leite Condensado (395g)',
                    'Creme de Leite (200g)',
                    'Achocolatado (200g)', 'Voltar'], 'PRODUTOS ENVASADOS')
        if PROD == 1: # Leite UHT
            validade_prod(dias=120)
        elif PROD == 2: # Leite Condensado
            validade_prod(dias=365)
        elif PROD == 3: # Creme de leite
            validade_prod(dias=300)
        elif PROD == 4: # Achocolatado
            validade_prod(dias=240)
        elif PROD == 5: # Voltar
            print('Aguarde...')
            sleep(1)
            continue
        else:
            print('\033[mERRO: Opção inválida! Tente novamente.\033[m')
    elif RESP == 2:
        linha()
        titulo('DATA MANUAL')
        FAB = str(input('Data de fabricação (formato: 01/01/1900): '))
        vld = int(input('Válido por quantos dias: '))
        validade_prod(FAB, vld)
    elif RESP >= 3:
        print('Finalizando... Aguarde!')
        sleep(2)
        break
