#
#  JadenCase 문자열 만들기
#  https://programmers.co.kr/learn/courses/30/lessons/12951
#  Version: Python 3.9.10
#
#  Created by WhiteHyun on 2022/04/16.
#


def solution(s: str):
    string_list = s.lower().split(" ")
    for index in range(len(string_list)):
        if string_list[index] and string_list[index][0].isalpha():
            string_list[index] = (
                chr(ord(string_list[index][0]) - 32) + string_list[index][1:]
            )
    return " ".join(string_list)


if __name__ == "__main__":
    print(solution("3abc de f  gg a  i"))
