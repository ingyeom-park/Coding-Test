def solution(numbers, hand):
    # 번호마다의 좌표를 딕셔너리 형태로 저장
    num_pos = {
        1 :   (0, 0), 
        2 :   (0, 1),
        3 :   (0, 2),
        4 :   (1, 0), 
        5 :   (1, 1),
        6 :   (1, 2),
        7 :   (2, 0),
        8 :   (2, 1),
        9 :   (2, 2),
        "*": (3, 0),
        0 :   (3, 1),
        "#": (3, 2)
    }

    # 왼손과 오른손의 시작 좌표 설정
    left_pos = num_pos["*"]
    right_pos = num_pos["#"]

    # 결과를 담을 result 리스트
    result = []

    # numbers 배열의 값을 하나씩 순회
    for x in numbers:
        
        # x가 왼손으로 눌러야 하는 키일 경우
        if x in [1, 4, 7]:
            left_pos = num_pos[x]
            result.append("L")
        
        # x가 오른손으로 눌러야 하는 키일 경우
        elif x in [3, 6, 9]:
            right_pos = num_pos[x]
            result.append("R")
        
        # x가 중간에 있어 판가름을 해야 하는 경우
        else: # x == [2, 5, 8, 0]
            
            # 왼손과 오른손의 키(x) 간의 절대 거리를 계산
            left_diff = abs(num_pos[x][0]-left_pos[0]) + abs(num_pos[x][1]-left_pos[1])
            right_diff = abs(num_pos[x][0]-right_pos[0]) + abs(num_pos[x][1]-right_pos[1])
            
            # 왼손의 차이가 더 작을 경우 (왼손이 더 가까움)
            if left_diff < right_diff:
                left_pos = num_pos[x]
                result.append("L")
            
            # 오른손의 차이가 더 작을 경우 (오른손이 더 가까움)  
            elif left_diff > right_diff:
                right_pos = num_pos[x]
                result.append("R")
            
            # 둘의 거리가 같을 경우
            elif left_diff == right_diff:
                
                # 왼손잡이인지 오른손잡이인지로 판가름
                if hand == "left":
                    left_pos = num_pos[x]
                    result.append("L")
                    
                elif hand == "right":
                    right_pos = num_pos[x]
                    result.append("R")
                    
    # 결과를 join 함수를 통해 보기좋게 치환, return       
    return "".join(result)