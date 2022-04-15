#
#  [1차] 뉴스 클러스터링
#  https://programmers.co.kr/learn/courses/30/lessons/17677
#  Version: Python 3.9.10
#
#  Created by WhiteHyun on 2022/04/15.
#


def union(collection_1, collection_2) -> list:
    temp_list = collection_1.copy()
    union_list = collection_1.copy()

    for element in collection_2:
        if element in temp_list:
            temp_list.remove(element)
        else:
            union_list.append(element)
    return union_list


def intersection(collection_1: list, collection_2: list) -> list:
    temp_list = collection_1.copy()
    intersection_list = []

    for element in collection_2:
        if element in temp_list:
            intersection_list.append(element)
            temp_list.remove(element)
    return intersection_list


def solution(str1: str, str2: str):
    str1 = str1.lower()
    str2 = str2.lower()
    str1_list = []
    str2_list = []
    stack = [str1[0]]
    for char in str1[1:]:
        char2 = stack.pop()
        if (element := char2 + char).isalpha():
            str1_list.append(element)
        stack.append(char)

    stack = [str2[0]]
    for char in str2[1:]:
        char2 = stack.pop()
        if (element := char2 + char).isalpha():
            str2_list.append(element)
        stack.append(char)

    if not str1_list and not str2_list:
        return 65536

    return int(
        len(intersection(str1_list, str2_list))
        / len(union(str1_list, str2_list))
        * 65536
    )


print(solution("aa1+aa2", "AAAA12"))
