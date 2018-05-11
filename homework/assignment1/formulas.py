def sumToN(n):
    return (n*(n+1)) // 2

def evenSum(n):
    return n*(n+1)

def oddSum(n):
    return sumToN(2*n) - evenSum(n)

def sumSquares(n):
    return (n*(n+1)*((2*n)+1)) // 6

def evenSquares(n):
    return 4 * sumSquares(n)

def oddSquares(n):
    return sumSquares(2*n) - evenSquares(n)

# Formula for Q1c
def formula(n):
    return oddSquares(n) - evenSquares(n)
