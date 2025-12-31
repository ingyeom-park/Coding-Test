def solution(my_string, alp):
    # 답안으로 제출할 리스트 만들기
    answer = []
    
    # my_string의 요소들을 for문(반복문) 돌리기
    # letter라는 이름으로 하나씩 꺼낸다는 뜻
    # 굳이 letter 아니어도 됌. i, j, 아무거나 이름붙여도 됌.
    for letter in my_string:
    
        # letter (my_string의 철자 하나씩)을 검사할거임.
        
        # 만약 letter가 alp랑 같은 철자(alphabet)라면?
        if letter == alp:
            # 아까만든 answer 리스트에 넣긴 넣는데, 대문자로 바꿔서 넣을거임.
            answer.append(letter.upper())
        # 만약 letter가 alp랑 다른 철자라면?
        else: #if letter != alp:
            # 그냥 소문자인 상태로 넣어 (대문자로 변환하지 않고 넣어)
            answer.append(letter)
    
    # 이제 answer을 return하면 됌.
    # 근데 그냥 answer을 return 혹은 print 해보면 다음과 같음
    # ['P', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'e', 'r', 's']
    
    # 이대로 제출하면 답안이 아님. Programmers 라고 제출해야 함.
    # 그래서 .join()을 사용함
    # "".join(answer)의 뜻:
        # .join(): 하나의 문자열로 만들거임.
        # .join(answer): answer을 하나의 문자열로 만들거임.
        # "".join(answer): ""를 기준으로 answer을 하나의 문자열로 만들거임.
        
        # ""는 구분자를 뜻함.
        # ","라고 썼으면 , 라는 철자를 기준으로 하나의 문자열로 만드는거임.
        # ""는 기준 없이 합친다는 뜻
    return "".join(answer)