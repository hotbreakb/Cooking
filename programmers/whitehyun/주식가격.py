#
#  주식가격
#  https://programmers.co.kr/learn/courses/30/lessons/42584
#  Version: Python 3.9.10
#
#  Created by WhiteHyun on 2022/04/12.
#


def solution(prices):
    answer = []
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i] > prices[j]:
                answer.append(j - i)
                break
        else:
            answer.append(j - i)
    return answer


print(solution([1, 2, 3, 2, 3]))

