import numpy

arrayIn = numpy.arange(6)
print(arrayIn)
it = numpy.nditer(arrayIn, op_flags=['readwrite'])
my_sum = 0
for num in it:
    my_sum = my_sum + num
    num[...] = my_sum
print(arrayIn)
