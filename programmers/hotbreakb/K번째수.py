from array import array

from click import command


def solution(array, commands):
    answer = []
    for start, end, k in commands:
        answer.append(sorted(array[start-1:end])[k-1])
    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))
