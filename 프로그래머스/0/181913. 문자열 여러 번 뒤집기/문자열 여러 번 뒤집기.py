def solution(my_string, queries):
    answer = []
    for i in my_string:
        answer.append(i)

    for i in queries:
        s, e = i[0], i[1]
        temp = list(answer[s:e+1])
        temp.reverse()
        answer[s:e+1] = temp
        
    return ''.join(answer)