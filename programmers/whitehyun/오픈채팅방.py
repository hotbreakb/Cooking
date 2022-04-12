#
#  오픈채팅방
#  https://programmers.co.kr/learn/courses/30/lessons/42888
#  Version: Python 3.8.12
#
#  Created by WhiteHyun on 2022/04/11.
#


def solution(records: list) -> list:
    user_id = {}
    result = []
    for record in records:
        command, *args = record.split()
        if command == "Leave":
            result.append((args[0], "님이 나갔습니다."))
            continue
        uid, nick_name = args
        user_id[uid] = nick_name
        if command == "Enter":
            result.append((uid, "님이 들어왔습니다."))

    answer = list(map(lambda x: user_id[x[0]] + x[1], result))

    return answer


print(
    solution(
        [
            "Enter uid1234 Muzi",
            "Enter uid4567 Prodo",
            "Leave uid1234",
            "Enter uid1234 Prodo",
            "Change uid4567 Ryan",
        ]
    )
)
