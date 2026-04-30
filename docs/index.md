# Cuadratura Gauss-Legendre

El problema consiste en escribir un script de Python llamado
`cuadrature.py`, el cual permita aproximar numéricamente la integral

\begin{align}
    I = \int_{0}^{\pi} \sin(x^2)\, dx
\end{align}

utilizando el método de cuadratura Gaussiana visto en clase. Este caso
es importante desde el punto de vista computacional, ya que la integral
no posee una solución analítica simple.

Además, se debe calcular el valor aproximado de la integral para
diferentes valores de \(N\), donde \(N\) representa el número de puntos
utilizados en la cuadratura. Finalmente, se debe realizar un gráfico del
resultado de la integral en función de \(N\), con el objetivo de observar
cómo cambia la aproximación conforme aumenta el orden del método.
