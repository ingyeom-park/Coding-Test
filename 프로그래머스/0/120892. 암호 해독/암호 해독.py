def solution(cipher, code):
    answer = []
    count = code

    for i in cipher:
        answer.append(cipher[count-1])
        count += code
        print(count)
        if count > len(cipher):
            break

    return "".join(answer)