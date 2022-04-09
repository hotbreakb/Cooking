def solution(sizes):
    width, height = 0, 0
    for card in sizes:
        card = sorted(card)
        width = max(width, card[0])
        height = max(height, card[1])

    return width*height


sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
print(solution(sizes))
