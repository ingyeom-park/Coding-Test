def solution(i, j, k):
    sum = "-"
    num_list = [x for x in range(i, j+1)]
    for i in num_list:
        sum += str(i)
    return sum.count(str(k))