import numpy

def calculation(arr):
    arr = numpy.array(arr)

    mean_calc = numpy.mean(arr, axis=1) 
    var_calc = numpy.var(arr, axis=0)
    std_calc = numpy.std(arr, axis=None)

    return mean_calc, var_calc, std_calc.round(11)

arr = [
    [1, 2],
    [3, 4]
    ]
result = calculation(arr)
print(result)