def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        line = format(int(format(arr1[i], "b"), 2)
                      | int(format(arr2[i], "b"), 2), "b").replace("1", "#").replace("0", " ")
        while len(line) < n:
            line = " "+line
        answer.append(line)
    return answer


n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n, arr1, arr2))
