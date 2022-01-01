#
#  13305번: 주유소
#  https://www.acmicpc.net/problem/13305
#  Version: Python 3.9.7
#
#  Created by white on 2022/01/01.
#


from sys import stdin

read = stdin.readline

if __name__ == "__main__":
    city_count = int(read())
    distance_list = list(map(int, read().split()))
    city_price_list = list(map(int, read().split()))
    total_price = 0
    person = 0  # 사람의 현재 위치
    while person != city_count:  # 사람이 도시 끝까지 갈 때 까지 반복

        next_city = person + 1  # 다음 도시

        # 다음 도시의 기름 가격이 현 위치보다 작아질 때 까지 반복
        while (
            next_city != city_count  # 인덱스 에러 처리
            and city_price_list[next_city] > city_price_list[person]
        ):
            next_city += 1

        # 현위치의 기름가격이 이후에 갈 도시들 중 가장 싼 곳일 경우
        if next_city == city_count:
            # 현위치에서 끝까지의 거리만큼 기름 충당
            total_price += sum(distance_list[person:]) * city_price_list[person]
            break
        else:
            # 현위치에서 기름값이 싼 도시까지의 거리만큼만 기름 충당 후 이동
            total_price += (
                sum(distance_list[person:next_city]) * city_price_list[person]
            )
            person = next_city  # 위치 이동
    print(total_price)

