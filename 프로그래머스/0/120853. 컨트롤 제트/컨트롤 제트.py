def solution(s):
    command = s.split(" ")

    answer = []

    for i in range(len(command)):

        if command[i] != "Z":
            answer.append(int(command[i]))
        else: # command[i] == "Z"
            answer.pop(-1)

    real_answer = 0
    for i in answer:
        real_answer += i

    return (real_answer)