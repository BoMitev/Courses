cards = input().split()
n = int(input())

half_size = len(cards) // 2


for j in range(n):
    left_side = cards[0:half_size]
    right_side = cards[half_size:]

    faro_cards = []

    for i in range(len(left_side)):
        faro_cards.append(left_side[i])
        faro_cards.append(right_side[i])

    cards = faro_cards
print(cards)