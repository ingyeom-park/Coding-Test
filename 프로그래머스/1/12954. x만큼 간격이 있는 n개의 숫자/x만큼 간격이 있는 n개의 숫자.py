def solution (x, n):
    answer = []
    digit = x
    for i in range(n):
        answer.append(digit)
        digit += x
    return answer