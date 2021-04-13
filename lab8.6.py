import matplotlib.pyplot
import numpy

t = numpy.linspace(0, 2 * numpy.pi, 100)
matplotlib.pyplot.figure(figsize=(4, 4))
matplotlib.pyplot.plot(numpy.sin(2 * t), numpy.cos(3 * t))
matplotlib.pyplot.show()
