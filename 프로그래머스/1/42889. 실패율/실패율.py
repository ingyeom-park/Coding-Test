def solution(n, stages):
    answer = {}
    player_count = len(stages)

    for cnt in range(1, n+1):
        if player_count == 0:
            failure = 0
        else:
            failure = stages.count(cnt)/player_count
        answer[cnt] = failure
        player_count -= stages.count(cnt)

    result = sorted(answer, key=lambda x: answer[x], reverse=True)
    return result