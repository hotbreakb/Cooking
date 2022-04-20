#
#  기능개발
#  https://programmers.co.kr/learn/courses/30/lessons/42586
#  Version: Python 3.8.9
#
#  Created by hotbreakb on 2022/04/10.
#

def solution(progresses, speeds):
    answer = []
    days = list(map(lambda item: (100-item[0])//item[1] if (
        100-item[0]) % item[1] == 0 else (100-item[0])//item[1]+1, zip(progresses, speeds)))

    i, uploaded = 0, 1
    while i < len(days):
        for j in range(i+1, len(days)):
            if days[i] >= days[j]:
                uploaded += 1
            else:
                break

        answer.append(uploaded)
        i += uploaded
        uploaded = 1
    return answer


progresses = [1, 1, 1]
speeds = [1, 2, 3]
print(solution(progresses, speeds))
