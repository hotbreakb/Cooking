#
#  가운데 글자 가져오기
#  https://programmers.co.kr/learn/courses/30/lessons/12903
#  Version: Python 3.8.9
#
#  Created by hotbreakb on 2022/04/10.
#

def solution(s):
    return s[len(s)//2] if len(s) % 2 != 0 else s[len(s)//2-1:len(s)//2+1]
