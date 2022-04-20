#
#  영어 끝말잇기
#  https://programmers.co.kr/learn/courses/30/lessons/12981
#  Version: Python 3.8.12
#
#  Created by WhiteHyun on 2022/04/19.
#


def solution(n, words):
    answer = [0, 0]

    speak_set = {words[0]}
    for i in range(1, len(words)):
        if words[i] in speak_set or words[i - 1][-1] != words[i][0]:
            answer[0] = i % n + 1
            answer[1] = i // n + 1
            break
        speak_set.add(words[i])
    return answer
