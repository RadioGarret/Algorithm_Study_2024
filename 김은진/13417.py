import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    cards = input().split()
    card_list = []

    start=cards[0]

    for card in cards:
        if ord(card) <= ord(start):
            card_list.insert(0, card)
            start = card
        else:
            card_list.append(card)

    card_str = ''.join(card_list)
    print(card_str)
