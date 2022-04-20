#
#  문자열 압축
#  https://programmers.co.kr/learn/courses/30/lessons/60057
#  Version: Python 3.8.9
#
#  Created by hotbreakb on 2022/04/10.
#

# def solution(s):
#     shortestCompressed = s

#     for unit in range(1, len(s)+1):
#         compressed = ""
#         i = 0
#         compressedNum = 0
#         while i < len(s):
#             pattern = s[i:i+unit]
#             for j in range(i+2*unit-1, len(s)):
#                 if s[j-unit+1:j] == pattern:
#                     compressedNum += 1
#                     i += unit

#         # 길이가 짧은 것이 결과값
#         if len(compressed) < len(shortestCompressed):
#             shortestCompressed = compressed

#     return len(shortestCompressed)

def solution(s):
    answer = len(s)

    # 완전 탐색
    for step in range(1, len(s)//2+1):
        count = 1  # arr 길이를 확인하는 대신 count 변수 사용
        compressed = 0  # compress를 실제 문자열로 만드는 대신 길이만 담는 변수로 설정
        prev = s[:step]

        for start in range(step, len(s)+step, step):
            curr = s[start:start+step]
            if curr == prev:
                count += 1  # 배열에 문자열을 실제로 넣어주는 대신 count만 증가
            else:
                compressed += len(str(count)+prev) if count > 1 else len(prev)
                count = 1  # 배열을 비워주는 대신 count = 1로 리셋
                prev = curr

        answer = min(answer, compressed)

    return answer


s = "abcbcbc"
print(solution(s))
