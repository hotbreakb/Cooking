from collections import Counter


def solution(dartResult):
    winner = Counter(dartResult)
    star = winner["*"]
    looser = winner["#"]

    answer = 0
    score = 0
    for i in range(len(dartResult)):
        if i > 0 and dartResult[i] == "0" and dartResult[i-1] == "1":
            continue
        if dartResult[i].isdigit():
            if i+1 < len(dartResult) and dartResult[i+1].isdigit():
                score = 10
                continue
            score = int(dartResult[i])
            continue

        if dartResult[i] == "S":
            answer += score
            continue
        if dartResult[i] == "D":
            score = pow(score, 2)
        elif dartResult[i] == "T":
            score = pow(score, 3)
        elif dartResult[i] == "*":
            if star > 1:
                score *= 4
                star -= 1
                answer += score
            elif star > 0:
                score *= 2
                star -= 1
                answer += score
        else:
            if star > 1:
                score *= (-2)
            else:
                score *= (-1)
            answer += score

    answer += score
    return answer


dartResult = input().rstrip()
print(solution(dartResult))
