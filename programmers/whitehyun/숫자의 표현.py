#
#  숫자의 표현
#  https://programmers.co.kr/learn/courses/30/lessons/12924
#  Version: Python 3.9.10
#
#  Created by WhiteHyun on 2022/04/16.
#


def solution(n):
    dp = [1] * (n + 1)

    for i in range(1, n + 1):
        sum_number = i  # 누적합을 구할 변수 선언
        for j in range(i + 1, n + 1):
            sum_number += j  # 연속합
            if sum_number > n:  # 리스트 길이를 넘어서면 1차 for문으로
                break

            dp[sum_number] += 1  # 합한 값을 인덱스로 하여 1 카운트

    return dp[n]

