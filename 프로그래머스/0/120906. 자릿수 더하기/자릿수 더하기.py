def solution(n):
    sum = 0
    str_n = str(n)

    for i in str_n:
        sum += int(i)
    return (sum)