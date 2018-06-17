def gcd(n1, n2):
    largest = n1 if (n1 > n2) else n2
    smallest = n2 if (n1 == largest) else n1
    remainder = smallest
    while remainder != 0:
        factor = largest // smallest
        remainder = largest - (smallest*factor) # == (largest % smallest)
        largest = smallest
        smallest = remainder
    return largest
