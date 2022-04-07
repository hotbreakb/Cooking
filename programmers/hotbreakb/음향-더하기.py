def solution(absolutes, signs):
    return sum(map(lambda items: items[0] * (-1) if not items[1]
                   else items[0]*items[1], zip(absolutes, signs)))


absolutes = [1, 2, 3]
signs = [True, False, True]
print(solution(absolutes, signs))
