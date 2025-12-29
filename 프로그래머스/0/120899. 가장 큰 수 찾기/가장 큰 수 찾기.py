def solution(array):
    sort_array = sorted(array)
    max = sort_array[-1]
    idx = 0

    for i in range(len(array)):
        if array[i] == max:
            idx = i
            break
    return (max, idx)