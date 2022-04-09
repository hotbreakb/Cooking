#
#  두 개 뽑아서 더하기
#  https://programmers.co.kr/learn/courses/30/lessons/68644
#  Version: Python 3.9.10
#
#  Created by WhiteHyun on 2022/04/08.
#


def solution(numbers):
    answer = set()
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            answer.add(numbers[i] + numbers[j])

    return sorted(answer)


if __name__ == "__main__":
    for number in ([2, 1, 3, 4, 1], [5, 0, 2, 7]):
        print(solution(number))
