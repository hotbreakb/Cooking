#
#  주차 요금 계산
#  https://programmers.co.kr/learn/courses/30/lessons/92341
#  Version: Python 3.8.9
#
#  Created by hotbreakb on 2022/04/15.
#

from typing import OrderedDict


def solution(fees, records):
    car_minutes = getCarMinutes(records)
    car_parking_minutes = OrderedDict(sorted(getParkingMinutes(
        car_minutes).items(), key=lambda car: car[0]))
    car_parking_fees = getCarParkingFees(fees, car_parking_minutes)

    return car_parking_fees


def getCarParkingFees(fees: list, car_parking_mins: dict) -> list:
    basic_min, basic_fee, unit_min, unit_fee = fees

    car_fees = []
    for id, minutes in car_parking_mins.items():
        calced_minutes = minutes - basic_min
        fee = basic_fee
        if calced_minutes <= 0:
            car_fees.append(fee)
        else:
            while calced_minutes > 0:
                fee += unit_fee
                calced_minutes -= unit_min
            car_fees.append(fee)

    return car_fees


def getParkingMinutes(car_mins: dict) -> dict:
    for id, minutes in car_mins.items():
        car_mins[id] = sum([minutes[i]-minutes[i-1]
                            for i in range(len(minutes)-1, -1, -2)])

    return car_mins


def getCarMinutes(records: list) -> dict:
    car_minutes = dict()
    for record in records:
        time, id, move = record.split()
        if id in car_minutes.keys():
            car_minutes[id].append(getMinuts(time))
        else:
            car_minutes[id] = [getMinuts(time)]

    for id, minutes in car_minutes.items():
        if len(minutes) % 2 != 0:
            car_minutes[id].append(getMinuts("23:59"))

    return car_minutes


def getMinuts(time: str) -> int:
    hour, min = map(int, time.split(":"))
    return 60*hour+min


fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT",
           "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))
