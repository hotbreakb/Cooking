#
#  15904번: UCPC는 무엇의 약자일까?
#  https://www.acmicpc.net/problem/15904
#  Version: Python 3.8.9
#
#  Created by hot on 2022/01/01.
#


from sys import stdin

read = stdin.readline


str = input().rstrip()

def isUPCP():
    answer = "UCPC"
    findIndex = 0

    for s in str:
        if s == answer[findIndex]:
            findIndex += 1
        
        if findIndex == len(answer):
            return True
    
    return False
    
    

if isUPCP():
    print("I love UCPC")
else:
    print("I hate UCPC")

