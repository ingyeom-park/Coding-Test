import math
def solution(n, m):
    return int(math.factorial(n)/(math.factorial(n-m)*math.factorial(m)))