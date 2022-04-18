#
#  영어 끝말잇기
#  https://programmers.co.kr/learn/courses/30/lessons/12981
#  Version: Python 3.8.9
#
#  Created by hotbreakb/level2 on 2022/04/18.
#

def solution(n, words):
    circle, user_index = 1, 1
    word_dict = dict()
    last_char = ""

    for word in words:
        if last_char != "" and last_char != word[0]:
            return [user_index, circle]

        last_char = word[-1]
        if word not in word_dict.keys():
            word_dict[word] = 1
        else:
            return [user_index, circle]

        user_index += 1

        if user_index > n:
            circle += 1
            user_index = 1

    return [0, 0]
