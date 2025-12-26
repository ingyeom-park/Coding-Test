def solution(rsp):
    result = []

    for i in rsp:
        if i == "0":
            result.append("5")
        elif i == "2":
            result.append("0")
        elif i == "5":
            result.append("2")
    answer = "".join(result)
    return answer