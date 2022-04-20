#
#  같은 숫자는 싫어
#  https://programmers.co.kr/learn/courses/30/lessons/12906
#  Version: Python 3.8.9
#
#  Created by hotbreakb on 2022/04/10.
#

def solution(arr):
    answer = [arr[0]]

    for i in range(1, len(arr)):
        if answer[-1] == arr[i]:
            continue
        answer.append(arr[i])
    return answer
