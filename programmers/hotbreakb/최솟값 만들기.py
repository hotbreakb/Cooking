#
#  최솟값 만들기
#  https://programmers.co.kr/learn/courses/30/lessons/12941
#  Version: Python 3.8.9
#
#  Created by hotbreakb on 2022/04/12.
#

def solution(A, B):
    answer = 0

    A = sorted(A)
    B = sorted(B, reverse=True)

    for i in range(len(A)):
        answer += A[i]*B[i]

    return answer
