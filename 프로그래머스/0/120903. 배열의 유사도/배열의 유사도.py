def solution(s1, s2):
    count = 0

    if len(s1) >= len(s2):
        comp = s2
        non_comp = s1
    else:
        comp = s1
        non_comp = s2

    for i in range(len(comp)):
        if comp[i] in non_comp:
            count += 1
        else:
            pass
    return count