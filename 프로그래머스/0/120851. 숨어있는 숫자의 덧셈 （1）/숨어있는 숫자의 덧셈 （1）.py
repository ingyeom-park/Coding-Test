def solution(my_string):
    sum = 0
    for i in my_string:
        if i.isdigit() == True:
            sum += int(i)
    return sum