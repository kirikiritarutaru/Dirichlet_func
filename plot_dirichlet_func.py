import matplotlib.pyplot as plt
import numpy as np
from scipy.special import factorial


def dirichlet_func(x, m, n):
    return np.power(np.cos(factorial(m) * np.pi * x), 2 * n)


if __name__ == '__main__':
    x = np.linspace(-1, 1, 1000000)
    num = 170
    fx = dirichlet_func(x, m=num, n=num)
    plt.scatter(x, fx, s=1)
    plt.show()
