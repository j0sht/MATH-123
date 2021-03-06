def sumToN(n):
    return (n*(n+1)) // 2

def evenSum(n):
    return 2 * sumToN(n)

def oddSum(n):
    return sumToN(2*n) - evenSum(n)

def sumSquares(n):
    return (n*(n+1)*((2*n)+1)) // 6

def evenSquares(n):
    return 4 * sumSquares(n)

def oddSquares(n):
    return sumSquares(2*n) - evenSquares(n)

def sumCubes(n):
    return ((n**2)*((n+1)**2)) // 4 # same as [sumToN(n)]^2 (question 2)

def evenCubes(n):
    return 8 * sumCubes(n)

def oddCubes(n):
    return sumCubes(2*n) - evenCubes(n)

def q1b():
    return 3 * (sumToN(333) - sumToN(33))

def q1c(n=250):
    return oddSquares(n) - evenSquares(n)

if __name__ == "__main__":
    print("102 + 105 + 108 + ... + 999 =", q1b())
    print("1^2 - 2^2 + 3^2 - 4^2 + 5^2 - 6^2 + ... + 499^2 - 500^2 =", q1c())
