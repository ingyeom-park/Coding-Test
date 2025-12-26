def solution(box, n):
    arr = []
    for i in range(len(box)):
        arr.append(box[i] // n)
    return arr[0]*arr[1]*arr[2]