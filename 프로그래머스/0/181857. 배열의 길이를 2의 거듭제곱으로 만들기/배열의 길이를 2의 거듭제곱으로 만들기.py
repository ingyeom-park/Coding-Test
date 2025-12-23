def solution(arr):
    n = 0
    while 2**n < len(arr):
        n += 1

    for cnt in range(2**(n)-len(arr)):
        arr.append(0)
    return arr