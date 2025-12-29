def solution(my_str, n):
    count = 0
    scattered_str = []
    answer = []
    for i in range(len(my_str)):

        if count > n-1:
            answer.append("".join(scattered_str))
            scattered_str = []
            count = 0

            scattered_str.append(my_str[i])
            count += 1

        else:
            scattered_str.append(my_str[i])
            count += 1 
    if len(scattered_str) > 0:
        answer.append("".join(scattered_str))
    return answer