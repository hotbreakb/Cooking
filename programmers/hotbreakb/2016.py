from datetime import datetime


def solution(a, b):
    YEAR = 2016
    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    day = datetime.strptime(f"{YEAR}-{a}-{b}", "%Y-%m-%d").weekday()
    return days[day]


print(solution(5, 24))
