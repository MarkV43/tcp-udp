# Trabalho TCP e UDP

Um trabalho para a disciplina de _Redes de Computadores para Automação_ desenvolvido por Ícaro Bedôr Cavalcante e Marcelo Vogt.

## Definição
---

O trabalho, implementado em Python, consiste de 2 estações (um controlador e um painel de controle) que comunicam entre si.
O painel de controle envia através de TCP dados para alteração de parâmetros de controle no controlador.
O controlador consiste de um simulador de um processo (dado que não temos o sistema físico em si) e de um sistema de controle discreto que interage dado processo, enviando o estado atual ao painel de controle via UDP.
O painel de controle, sendo atualizado disso, apresenta visualmente, tanto uma representação fiel do sistema, quanto em forma de gráficos, ao usuário, esses dados.

## O processo
---

O processo físico consiste de uma ponte rolante uniaxial.

$$ m \ell^2 \ddot \theta = -m \ddot x_v \ell \cos \theta - m g \ell \sin \theta - b \dot \theta $$
$$ (M + m) \ddot x_v = m \dot\theta^2 \ell \sin \theta - m \ddot\theta \ell \cos \theta + F(t) - d\dot x_v $$

### Simbologia
---

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
