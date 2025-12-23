def solution(myStr):
    answer = []
    temp = []

    for ch in myStr:
        if ch not in ["a", "b", "c"]:
            temp.append(ch)
        else:
            if temp:
                answer.append("".join(temp))
                temp = []

    if temp:
        answer.append("".join(temp))

    if not answer:
        return ["EMPTY"]

    return answer
