def solution(arr):
    row_arr = len(arr)
    col_arr = len(arr[0])
    print(row_arr, col_arr)

    if row_arr > col_arr:
        diff = row_arr-col_arr
        for cnt in range(len(arr)):
            for i in range(diff):
                arr[cnt].append(0)
    elif row_arr < col_arr:
        diff = col_arr-row_arr
        for cnt in range(diff):
            arr.append([0]*col_arr)

    return arr
