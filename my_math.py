##
## EPITECH PROJECT, 2021
## 105torus
## File description:
## my_math
##

def my_deg(c, x):
    res = c[4] * x**4 + c[3] * x**3 + c[2] * x**2 + c[1] * x + c[0]

    return res

def my_deriv(c, x):
    res = 4 * c[4] * x**3 + 3 * c[3] * x**2 + 2 * c[2] * x + c[1]

    return res
