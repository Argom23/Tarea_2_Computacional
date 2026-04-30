#!/bin/env python3

from scipy.special import legendre
import matplotlib.pyplot as plt
import numpy as np

def gaussxw(N):
    """
    Compute Gauss-Legendre quadrature points and weights.

    Args:
        N (int): Number of quadrature points (order of the approximation).

    Returns:
        tuple:
            - x (ndarray): Quadrature points in the interval [-1, 1].
            - w (ndarray): Corresponding weights for each point.

    Examples:
        >>> x, w = gaussxw(2)
        >>> x
        array([-0.57735027,  0.57735027])
        >>> w
        array([1., 1.])
    """
    x, w = np.polynomial.legendre.leggauss(N)
    return x, w


def gaussxwab(a, b, x, w):
    """
    Rescale Gauss-Legendre quadrature points and weights
    from the standard interval [-1, 1] to a new interval [a, b].

    Args:
        a (float): Lower bound of the target interval.
        b (float): Upper bound of the target interval.
        x (array-like): Quadrature points defined in [-1, 1].
        w (array-like): Corresponding weights for the points x.

    Returns:
        tuple:
            - x_scaled: points mapped to the interval [a, b]
            - w_scaled: weights adjusted for the new interval
   Examples:
        >>> x, w = gaussxw(2.0)
        >>> x_scaled, w_scaled = gaussxwab(0, 2, x, w)
        >>> x
        [0.42264973 1.57735027]
        >>> w
        [1. 1.]

   """
    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w

def funcInt(x):
    """
    Function to be integrated using Gaussian quadrature.

    Args:
        x (float): Input value.

    Returns:
        float: Evaluated function sin(x^2) at x.

    Examples:
        >>> funcInt(1.0)
        0.8414709848
    """   
    return np.sin(x*x)

n_max = 11
n_values = np.arange(1, n_max)
result_values = np.zeros(n_max-1)

for N in range(1,n_max):
    xN, wN = gaussxw(N)
    puntoN, pesoN = gaussxwab(0, np.pi, xN, wN)
    result_values[N-1] = np.sum([pesoN * funcInt(puntoN)])
    print(result_values[N-1])

fig, ax = plt.subplots(dpi=100)

ax.scatter(n_values, result_values)

plt.grid()
plt.ylabel(r'$I= \int^{\pi}_0 dx sen(x^2)$')
plt.xlabel("$N$")
plt.xticks(n_values)
plt.show()
