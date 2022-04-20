#
#  [1차] 뉴스 클러스터링
#  https://programmers.co.kr/learn/courses/30/lessons/17677
#  Version: Python 3.8.9
#
#  Created by hotbreakb on 2022/04/13.
#

def solution(str1, str2):
    value = 65536
    str1_words = list()
    str2_words = list()

    str1_words = getWords(str1)
    str2_words = getWords(str2)

    union_sum = 0

    str1_counter = dict()
    for word in str1_words:
        if word not in str1_counter.keys():
            str1_counter[word] = 0
        str1_counter[word] += 1

    for word in str2_words:
        if word in str1_counter.keys() and str1_counter[word] > 0:
            str1_counter[word] -= 1
            union_sum += 1

    intersection_num = len(str1_words) + len(str2_words) - union_sum

    if intersection_num == 0:
        return value

    return int((union_sum / intersection_num)*value)


def getWords(input_str: str) -> list:
    words = []
    for i in range(1, len(input_str)):
        word = input_str[i-1:i+1]
        word = word.lower()
        if ord(word[0]) < ord("a") or ord(word[0]) > ord("z") or ord(word[1]) < ord("a") or ord(word[1]) > ord("z"):
            continue
        words.append(word)

    return words


str1 = input().rstrip()
str2 = input().rstrip()
print(solution(str1, str2))
