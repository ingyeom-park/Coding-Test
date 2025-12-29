def solution(emergencry):
    temp = sorted(emergencry, reverse=True)
    temp_dict = {} # {100: 1, 30: 2, 23: 3, 10: 4, 6: 5}
    for i in range(len(temp)):
        temp_dict[temp[i]] = i+1

    answer = []
    for i in range(len(emergencry)):

        for k, v in temp_dict.items():
            if emergencry[i] == k:
                answer.append(v)
    return answer