winnings = []

card_values = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
types = ["5K", "4K", "FH",  "3K", "2P", "1P", "HC"]

with open("input.txt", "r") as f:
    order: dict[str, list[str]] = {k: [] for k in types}

    hands, bids = [], []

    for line in map(str.strip, f.readlines()):
        hand = line.split()[0]
        bid = line.split()[1]

        hands.append(hand)
        bids.append(bid)

        cards: dict[str, int] = {}

        for card in card_values:
            if (num := hand.count(card)) > 0:
                cards[card] = num

        match values := list(cards.values()):
            case _ if 5 in values:
                order[types[0]].append(hand)
            case _ if 4 in values:
                order[types[1]].append(hand)
            case _ if 3 in values and 2 in values:
                order[types[2]].append(hand)
            case _ if 3 in values:
                order[types[3]].append(hand)
            case _ if values.count(2) == 2:
                order[types[4]].append(hand)
            case _ if 2 in values:
                order[types[5]].append(hand)
            case _:
                order[types[6]].append(hand)

    i = len(hands)

    for k, v in order.items():
        if v:
            ordered_hands = sorted(v, key=lambda x: [card_values.index(c) for c in x])
            for hand in ordered_hands:
                winnings.append(int(bids[hands.index(hand)]) * i)
                i -= 1

print(sum(winnings))
