def solution(numbers, direction):
    if direction == "left":
        numbers.append(numbers[0])
        del numbers[0]
    else: #direction == "right"
        numbers.insert(0, numbers[-1])
        numbers.pop()
    return numbers