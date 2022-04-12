#
#  오픈채팅방
#  https://programmers.co.kr/learn/courses/30/lessons/42888
#  Version: Python 3.8.9
#
#  Created by hotbreakb on 2022/04/12.
#

def solution(record):
    answer = []
    userInfo = {}
    for info in record:
        if info[0] == "L":
            continue
        action, uid, name = info.split()
        if action == "Change":
            userInfo[uid] = name
        elif action == "Enter":
            userInfo[uid] = name

    for info in record:
        action, uid, _ = "", "", ""
        if info[0] == "C":
            continue
        if info[0] != "L":
            action, uid, _ = info.split()
        else:
            action, uid = info.split()
        if action == "Enter":
            answer.append(f"{userInfo[uid]}님이 들어왔습니다.")
        elif action == "Leave":
            answer.append(f"{userInfo[uid]}님이 나갔습니다.")

    return answer
