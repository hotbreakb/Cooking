#
#  모음사전
#  https://programmers.co.kr/learn/courses/30/lessons/84512
#  Version: Python 3.9.10
#
#  Created by WhiteHyun on 2022/04/16.
#


from sys import setrecursionlimit

setrecursionlimit(1000000)

compare_list = []
count = 0


def back_tracking(vowels: list, words: list):
    global count
    if words == compare_list:  # 같은가?
        return True

    if len(compare_list) == 5:  # 길이가 6 이상이면 안됨. 바로 리턴
        return False

    # 모음으로 문장 만드는 과정
    for vowel in vowels:  # 모음 리스트에서 하나씩 꺼내옴
        compare_list.append(vowel)  # 리스트에 추가
        count += 1  # 카운트 증가
        if back_tracking(vowels, words):  # 함수 순환, 만약 True라면, 같은 글자를 찾은 것!
            return True
        compare_list.pop()

    return False


def solution(word: str) -> int:
    vowel_list = ["A", "E", "I", "O", "U"]
    back_tracking(vowel_list, list(word))
    return count


print(solution("EIO"))
