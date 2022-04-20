#
#  H-Index
#  https://programmers.co.kr/learn/courses/30/lessons/42747
#  Version: Python 3.8.9
#
#  Created by hotbreakb on 2022/04/12.
#

def solution(citations):
    papers = sorted(citations, reverse=True)
    max_number = papers[0]
    for h_index in range(max_number, -1, -1):
        index = 0
        while index < len(papers) and papers[index] >= h_index:
            index += 1
        if h_index <= index:
            return h_index


if __name__ == "__main__":
    print(solution([0, 1, 2, 2, 3, 5, 6, 7]))
    print(solution([1, 2, 3, 4, 5, 6, 7]))
    print(solution([0, 0, 2]))
    print(solution([0, 0, 0]))
    print(solution([3, 0, 6, 1, 5]))
    print(solution([0, 1, 2, 5, 5, 5, 5]))
