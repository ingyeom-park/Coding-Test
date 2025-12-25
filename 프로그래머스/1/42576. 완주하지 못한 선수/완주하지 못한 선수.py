def solution(participant, completion):
    # 1. 두 리스트를 모두 정렬합니다.
    participant.sort()
    completion.sort()
    
    # 2. 앞에서부터 하나씩 비교합니다.
    for i in range(len(completion)):
        # 만약 순서가 맞지 않는 이름이 나온다면, 그 사람이 완주하지 못한 사람입니다.
        if participant[i] != completion[i]:
            return participant[i]
            
    # 3. 끝까지 다 똑같다면, 마지막 남은 한 사람이 범인입니다.
    return participant[-1]