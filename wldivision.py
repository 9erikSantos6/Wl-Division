#!/usr/bin/python3
#
#  [Program]
#
#  Wl-Division
#  A wordlist divider
#
#  [Author]
#
#  9erikSantos6
#
#  [License]
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import argparse
__author__ = "9erikSantos6"
__license__ = "MIT"
__version__ = "1.0"

def banner():
    letreiro = '''
    ██╗    ██╗██╗      ██████╗ ██╗██╗   ██╗██╗███████╗██╗ ██████╗ ███╗   ██╗    
    ██║    ██║██║      ██╔══██╗██║██║   ██║██║██╔════╝██║██╔═══██╗████╗  ██║    
    ██║ █╗ ██║██║█████╗██║  ██║██║██║   ██║██║███████╗██║██║   ██║██╔██╗ ██║    
    ██║███╗██║██║╚════╝██║  ██║██║╚██╗ ██╔╝██║╚════██║██║██║   ██║██║╚██╗██║    
    ╚███╔███╔╝███████╗ ██████╔╝██║ ╚████╔╝ ██║███████║██║╚██████╔╝██║ ╚████║    
    ╚══╝╚══╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝  ╚═╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝     
    '''
    largura_banner = max(len(linha) for linha in letreiro.split('\n'))
    borda = '=' * (largura_banner + 4)
    espaco = ' ' * (largura_banner - 62)
    github_link = '[ Erik | https://github.com/9erikSantos6 ]'
    texto_versao = __version__
    banner = f'''\n{borda}
    \n{letreiro}
    \n{espaco}{github_link}{espaco}v{texto_versao}
    \n{borda}\n
    '''
    print(banner)


def mostrar_versao():
    print(f'Wl-Division {__version__} ( https://github.com/9erikSantos6/Wl-Division )')
    print('Plataforma: x86_64-pc-linux-gnu')
    print('Compilado com: Python-3.11.8')
    print('Bibliotecas: python-magic-0.4.27')
    print('Data de Lançamento: 27/04/2024')
    print('Atualizado por: 9erikSantos6')


def detectar_encode_arquivo(caminho_arquivo_origem=''):
    from magic import Magic
    arquivo = open(caminho_arquivo_origem, 'rb').read()
    magic = Magic(mime_encoding=True)
    encode = magic.from_buffer(arquivo)
    return encode


def dividir_inigualmente(num, divisoes):
    try:
        result_list = []
        div_inteira = num // divisoes
        resto_div = num % divisoes
        for _ in range(divisoes - resto_div):
            result_list.append(div_inteira)
        for _ in range(resto_div):
            result_list.append(div_inteira + 1)
        return result_list
    except Exception as erro_divisao:
        print(f"[\033[05m✗\033[25m\033[1;m] Ocorreu um erro: {erro_divisao}")
        return


def aprovar_disponibilidade_arquivo_origem(caminho_arquivo_origem=''):
    try:
        if os.path.exists(caminho_arquivo_origem):
            if os.path.isfile(caminho_arquivo_origem):
                nome_arquivo = os.path.basename(caminho_arquivo_origem)
                extensoes_suportadas = ['.txt', '.md', '.rst', '.log', '.lst']
                extensao_do_arquivo = os.path.splitext(nome_arquivo)[-1]

                if extensao_do_arquivo not in extensoes_suportadas:
                    print(f'[\033[05m✗\033[25m\033[1;m] Erro: O arquivo {nome_arquivo} não é suportado!')
                    print('[\033[05m✗\033[25m\033[1;m] Use .txt, .md, .lst, .rst,  ou .log')
                    return False

                return True

            print(f'[\033[05m✗\033[25m\033[1;m] Erro: O arquivo de origem é uma pasta!')
            return False

        else:
            print(f'[\033[05m✗\033[25m\033[1;m] Erro: O caminho do arquivo {caminho_arquivo_origem} não existe!')
            return False

    except Exception as erro_leitura:
        print(f'[\033[05m✗\033[25m\033[1;m] Erro ao tentar ler linhas de {nome_arquivo}: {erro_leitura}')


def aprovar_divisibilidade_arquivo_origem(numero_divisoes = 2, caminho_arquivo_origem = ''):
    try:
        with open(caminho_arquivo_origem, 'r', encoding=detectar_encode_arquivo(caminho_arquivo_origem), errors='ignore') as arquivo:
            try:
                conteudo_arquivo = arquivo.readlines()
                linhas_arquivo = len(conteudo_arquivo)
                numero_divisoes =  2 if numero_divisoes < 2 else numero_divisoes 
                if linhas_arquivo < numero_divisoes:
                    print(f'[\033[05m✗\033[25m\033[1;m] Erro: O arquivo {caminho_arquivo_origem} não tem linhas suficientes!')
                    return False

                return True

            except Exception as erro_leitura:
                print(f'[\033[05m✗\033[25m\033[1;m] Erro ao tentar ler linhas de {caminho_arquivo_origem}: {erro_leitura}')

    except Exception as erro_abertura:
        print(f'[\033[05m✗\033[25m\033[1;m] Erro ao abrir {caminho_arquivo_origem}: {erro_abertura}')


def criar_diretoro(caminho_arquivo_destino='', criar_novo_diretorio=False):
    if criar_novo_diretorio:
        if not os.path.exists(caminho_arquivo_destino):
            if not os.path.isfile(caminho_arquivo_destino):
                try:
                    os.makedirs(caminho_arquivo_destino)
                    print(f'* Diretório {caminho_arquivo_destino} criado com sucesso! [\033[05m✓\033[25m\033[1;m]')

                except Exception as erro_criar_diretorio:
                    print(f'[\033[05m✗\033[25m\033[1;m] Erro ao tentar criar o diretório {caminho_arquivo_destino}: {erro_criar_diretorio}')

            else:
                print(f'[\033[05m✗\033[25m\033[1;m]  Erro: O diretório {caminho_arquivo_destino} é um arquivo!')

        else:
            print(f'[\033[05m!\033[25m\033[1;m] Alerta: O diretório {caminho_arquivo_destino} já existe!')
            print(f'[\033[05m!\033[25m\033[1;m] Salvando em {caminho_arquivo_destino} mesmo assim...')


def aprovar_disponibilidade_diretorio_destino(caminho_arquivo_destino='', criar_novo_diretorio=False):
    try:
        criar_diretoro(caminho_arquivo_destino, criar_novo_diretorio)
        if os.path.exists(caminho_arquivo_destino):
            if os.path.isdir(caminho_arquivo_destino):
                return True

            nome_arquivo = os.path.basename(caminho_arquivo_destino)
            print(f'[\033[05m✗\033[25m\033[1;m] Erro: O arquivo {nome_arquivo} não é uma pasta!')
            return False

        print(f'[\033[05m✗\033[25m\033[1;m] Erro: O caminho do arquivo {caminho_arquivo_destino} não existe!')
        return False

    except Exception as erro_abertura:
        print(f'[\033[05m✗\033[25m\033[1;m] Erro ao tentar abrir: {caminho_arquivo_destino}: {erro_abertura}')


def aprovar_usagens(caminho_arquivo_origem='', numero_divisoes=2, caminho_arquivo_destino='', criar_novo_diretorio=False):
    try:
        if not aprovar_disponibilidade_arquivo_origem(caminho_arquivo_origem):
            return False

        if not aprovar_divisibilidade_arquivo_origem(numero_divisoes, caminho_arquivo_origem):
            return False

        if not aprovar_disponibilidade_diretorio_destino(caminho_arquivo_destino, criar_novo_diretorio):
            return False

        return True

    except Exception as erro_aprovacao:
        print(f'[\033[05m✗\033[25m\033[1;m] Erro no tratamento de paramentros: {erro_aprovacao}')
        return False


def escrever_novo_arquivo(caminho_arquivo_destino='', nome_wordlist='', lista_de_palavras=[]):
    try:
        if os.path.exists(caminho_arquivo_destino):
            nome_wordlist = nome_wordlist + '.lst'
            caminho_absoluto_nova_lista = os.path.normpath(f'{caminho_arquivo_destino}/{nome_wordlist}')
            with open(caminho_absoluto_nova_lista, 'w', encoding='utf-8') as arquivo:
                arquivo.write(''.join(lista_de_palavras))

            print(f'* Lista {os.path.basename(caminho_absoluto_nova_lista)} criada com sucesso! [\033[05m✓\033[25m\033[1;m]\n     └─> {caminho_absoluto_nova_lista}\n')
            return

    except Exception as error:
        print(f'[\033[05m✗\033[25m\033[1;m] O correu um erro ao tentar criar as wordlists: {error}')


def dividir_arquivo(args):
    try:
        caminho_arquivo_origem = args.caminho_wordlist_origem
        numero_divisoes = args.numero_divisoes
        caminho_arquivo_destino = args.caminho_novas_wordilists
        criar_novo_diretorio = args.criar_novo_diretorio

        if aprovar_usagens(caminho_arquivo_origem, numero_divisoes,  caminho_arquivo_destino, criar_novo_diretorio):
            numero_divisoes = 2 if numero_divisoes < 2 else numero_divisoes
            encode_arquivo_origem = detectar_encode_arquivo(caminho_arquivo_origem)
            print('\n> Processando...\n')

            with open(caminho_arquivo_origem, 'r', encoding=encode_arquivo_origem, errors='ignore') as arquivo:
                conteudo_arquivo = arquivo.readlines()
                linhas_arquivo = len(conteudo_arquivo)
                linhas_chunks = dividir_inigualmente(linhas_arquivo, numero_divisoes)
                linhas_indexes = 0
                lista_de_palavras = []

                for i, chunk in enumerate(linhas_chunks):
                    for _ in range(chunk):
                        lista_de_palavras.append(conteudo_arquivo[linhas_indexes])
                        linhas_indexes += 1

                    nome_arquivo_atual = f'{os.path.splitext(os.path.basename(caminho_arquivo_origem))[0]}-division-{i+1}'
                    escrever_novo_arquivo(caminho_arquivo_destino, nome_arquivo_atual, lista_de_palavras)

            print('> \033[05mConcluído!\033[25m\033[1;m')
            return

        print('[\033[05m✗\033[25m\033[1;m] Erro de usagem, verifique novamente os argumentos!')
        return

    except Exception as error_divisao_arquivo:
        print(f'[\033[05m✗\033[25m\033[1;m] Erro ao tentar dividir o arquivo: {error_divisao_arquivo}')


def main():
    banner()
    parser = get_parser()
    args = parser.parse_args()

    if args.versao:
        mostrar_versao()

    elif args.caminho_wordlist_origem:
        dividir_arquivo(args)

    else:
        parser.print_help()


def get_parser():
    parser = argparse.ArgumentParser(description="Wl-Division é um programa de usagem simples que vai te ajudar a dividir wordlists!")

    parser.add_argument(
        '--wordlist-base',
        '-w',
        metavar='WORDLIST_PATH',
        dest='caminho_wordlist_origem',
        help='Caminho da wordlist originária',
        type=str,
    )

    parser.add_argument(
        '--divisions',
        '-d',
        dest='numero_divisoes',
        metavar='DIVISIONS_NUMBER',
        default=2,
        required=False,
        type=int,
        help='Número de divisões que será feito na wordlist',
    )

    parser.add_argument(
        '--output-folder',
        '-o',
        metavar='DUMP_FOLDER',
        dest='caminho_novas_wordilists',
        help='Pasta de output para as novas listas',
        type=str,
    )

    parser.add_argument(
        '--create-folder',
        '-c',
        dest='criar_novo_diretorio',
        action='store_true',
        help='Se o diretório de destino não exite,'
        'passe esse parâmentro para criá-lo'
    )

    parser.add_argument(
        '--version',
        '-v',
        dest='versao',
        action='store_true',
        help='Mostra a versão desse programa'
    )

    return parser


if __name__ == "__main__":
    main()
