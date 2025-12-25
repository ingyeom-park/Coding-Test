def solution(array, height):
    count = 0

    for num in range(len(array)):
        if height < array[num]:
            count += 1
    return count