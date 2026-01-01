import math

def solution(n):
    if n / int(math.sqrt(n)) == int(math.sqrt(n)):
        print(n, int(math.sqrt(n)))
        return int(math.sqrt(n)+1)**2
    else:
        return -1