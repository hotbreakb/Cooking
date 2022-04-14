#
#  최댓값과 최솟값
#  https://programmers.co.kr/learn/courses/30/lessons/12939
#  Version: Python 3.8.9
#
#  Created by hotbreakb on 2022/04/12.
#

def solution(s):
    nums = sorted(map(int, s.split()))
    return str(nums[0])+" "+str(nums[-1])
