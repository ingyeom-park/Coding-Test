def solution(keyinput, board):
    start = [0, 0]
    for command in keyinput:
        if command == "up":
            if start[1] >= board[1]//2:
                print("passed")
                pass
            else:
                start[1] += 1

        elif command == "down":
            if start[1] <= -(board[1]//2):
                print("passed")
                pass
            else:
                start[1] -= 1

        elif command == "left":
            if start[0] <= -(board[0]//2):
                print("passed")
                pass
            else:
                start[0] -= 1

        elif command == "right":
            if start[0] >= board[0]//2:
                print("passed")
                pass
            else:
                start[0] += 1
    return start