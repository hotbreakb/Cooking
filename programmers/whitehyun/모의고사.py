#
#  모의고사
#  https://programmers.co.kr/learn/courses/30/lessons/42840
#  Version: Python 3.9.10
#
#  Created by WhiteHyun on 2022/04/08.
#


from math import ceil


def solution(answers):
    answer_count = len(answers)
    math_forgiver_1 = [1, 2, 3, 4, 5] * ceil(answer_count / 5)
    math_forgiver_2 = [2, 1, 2, 3, 2, 4, 2, 5] * ceil(answer_count / 8)
    math_forgiver_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * ceil(answer_count / 10)

    math_forgiver_1 = math_forgiver_1[:answer_count]
    math_forgiver_2 = math_forgiver_2[:answer_count]
    math_forgiver_3 = math_forgiver_3[:answer_count]

    correct = [0] * 3
    for index in range(answer_count):
        if math_forgiver_1[index] == answers[index]:
            correct[0] += 1
        if math_forgiver_2[index] == answers[index]:
            correct[1] += 1
        if math_forgiver_3[index] == answers[index]:
            correct[2] += 1

    max_correct = max(correct)
    answer = []
    for index in range(3):
        if correct[index] == max_correct:
            answer.append(index + 1)
    return answer


if __name__ == "__main__":
    for ans in [[1, 2, 3, 4, 5], [1, 3, 2, 4, 2], [1, 2, 3, 5, 4, 6]]:
        print(solution(ans))
