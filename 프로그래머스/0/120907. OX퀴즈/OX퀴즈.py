def solution(quiz):
    result = []
    for i in quiz:
        mod = i.split(" ")
        
        print(mod)
        # X (수식) Y = Z 구성u
        if mod[1] == "+" and (int(mod[0])+int(mod[2])==int(mod[4])):
            result.append("O")
        elif mod[1] == "-" and (int(mod[0])-int(mod[2])==int(mod[4])):
            result.append("O")
        else:
            result.append("X")

    return result