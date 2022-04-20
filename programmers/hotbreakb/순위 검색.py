#
#  순위 검색
#  https://programmers.co.kr/learn/courses/30/lessons/72412
#  Version: Python 3.8.9
#
#  Created by hotbreakb on 2022/04/16.
#

def solution(infos, query):
    answer = []
    participants_info = []
    for info in infos:
        participants_info.append(info.split())

    for command in query:
        # query -> "and" 지우기
        command = command.replace(" and ", " ")
        options = command.split()
        participants_info_copied = participants_info.copy()

        for i in range(len(options)):
            if options[i] == "-":
                continue
            if options[i].isdigit():
                participants_info_copied = list(filter(
                    lambda participant: int(participant[i]) >= int(options[i]), participants_info_copied))
            else:
                participants_info_copied = list(filter(
                    lambda participant: participant[i] == options[i], participants_info_copied))

        answer.append(len(participants_info_copied))

    return answer


infos = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
         "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]
print(solution(infos, query))
