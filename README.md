<!---
	To compile the LaTeX in this file to README.md, one must run the commands
	`python -m readme2tex --output README.md INPUT.md --nocdn`
	`python fix-svg-color.py`

	To install the first tool you must run
	`pip install readme2tex`
-->

# Trabalho TCP e UDP

Um trabalho para a disciplina de _Redes de Computadores para Automação_ desenvolvido por Ícaro Bedôr Cavalcante e Marcelo Vogt.

## Definição

O trabalho, implementado em Python, consiste de 3 estações (um simulador, um controlador e um painel de controle) que comunicam entre si.
O painel de controle envia através de TCP, dados para alteração de parâmetros de controle no controlador.
O controlador consiste de um sistema de controle discreto que interage com o simulador via UDP.
O simulador mostra uma representação fiel do sistema real ao usuário, e envia através de UDP também, o estado atual para o controlador.

## O processo

O processo físico consiste de uma ponte rolante uniaxial.

<p align="center"><img src="svgs/0e9a55de53e1e1a347c16262da9f0947.svg?invert_in_darkmode" align=middle width=264.6421899pt height=18.512775599999998pt/></p>
<p align="center"><img src="svgs/836b283b474b11995cfb2f9ac3600e9c.svg?invert_in_darkmode" align=middle width=356.74443254999994pt height=19.4260143pt/></p>

### Simbologia

<img src="svgs/0e51a2dede42189d77627c4d742822c3.svg?invert_in_darkmode" align=middle width=14.433101099999991pt height=14.15524440000002pt/> Massa da carga <img src="svgs/8cc5b242521d00854cf3cd97ee01499c.svg?invert_in_darkmode" align=middle width=50.22836939999999pt height=21.18721440000001pt/> Kg

<img src="svgs/fb97d38bcc19230b0acd442e17db879c.svg?invert_in_darkmode" align=middle width=17.73973739999999pt height=22.465723500000017pt/> Massa da viga <img src="svgs/a05e2235eef34e3ad8345d8746fe5b6a.svg?invert_in_darkmode" align=middle width=42.00916004999999pt height=21.18721440000001pt/> Kg

<img src="svgs/d30a65b936d8007addc9c789d5a7ae49.svg?invert_in_darkmode" align=middle width=6.849367799999992pt height=22.831056599999986pt/> Comprimento do cabo entre viga e carga <img src="svgs/b8f8e99442889e80d6502f1beca739ee.svg?invert_in_darkmode" align=middle width=25.570741349999988pt height=21.18721440000001pt/> m

<img src="svgs/f45e64c5ffa0374b4ef861d4f0144021.svg?invert_in_darkmode" align=middle width=16.383249299999992pt height=14.15524440000002pt/> Posição da viga

<img src="svgs/3cf4fbd05970446973fc3d9fa3fe3c41.svg?invert_in_darkmode" align=middle width=8.430376349999989pt height=14.15524440000002pt/> Gravidade <img src="svgs/a499f99af6a9e92d550633ee68ff6276.svg?invert_in_darkmode" align=middle width=46.57538489999998pt height=21.18721440000001pt/> m/s²

<img src="svgs/27e556cf3caa0673ac49a8f0de3c73ca.svg?invert_in_darkmode" align=middle width=8.17352744999999pt height=22.831056599999986pt/> Ângulo de inclinação do cabo com a vertical

<img src="svgs/b8bc815b5e9d5177af01fd4d3d3c2f10.svg?invert_in_darkmode" align=middle width=12.85392569999999pt height=22.465723500000017pt/> Força na viga (variável controlada) <img src="svgs/77bf082e145a70a3ff1d2f7ca122e95a.svg?invert_in_darkmode" align=middle width=46.57538489999998pt height=21.18721440000001pt/> KN

<img src="svgs/4bdc8d9bcfb35e1c9bfb51fc69687dfc.svg?invert_in_darkmode" align=middle width=7.054796099999991pt height=22.831056599999986pt/> Coeficiente de atrito do ar <img src="svgs/5ab7be53be041e6b2240494870061da9.svg?invert_in_darkmode" align=middle width=42.00916004999999pt height=21.18721440000001pt/>

<img src="svgs/2103f85b8b1477f430fc407cad462224.svg?invert_in_darkmode" align=middle width=8.55596444999999pt height=22.831056599999986pt/> Coeficiente de atrito com o eixo de deslocamento <img src="svgs/5ab7be53be041e6b2240494870061da9.svg?invert_in_darkmode" align=middle width=42.00916004999999pt height=21.18721440000001pt/>

<img src="svgs/100f3b1bc4e9452f6562e800febf5c60.svg?invert_in_darkmode" align=middle width=9.93164039999999pt height=30.632847300000012pt/> Primeira derivada de <img src="svgs/190083ef7a1625fbc75f243cffb9c96d.svg?invert_in_darkmode" align=middle width=9.81741584999999pt height=22.831056599999986pt/> no tempo

<img src="svgs/3a0328249aa81733bf44a7d91ba2e0b9.svg?invert_in_darkmode" align=middle width=11.75813594999999pt height=30.632847300000012pt/> Segunda derivada de <img src="svgs/190083ef7a1625fbc75f243cffb9c96d.svg?invert_in_darkmode" align=middle width=9.81741584999999pt height=22.831056599999986pt/> no tempo

# Execução

## Pré-requisitos

Você precisará da biblioteca `tkinter`. Para instalá-la, basta executar `pip install tk`

Para executar o projeto você precisará de três janelas de comando.
Na primeira, execute `python simulador/main.py`.
Na segunda, execute `python controlador/main.py`.
Na terceira, execute `python panel/main.py`.

Na terceira janela você pode digitar números para alterar o valor e referência.
