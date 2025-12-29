def solution(order):
    count = 0
    list_order = [int(x) for x in str(order)]
    for i in list_order:
        if i == 3 or i == 6 or i == 9:
            count += 1
            
    return count