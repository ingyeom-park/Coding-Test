def solution(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    return True if n % sum == 0 else False