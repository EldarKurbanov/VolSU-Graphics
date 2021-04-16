import numpy
import matplotlib.pyplot

max_iterations = 500
lenX = lenY = 20
delta = 1

TTop = 100
TBottom = 0
TLeft = 0
TRight = 30
TGuess = 30

color_interpolation = 50
colourMap = matplotlib.pyplot.cm.jet
#colourMap = plt.cm.coolwarm

X, Y = numpy.meshgrid(numpy.arange(0, lenX), numpy.arange(0, lenY))

T = numpy.empty((lenX, lenY))
T.fill(TGuess)

T[(lenY-1):, :] = TTop
T[:1, :] = TBottom
T[:, (lenX-1):] = TRight
T[:, :1] = TLeft

for iteration in range(0, max_iterations):
    for i in range(1, lenX-1, delta):
        for j in range(1, lenY-1, delta):
            T[i, j] = 0.25 * (T[i+1][j] + T[i-1][j] + T[i][j+1] + T[i][j-1])

matplotlib.pyplot.title("Contour of Temperature")
matplotlib.pyplot.contourf(X, Y, T, color_interpolation, cmap=colourMap)
matplotlib.pyplot.colorbar()
matplotlib.pyplot.show()
