

def calc_i(string):
    """Calculates powers of i in the form 'i^x'."""
    i, power = string.split('^')


def factorial(num):
    '''Provides the result of the given factorial'''
    result = 1
    for x in range(num+1):
        if x == 0:
            pass
        else:
            result = x * result
    print(result)

