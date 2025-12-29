def solution(s):
    s_list = [x for x in s]
    s_dict = {}
    answer = []

    for i in s:
        if i not in s_dict:
            s_dict[i] = 1
        else: # i in s_dict:
            s_dict[i] += 1

    for k, v in s_dict.items():
        if v == 1:
            answer.append(k)

    return "".join(sorted(answer))
