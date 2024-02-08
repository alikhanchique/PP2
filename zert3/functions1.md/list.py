import math
def Read(n):
    lst = []
    for i in range(0, n):
        ele = int(input())
        lst.append(ele)
    r = Create(lst, n)
    if r == 0:
        print("There are no prime numbers in this list")
    else:
        print("The prime numbers in this list are: ", r)
def Create(lst, n):
    primes = []
    for i in lst:
        p = i
        if Prime(p) == True:
            primes.append(p)
    return primes


def Prime(p):
    if p > 1:
    # Iterate from 2 to n / 2
        for i in range(2, int(p/2)+1):
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
            if (p % i) == 0:
                return False
            else:
                return True
 

n = int(input())
Read(n)