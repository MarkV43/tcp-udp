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

$$ m \ell^2 \ddot \theta = -m \ddot x_v \ell \cos \theta - m g \ell \sin \theta - b \dot \theta $$
$$ (M + m) \ddot x_v = m \dot\theta^2 \ell \sin \theta - m \ddot\theta \ell \cos \theta + F(t) - d\dot x_v $$

### Simbologia

$m$ Massa da carga $\leq 5000$ Kg

$M$ Massa da viga $= 496$ Kg

$\ell$ Comprimento do cabo entre viga e carga $= 7$ m

$x_v$ Posição da viga

$g$ Gravidade $= 9.81$ m/s²

$\theta$ Ângulo de inclinação do cabo com a vertical

$F$ Força na viga (variável controlada) $\leq 44.1$ KN

$b$ Coeficiente de atrito do ar $\approx 100$

$d$ Coeficiente de atrito com o eixo de deslocamento $\approx 100$

$\dot f$ Primeira derivada de $f$ no tempo

$\ddot f$ Segunda derivada de $f$ no tempo

# Execução

## Pré-requisitos

Você precisará da biblioteca `tkinter`. Para instalá-la, basta executar `pip install tk`

Para executar o projeto você precisará de três janelas de comando.
Na primeira, execute `python simulador/main.py`.
Na segunda, execute `python controlador/main.py`.
Na terceira, execute `python panel/main.py`.

Na terceira janela você pode digitar números para alterar o valor e referência.
