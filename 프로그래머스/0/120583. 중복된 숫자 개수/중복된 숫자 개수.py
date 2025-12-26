def solution(array, n):
    result = 0
    for i in array:
        if n == i:
            result += 1
    return result