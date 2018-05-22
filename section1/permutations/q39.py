from math import factorial

def q39():
    for a in range(0,10):
        for b in range(0,10):
            for c in range(0,10):
                num = a*100 + b*10 + c
                f_sum = factorial(a) + factorial(b) + factorial(c)
                if num == f_sum:
                    print(num," = ",a,"! + ",b,"! + ",c,"!",sep='')
                    return
    print("Did not find number")

if __name__ == "__main__":
    q39()
