#
#  주식가격
#  https://programmers.co.kr/learn/courses/30/lessons/42584
#  Version: Python 3.8.9
#
#  Created by hotbreakb on 2022/04/12.
#

def solution(prices):
    stack = []
    answer = [0]*len(prices)

    for i, p in enumerate(prices):
        if not stack or stack[-1][1] <= p:
            stack.append((i, p))
        else:
            while stack and stack[-1][1] > p:
                poped = stack.pop()
                answer[poped[0]] = i-poped[0]
            stack.append((i, p))

    for i in range(len(stack)):
        answer[stack[i][0]] = len(prices)-1-stack[i][0]

    return answer


prices = [1, 2, 3, 4, 5]
print(solution(prices))
