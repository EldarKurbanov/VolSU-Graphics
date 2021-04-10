import numpy


def get_random_dimension():
    return numpy.random.randint(low=2, high=7)


width = get_random_dimension()
height = get_random_dimension()
randomArray = numpy.random.rand(height, width)
print("random array:\n", randomArray)
maxSum = 0
maxSlice = 0
for a in range(0, height - 1):
    b = 0
    for b in range(0, width - 1):
        currSlice = randomArray[a:a+2, b:b+2]
        currSum = currSlice.sum()
        if maxSum < currSum:
            maxSum = currSum
            maxSlice = currSlice
print("maxSlice:\n", maxSlice)
