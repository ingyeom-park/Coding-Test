def solution(my_string):
    check_dick = {}
    answer = []
    for letter in my_string:
        if letter not in check_dick:
            check_dick[letter] = 1
            answer.append(letter)
        elif letter in check_dick:
            pass
    return "".join(answer)