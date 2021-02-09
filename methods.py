##
## EPITECH PROJECT, 2021
## 105torus (Workspace)
## File description:
## methods
##

from my_math import my_deg, my_deriv
from torus_utils import error_handling, my_print, secant_call

def dichotomy(a, n, inter_min, inter_max):
    z = 0
    xm = (inter_min + inter_max) / 2

    while abs(my_deg(a, xm)) > (10 ** -n) and z < 300:
        xm = (inter_min + inter_max) / 2
        if inter_min + inter_max == 0:
            exit(84)
        if my_deg(a, inter_min) * my_deg(a, xm) == 0    \
            and my_deg(a, inter_min) * my_deg(a, xm) == 1:
            exit(84)
        if my_deg(a, inter_min) * my_deg(a, xm) < 0:
            inter_max = xm
            my_print(n, inter_max)
        else:
            inter_min = xm
            my_print(n, inter_min)
        z += 1
    return

def newton(a, n, inter):
    z = 0

    while abs(my_deg(a, inter)) > 10 ** -n and z < 300:
        my_print(n, inter)
        if my_deriv(a, inter) == 0 or my_deg(a, inter) == 0:
            exit(84)
        inter = inter - (my_deg(a, inter) / my_deriv(a, inter))
        z += 1
    my_print(n, inter)
    return

def secant(a, n, inter_min, inter_max):
    z = 0
    f = [my_deg(a, inter_max), my_deg(a, inter_max) - my_deg(a, inter_min)]
    if f[0] == 0 or f[1] == 0:
        exit(84)
    xm = inter_max - (f[0] / f[1])
    my_print(n, xm);
    inter_min, inter_max = inter_max, xm

    while abs(f[0]) / abs(f[1]) > 10 ** -n and z < 300:
        f[0] = (my_deg(a, inter_max)) * (inter_max - inter_min)
        f[1] = (my_deg(a, inter_max)) - (my_deg(a, inter_min))
        if f[0] == 0 or f[1] == 0:
            exit(84)
        xm = inter_max - (f[0] / f[1])
        my_print(n, xm);
        inter_min, inter_max = inter_max, xm
        z += 1
    return
