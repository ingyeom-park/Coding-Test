
def solution(num, total):
    n = int((total-sum(range(1, num)))/num)
    return [n+i for i in range(num)]