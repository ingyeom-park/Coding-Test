def solution(array):
    dick = {}

    for i in array:
        if i not in dick:
            dick[i] = 1
        else: # i in dick:
            dick[i] += 1

    max_value = 0
    for value in dick.values():
        if value > max_value:
            max_value = value

    temp = []
    for key, value in dick.items():
        if value == max_value:
            temp.append(key)

    if len(temp) != 1:
        return -1
    else:
        return temp[0]