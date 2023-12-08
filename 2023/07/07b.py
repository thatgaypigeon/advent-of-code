winnings = []

card_values = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
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
            if (num := hand.count(card)) > 0 and card != "J":
                cards[card] = num

        values = list(cards.values())

        j_count = hand.count("J")

        if values:
            max_value = max(values) or 0
            values.remove(max_value)
        else:
            max_value = 0

        max_value = max_value + j_count

        match max_value:
            case 5:
                type_index = 0
            case 4:
                type_index = 1
            case 3:
                if 2 in values:
                    type_index = 2
                else:
                    type_index = 3
            case 2:
                if 2 in values:
                    type_index = 4
                else:
                    type_index = 5
            case _:
                type_index = 6

        hand_type = types[type_index]

        order[hand_type].append(hand)

    i = len(hands)

    for k, v in order.items():
        if v:
            ordered_hands = sorted(v, key=lambda x: [card_values.index(c) for c in x])
            for hand in ordered_hands:
                winnings.append(int(bids[hands.index(hand)]) * i)
                i -= 1

print(sum(winnings))
