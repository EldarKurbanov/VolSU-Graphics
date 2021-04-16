import numpy
import matplotlib.pyplot
import math

N = 25
n = numpy.arange(1, N+1)
b = numpy.array([1.0/(k**2) for k in range(1, N+1)])
M = int(math.log(N+1))
S = numpy.array([b[k-2:(k+1)-2].sum() for k in range(1, M)])

matplotlib.pyplot.plot(n, b, '.', label=r'$u_n=\frac{1}{n^2}$')
matplotlib.pyplot.plot(S, '.', label=r'$S_p= \sum_{k=p}^{p}u_k$')

matplotlib.pyplot.legend()
matplotlib.pyplot.grid(True)
matplotlib.pyplot.show()
