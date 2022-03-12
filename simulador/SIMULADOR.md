$$ m \ell^2 \ddot \theta = -m \ddot x_v \ell \cos \theta - m g \ell \sin \theta - b \dot \theta $$
$$ (M + m) \ddot x_v = m \dot\theta^2 \ell \sin \theta - m \ddot\theta \ell \cos \theta + F(t) - d\dot x_v $$

Resolvendo as EDOs para $\ddot x_v$ e $\ddot\theta$, obtemos

$$ \ddot x_v = \frac{1}{M + m \sin^2 \theta} \left( m \dot\theta^2 \ell \sin \theta + m \cos \theta \left( g \sin \theta + \frac{b \dot\theta}{m \ell} \right) + F(t) - d \dot x_v \right) $$

$$ \ddot\theta = - \frac{1}{\ell} \frac{\cos\theta}{M + m \sin^2 \theta} \left( m \dot\theta^2 \ell \sin \theta + m \cos \theta \left( g \sin \theta + \frac{b \dot\theta}{m \ell} \right) + F(t) - d \dot x_v \right) - \frac{g \sin \theta}{\ell} - \frac{b \dot\theta}{m \ell^2} $$

Para rodar o simulador você precisa da biblioteca `p5` do Python.
Para instalá-la, siga [as intruções](https://p5.readthedocs.io/en/latest/install.html).
