def solution(fees, records):
    import math

    base_time, base_fee, unit_time, unit_fee = fees
    parking_dict = {}
    answer = {}

    # 1. 차량별 기록 저장
    for record in records:
        time, car_number, status = record.split()
        h, m = time.split(":")
        minutes = int(h) * 60 + int(m)
        time_status = f"{minutes}-{status}"

        if car_number not in parking_dict:
            parking_dict[car_number] = []

        parking_dict[car_number].append(time_status)

    # 2. 차량별 누적 시간 계산
    for car in parking_dict:
        record_list = parking_dict[car]

        if len(record_list) % 2 == 1:
            record_list.append("1439-OUT")

        total_time = 0
        for i in range(0, len(record_list), 2):
            in_time = int(record_list[i].split("-")[0])
            out_time = int(record_list[i+1].split("-")[0])
            total_time += out_time - in_time

        # 3. 요금 계산
        if total_time <= base_time:
            answer[car] = base_fee
        else:
            extra = total_time - base_time
            answer[car] = base_fee + math.ceil(extra / unit_time) * unit_fee

    # 4. 차량번호 오름차순 결과 반환
    return [answer[car] for car in sorted(answer)]
