#
#  주차 요금 계산
#  https://programmers.co.kr/learn/courses/30/lessons/92341
#  Version: Python 3.9.10
#
#  Created by WhiteHyun on 2022/04/16.
#


from math import ceil


def get_time(start_time: str, end_time: str) -> int:
    """
    경과된 시간을 분 단위로 리턴한다.
    """
    start_hour, start_minute = map(int, start_time.split(":"))
    end_hour, end_minute = map(int, end_time.split(":"))
    return end_hour * 60 + end_minute - start_hour * 60 - start_minute


def solution(fees, records):
    # default_time: 기본 주차시간
    # default_fee: 기본 주차요금
    # unit_time: 시간 단위
    # unit_fee: 시간당 요금 단위
    # parking_records: 주차 기록
    # time_records: 총 주차한 시간 기록
    # fee_records: 총 주차 요금 기록
    default_time, default_fee, unit_time, unit_fee = fees
    parking_records = {}
    time_records = {}
    fee_records = {}

    # 주차 시간 계산
    for record in records:
        time, car_number, status = record.split()

        if status == "IN":
            parking_records[car_number] = time
        else:
            total_time = get_time(parking_records[car_number], time)
            parking_records.pop(car_number)
            if car_number not in time_records:
                time_records[car_number] = 0
            time_records[car_number] += total_time

    # 남은 주차 시간 계산
    for car_number, start_time in parking_records.items():
        total_time = get_time(start_time, "23:59")

        if car_number not in time_records:
            time_records[car_number] = 0
        time_records[car_number] += total_time

    # 주차 요금 계산
    for car_number, total_time in time_records.items():
        if total_time - default_time < 0:
            fee_records[car_number] = default_fee
        else:
            fee_records[car_number] = (
                default_fee + ceil((total_time - default_time) / unit_time) * unit_fee
            )
    return list(
        map(lambda values: values[1], sorted(fee_records.items(), key=lambda x: x[0]))
    )


if __name__ == "__main__":

    print(
        solution(
            [180, 5000, 10, 600],
            [
                "05:34 5961 IN",
                "06:00 0000 IN",
                "06:34 0000 OUT",
                "07:59 5961 OUT",
                "07:59 0148 IN",
                "18:59 0000 IN",
                "19:09 0148 OUT",
                "22:59 5961 IN",
                "23:00 5961 OUT",
            ],
        )
    )
