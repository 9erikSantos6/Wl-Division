# Wl-Division

## Sobre

Wl-Division é uma ferramenta desenvolvida em Python que simplifica a tarefa de dividir wordlists em partes menores. Em muitos cenários de segurança cibernética, a autenticação é realizada por meio de usuários e senhas. Para testar a segurança de sistemas, é comum utilizar a técnica de brute-force, onde o poder computacional é empregado para tentar várias combinações de usuários e senhas.

Essa abordagem requer o uso de wordlists, que são listas de palavras contendo diversas combinações de caracteres. No entanto, muitas dessas wordlists são extensas e demandam um poder de processamento considerável para obter resultados satisfatórios. É aí que o Wl-Division entra em cena.

O Wl-Division foi criado para mitigar esse desafio. Ele permite dividir uma wordlist grande em partes menores, conforme especificado. Isso possibilita a execução do processo de brute-force em várias instâncias seu script de forma simultânea, ou, se você tiver acesso a múltiplos dispositivos ou máquinas, é possível distribuir as divisões da wordlist entre eles. Dessa forma, os recursos disponíveis são aproveitados ao máximo, aumentando a eficiência do processo.

Essa funcionalidade se torna útil em testes de penetração e investigações forenses, onde a divisão de wordlists em partes menores pode acelerar consideravelmente o tempo necessário para realizar os testes de brute force e obter resultados relevantes.


Requirements
------------

Você precisa do Python3 para rodar o Wl-Division


Quick start
-----------

    $ git clone https://github.com/9erikSantos6/Wl-Division.git   

    $ cd Wl-Division

    $ pip install -r requirements.txt
    
    $ chmod +x wldivision.py 

    $ ./wldivision -h

## Opções

    Usagem: wldivision.py

        -h      Este menu de help

        -w      Caminho para a wordlist que você quer dividir

        -d      Número de divisões a serem feitas na wordlist

        -c      Criar o diretorio de saída para as divisões de wordilist caso não exista

        -o      Diretório de saída para as divisões de wordlist

        -v      Mostra a versão deste programa

## Exemplo

    $ ./wldivision.py -w </caminho/para/wordilist/original> -d <numero-de-divisões> -o </caminho/de/despejo>

## License

  This program is free software; you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation; either version 3 of the License, or
  any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program; if not, write to the Free Software
  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

  See './LICENSE' for more information.


## Commit no GitHub

Esse projeto foi comitado em https://github.com/9erikSantos6/Wl-Division por 9erikSantos6


## Autor Original

    9erikSantos6
    https://github.com/9erikSantos6
