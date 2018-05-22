from math import factorial

# Permutation (Linear Arrangment -> Non-repeating)
# Ex) Class of ten students, choose 5 to be seated in front row,
#     how many such arrangements are possible? nChooseR(10, 5) = 30,240
def nChooseR(n, r):
    return factorial(n) // factorial(n-r)

# Linear Arrangement -> Repeating
def nRTimes(n, r):
    return n**r

