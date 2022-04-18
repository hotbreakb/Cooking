#
#  n^2 배열 자르기
#  https://programmers.co.kr/learn/courses/30/lessons/87390
#  Version: Python 3.9.10
#
#  Created by WHiteHyun on 2022/04/16.
#


def solution(n: int, left: int, right: int) -> list:
    matrix = []  # 빈 배열 설정
    for row in range(n):
        # n * (row+1) => 2차원 배열의 1+row행을 1차원행렬로 변환하였을 때 인덱스 값
        # 즉, left라는 index가 row행에 없다면 다시 반복
        if left > n * (row + 1):
            continue

        for col in range(n):
            # n * row + col => row행 col열의 값을 1차원 행렬로 변환하였을 때 인덱스 값
            # 즉, left라는 index가 row행 col열에 없다면 다시 반복
            if left > n * row + col:
                continue

            # ===================================
            # 이 쪽으로 코드가 넘어왔다면 left값을 찾은 것!
            # ===================================

            # 만약 right값을 초과했다면 반복문을 끝내자.
            if n * row + col > right:
                break

            # left와 right 사이의 값을 넣을 차례!
            if col < row:
                matrix.append(row + 1)
            else:
                matrix.append(col + 1)
        else:
            continue
        break

    return matrix
