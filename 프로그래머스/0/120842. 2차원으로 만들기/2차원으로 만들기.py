def solution(num_list, n):
    count = 0
    result = []
    temp = []
    for i in num_list:
        temp.append(i)
        count += 1
        if count == n:
            result.append(temp)
            count = 0
            temp = []
    return result