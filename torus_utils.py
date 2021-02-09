##
## EPITECH PROJECT, 2021
## 105torus (Workspace)
## File description:
## torus_utils
##

def error_handling(n):
    print("USAGE")
    print("    ./105torus opt a0 a1 a2 a3 a4 n")
    print("DESCRIPTION")
    print("    opt     method option:")
    print("                1 for the bisection method")
    print("                2 for Newton's method")
    print("                3 for the secant method")
    print("    a[0-4]  coefficients of the equation")
    print("    n       precision (the application of the polynomial")
    print("            to the solution should be smaller than 10^-n)")
    exit(n)

def my_print(n, xm):
    if float(str("%." + str(n) + "f") % (xm)) == xm:
        print("x =", xm)
    else:
        print(str("x = %." + str(n) + "f") % (xm))
    return

def secant_call(inter_min, inter_max, n, f):
    if f[0] == 0 or f[1] == 0:
        error_handling(84)
    xm = inter_max - (f[0] / f[1])
    my_print(n, xm)
    return xm
