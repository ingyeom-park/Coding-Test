def solution(numbers, hand):
    numbers_pos = {
    1 : (1, 1),
    2 : (1, 2),
    3 : (1, 3), 
    4 : (2, 1),
    5 : (2, 2),
    6 : (2, 3),
    7 : (3, 1), 
    8 : (3, 2),
    9 : (3, 3),
    0 : (4, 2)
}
    # 왼손으로 누르면 L, 오른손으로 누르면 R을 차례대로 저장
    result = []

    left_pos = (4, 1)
    right_pos = (4, 3)

    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            left_pos = numbers_pos[i]
            result.append("L")

        elif i == 3 or i == 6 or i == 9:
            right_pos = numbers_pos[i]
            result.append("R")

        elif i == 2 or i == 5 or i == 8 or i == 0:
            target_pos = numbers_pos[i]
            if (abs(target_pos[0] - left_pos[0]) + abs(target_pos[1] - left_pos[1])) < (abs(target_pos[0] - right_pos[0]) + abs(target_pos[1] - right_pos[1])):
                left_pos = numbers_pos[i]
                result.append("L")
            elif (abs(target_pos[0] - left_pos[0]) + abs(target_pos[1] - left_pos[1])) > (abs(target_pos[0] - right_pos[0]) + abs(target_pos[1] - right_pos[1])):
                right_pos = numbers_pos[i]
                result.append("R")
            elif (abs(target_pos[0] - left_pos[0]) + abs(target_pos[1] - left_pos[1])) == (abs(target_pos[0] - right_pos[0]) + abs(target_pos[1] - right_pos[1])):
                if hand == "left":
                    left_pos = numbers_pos[i]
                    result.append("L")
                else:
                    right_pos = numbers_pos[i]
                    result.append("R")

    result = ''.join(result)

    return result