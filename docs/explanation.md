# Cuadratura Gaussiana
La idea principal está dada por

\begin{align}
    \int_a^b {\rm{d}}x f(x) \approx \sum_{k=1}^{N} w_k f(x_k).
\end{align}

donde:
  * $w_k$ son los "pesos"
  * $x_k$ son los puntos de muestreo
  
Para las ecuaciones de Newton-Cotes de la clase anterior:  
  * Los puntos de muestreo son **equidistantes**.
  * Una ecuación de Newton-Cotes de orden $N$ es *exacta* (i.e., no hay aproximación) para un polinomio de grado $N$.
  * Un polinomio de orden $N$ aproxima una función bien comportada mejor que un polinomio de orden $N-1$, debido al grado de libertad añadido.
  
Por el otro lado, para la cuadratura Gaussiana:
  * Los puntos de muestreo se escogen de manera tal que **no son equidistantes**. Esto introduce más grados de libertad para la misma discretización en $N$ subregiones.
  * Es exacta para un polinomio de orden $(2N - 1)$.
  * Es decir, la cuadratura gaussiana con $N$ puntos es exacta para cualquier polinomio de grado hasta $(2N - 1)$.

Los pesos y puntos de muestreo se eligen tal que:
  * $x_k$ corresponden a las $N$ raíces (ceros) de los polinomios de Legendre $P_N(x)$ de orden $N$.
  * Los pesos se eligen tal que:
      - $\displaystyle w_k = \left[\frac{2}{1-x^2}\left(\frac{dP_N}{dx}\right)^{-2}\right]_{x={x_k}}$, con $x_k$ que cumple $P_N(x_k)=0$

## Polinomios de Legendre

Los polinomios de Legendre son un sistema de polinomios ortogonales que pueden ser definidos de manera recursiva. Tenemos:

\begin{align}
    \forall (M, N) \in\mathbb N^2, \quad \int_{-1}^1 {\rm{d}}x P_N(x)P_M(x) = \frac{2\delta_{MN}}{2N+1}.
\end{align}

Note que los polinomios están definidos en el intervalo $[-1, 1]$.
Los se definen empezando con

\begin{align}
    P_0(x) = 1 \Rightarrow P_1(x) = x,
\end{align}

tal que los siguientes órdenes se generan con la regla de recursividad

\begin{align}
    (N+1)P_{N+1}(x) = (2N+1)xP_N(x) -NP_{N-1}(x).
\end{align}

Alternativamente, los polinomios pueden ser definidos de manera iterativa bajo la regla (fórmula de Rodrigues)

\begin{align}
    P_N(x) = \frac1{2^N N!}\frac{d^N}{dx^N}\left[(x^2-1)^N\right].
\end{align}
