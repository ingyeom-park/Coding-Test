def solution(my_string):
    my_string_splited = my_string.split(" ")
    len_string = len(my_string_splited)
    answer = int(my_string_splited[0])

    print(len_string)
    # 1 3 5 7 9
    for i in range(0, len_string-1, 2):
        #부호자를 식별
        if my_string_splited[i+1] == "+":
            answer += int(my_string_splited[i+2])
        else: #my_string_splited[i] == "-"
            answer -= int(my_string_splited[i+2])
    return answer