import math

def solution(n):
    ret = 0
    for i in range(1, n//2+1):
        ret += i
    return (2 * ret)