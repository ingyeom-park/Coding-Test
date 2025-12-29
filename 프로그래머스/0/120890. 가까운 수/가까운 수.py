def solution(array, n):
    arr_dict = {}
    for i in array:
        dist = abs(n-i)
        if dist not in arr_dict:
            arr_dict[dist] = [i]
        else:
            arr_dict[dist].append(i)
    for j in arr_dict:
        arr_dict[j].sort()
    
    sort_dict = sorted(arr_dict.items())
    return sort_dict[0][1][0] 