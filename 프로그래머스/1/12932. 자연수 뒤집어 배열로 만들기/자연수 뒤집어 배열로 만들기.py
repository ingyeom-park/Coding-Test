def solution(n):
    n = "".join(reversed(str(n)))
    temp = []
    for num in str(n):
        temp.append(int(num))
    return temp