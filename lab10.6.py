import matplotlib.pyplot
import numpy
import scipy.spatial

points = numpy.random.rand(10, 2)
vor = scipy.spatial.Voronoi(points)
scipy.spatial.voronoi_plot_2d(vor)

matplotlib.pyplot.show()
