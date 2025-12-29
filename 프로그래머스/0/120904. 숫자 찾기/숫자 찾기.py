def solution(num, k):
    list_num = [int(i) for i in str(num)]
    result = 0
    
    for i in range(len(list_num)):
        if list_num[i] == k:
            result = i+1
            break
    if result == 0:
        result = -1
    
    return result
    
    