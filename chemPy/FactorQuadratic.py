import re
import sys


def find_terms(quadratic):
    '''Only works with quadratics that have the form
    "x**2 +/- ax +/- b"'''
    terms = re.search(r'''
    ^(?P<sign1>-?)
    (?P<term1>\w+\^2)
    (?P<sign2>[\+-]?)
    (?P<term2coff>\d+)
    (?P<term2var>\w)
    (?P<sign3>[\+-]?)
    (?P<term3>\d+)$
    ''', quadratic, re.I | re.X | re.M)
    return terms


def attach_signs(terms):
    sign_1 = terms.group('sign1')
    sign_2 = terms.group('sign2')
    term_2_coff = float(sign_2 + terms.group('term2coff'))
    term_2_var = terms.group('term2var')
    sign_3 = terms.group('sign3')
    term_3 = float(sign_3 + terms.group('term3'))

    if sign_1 == '-':
        if sign_2 == '+':
            term_2_coff = -term_2_coff
        else:
            term_2_coff = abs(term_2_coff)
        if sign_3 == '+':
            term_3 = -term_3
        else:
            term_3 = abs(term_3)
    return [term_2_coff, term_2_var, term_3]


def calc_answer(terms):
    if abs(terms[0]) < abs(terms[2]):
        high_num = abs(terms[2]) + 1
    elif abs(terms[0]) > abs(terms[2]):
        high_num = abs(terms[0]) + 1
    else:
        high_num = abs(terms[2]) + 1

    for a in range(int(high_num)):
        for b in range(int(high_num)):
            if float(a * b) == abs(terms[2]):
                if float(a + b) == terms[0]:
                    return [a, b, terms[1]]
                elif float(-a + b) == terms[0]:
                    return [-a, b, terms[1]]
                elif float(a - b) == terms[0]:
                    return [a, -b, terms[1]]
                elif float(-a - b) == terms[0]:
                    return [-a, -b, terms[1]]


def format_answer(ans_nums):
    if ans_nums[0] * -1 == abs(ans_nums[0]):
        eq1 = "({} - {})".format(ans_nums[2], abs(ans_nums[0]))
    else:
        eq1 = "({} + {})".format(ans_nums[2], ans_nums[0])
    if ans_nums[1] * -1 == abs(ans_nums[1]):
        eq2 = "({} - {})".format(ans_nums[2], abs(ans_nums[1]))
    else:
        eq2 = "({} + {})".format(ans_nums[2], ans_nums[1])
    return "{}{}".format(eq1, eq2)


def main(quadratic):
    str_trms = find_terms(quadratic)
    num_trms = attach_signs(str_trms)
    ans_nums = calc_answer(num_trms)
    answer = format_answer(ans_nums)
    print(answer)


if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except IndexError:
        print('Need to add a quadratic as an argument.\n')
