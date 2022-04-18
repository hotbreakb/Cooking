#
#  [1차] 뉴스 클러스터링
#  https://programmers.co.kr/learn/courses/30/lessons/17677
#  Version: Python 3.9.10
#
#  Created by WhiteHyun on 2022/04/15.
#


def union(collection_1, collection_2) -> list:
    """
    다중집합의 합집합을 구한다.
    """
    temp_list = collection_1.copy()
    union_list = collection_1.copy()

    for element in collection_2:
        if element in temp_list:
            temp_list.remove(element)
        else:
            union_list.append(element)
    return union_list


def intersection(collection_1: list, collection_2: list) -> list:
    """
    다중집합의 교집합을 구한다.
    """
    temp_list = collection_1.copy()
    intersection_list = []

    for element in collection_2:
        if element in temp_list:
            intersection_list.append(element)
            temp_list.remove(element)
    return intersection_list


def get_multiplet_sets(string: str) -> list:
    """
    문자열을 가지고 다중집합을 구한다.
    """
    multiple_set = []
    for index in range(len(string) - 1):
        if (element := string[index : index + 2]).isalpha():
            multiple_set.append(element)
    return multiple_set


def solution(str1: str, str2: str) -> int:
    str1 = str1.lower()
    str2 = str2.lower()

    multiple_set_1 = get_multiplet_sets(str1)
    multiple_set_2 = get_multiplet_sets(str2)

    if not multiple_set_1 and not multiple_set_2:
        return 65536

    return int(
        len(intersection(multiple_set_1, multiple_set_2))
        / len(union(multiple_set_1, multiple_set_2))
        * 65536
    )


if __name__ == "__main__":
    print(solution("aa1+aa2", "AAAA12"))
