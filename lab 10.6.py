import matplotlib.pyplot
import numpy
import scipy.spatial

points = numpy.random.rand(10, 2)
vor = scipy.spatial.Voronoi(points)
scipy.spatial.voronoi_plot_2d(vor)
scipy.spatial.voronoi_plot_2d(vor, show_vertices=False, line_colors='orange',
                              line_width=3, line_alpha=0.6, point_size=2)
matplotlib.pyplot.show()
