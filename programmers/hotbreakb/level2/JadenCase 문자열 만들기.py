#
#  JadenCase 문자열 만들기
#  https://programmers.co.kr/learn/courses/30/lessons/12951
#  Version: Python 3.8.9
#
#  Created by hotbreakb on 2022/04/14.
#

def solution(s):
    answer = ""

    for i in range(len(s)):
        if s[i] == " " or s[i].isdigit():
            answer += s[i]
        else:
            if i == 0:
                answer += s[i].upper()
            elif s[i-1] != " ":
                answer += s[i].lower()
            else:
                answer += s[i].upper()

    return answer


s = input().rstrip()
print(solution(s))
