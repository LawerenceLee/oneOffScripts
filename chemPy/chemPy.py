"""ChemPy

created by: Zach Owens
"""


def convert_unit(num, num_unit, desired_unit):
    num_unit = num_unit.upper()
    desired_unit = desired_unit.upper()

    def c_to_f(num):
        return num * (9 / 5) + 32

    def f_to_c(num):
        return (num - 32) * (5 / 9)

    def k_to_c(num):
        return num - 273.15

    def c_to_k(num):
        return num + 273.15

    if num_unit == "C":
        if desired_unit == "F":
            return c_to_f(num)
        elif desired_unit == "K":
            return c_to_k(num)
        else:
            raise ValueError('Input is not correct.')
    elif num_unit == "F":
        if desired_unit == "C":
            return f_to_c(num)
        elif desired_unit == "K":
            return c_to_k(f_to_c(num))
        else:
            raise ValueError('Input is not correct.')
    elif num_unit == "K":
        if desired_unit == "C":
            return k_to_c(num)
        elif desired_unit == "F":
            return c_to_f(k_to_c(num))
        else:
            raise ValueError('Input is not correct.')
    else:
        raise ValueError('Input is not correct.')
