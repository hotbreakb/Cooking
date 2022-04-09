def solution(price, money, count):
    diff = sum(range(1, count+1))*price - money
    if diff < 0:
        diff = 0
    return diff


price = 1
money = 100
count = 2
print(solution(price, money, count))
