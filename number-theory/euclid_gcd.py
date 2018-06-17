def gcd(n1, n2):
    largest = n1 if n1 > n2 else n2
    smallest = n2 if largest == n1 else n1
    remainder = smallest
    the_gcd = remainder
    while remainder != 0:
        factor = largest // smallest
        remainder = largest - (smallest*factor)
        largest = smallest
        smallest = remainder
    return largest
