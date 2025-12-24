def solution(participant, completion):
    people_dict = {}
    # 참가자들의 정보를 처리할 변수
    # k = 참가자 이름
    # v = 이름에 대한 참가자 수

    # 입력으로 주는 참가자 명단을 보면서 정리: 순회 > for문
    for p in participant:
        if p in people_dict: #기등록 이름
            people_dict[p] += 1
        else:                #t신규등록 이름
            people_dict[p] = 1

    #완주자 명단을 순회하기
    for c in completion:
        # 완주자 이름 1명씩 불러다가 할 것.
        # 기준: 이름에 대한 사람 수(v쪽 값이 1이냐, 2냐 등)

        # 1명이 등록되어있고, 그 1명이 완주했다면: 완전 제명
        if people_dict[c] == 1: del people_dict[c]
        # 아직 동명이인 2명 이상 남아있다면?
        else: people_dict[c] -= 1

        # 이렇게 계속 순회 순회 순회 한다면, people_dict의 키 값에 남아있게 된다. 
    
    answer = list(people_dict.keys())[0]
    return answer