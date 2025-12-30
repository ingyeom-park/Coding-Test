def solution(numbers):
    temp = ''
    answersheet = {"zero" : 0, "one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight": 8, "nine" : 9}
    answer = []

    for i in numbers:
        temp += i
        for key, value in answersheet.items():
            if temp == key:
                answer.append(str(value))
                temp = ''
                
    result = int("".join(answer))
    return result