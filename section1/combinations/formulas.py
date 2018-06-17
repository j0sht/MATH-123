from math import factorial

def nChooseR(n, r):
    return factorial(n) // (factorial(r)*factorial(n-r))
