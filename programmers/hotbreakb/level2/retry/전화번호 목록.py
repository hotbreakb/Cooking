#
#  전화번호 목록
#  https://programmers.co.kr/learn/courses/30/lessons/42577
#  Version: Python 3.8.9
#
#  Created by hotbreakb on 2022/04/18.
#
import heapq


def solution(phone_book):
    heap_queue = []
    for phone_num in phone_book:
        heapq.heappush(heap_queue, phone_num)

    for phone_num in phone_book:
        print(heapq.heappop(heap_queue))

    return True


phone_book = ["234", "24", "123", "456789"]
print(solution(phone_book))
