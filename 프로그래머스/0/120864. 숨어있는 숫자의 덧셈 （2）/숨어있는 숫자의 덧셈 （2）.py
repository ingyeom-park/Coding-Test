def solution(my_string):
    temp = []
    result = 0

    for i in range(len(my_string)):

        # my_string[i]이 숫자면
        if my_string[i].isdigit() == True:

            # temp에 그 숫자 저장
            temp.append(my_string[i])

            # 만약 문자열 끝에 다다른거였다면
            if i == len(my_string) - 1:

                # result에 지금까지의 수 모두 우겨넣기
                result += int("".join(temp))

        # my_string[i]이 문자면
        else:

            # 일전에 temp에 저장해놓은 숫자가 있다면
            if len(temp) > 0:

                # 이제 저장된 숫자들을 모두 자연수로 치환, result에 저장
                result += int("".join(temp))

                # 임시변수인 temp 초기화
                temp = []

            # temp가 텅텅 비어있었다면, 일전에도 문자, 지금도 문자.
            else:
                pass
            
    return result