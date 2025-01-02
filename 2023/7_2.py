from collections import defaultdict

file = 'data/7.txt'

cards_order = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "1", "J"]


class Hand:

    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = bid
        self.sorted_hand = self.sort_hand()
        self.type = self.get_type()

    def __gt__(self, other):
        if not other or not self:
            return True
        if self.type > other.type:
            return True
        if self.type < other.type:
            return False
        # keys1 = sorted(self.hand, key = lambda i: (-self.sorted_hand[i], cards_order.index(i)))
        # keys2 = sorted(other.hand, key = lambda i: (-other.sorted_hand[i], cards_order.index(i)))

        for index, k1 in enumerate(self.hand):
            k2 = other.hand[index]
            if not k1:
                continue
            if cards_order.index(k1)<cards_order.index(k2):
                return True
            if cards_order.index(k1)>cards_order.index(k2):
                return False
            continue
        print("yolo %s %s" % (self.hand, other.hand))
        return True

    def sort_hand(self):
        sorted_hand = defaultdict(int)
        for card in self.hand:
            sorted_hand[card] += 1
        return sorted_hand

    def get_type(self):
        vexcl = [v for k, v in self.sorted_hand.items() if k != "J"]
        kexcl = [k for k, v in self.sorted_hand.items() if k != "J"]
        max_v = 0
        if vexcl:
            max_v = max(vexcl)
        jcards = self.sorted_hand.get("J", 0)
        if max_v+jcards == 5:
            return 6
        if max_v+jcards == 4:
            return 5
        if max_v+jcards == 3:
            if len(kexcl) == 2:
                return 4
            return 3
        if max_v+jcards == 2:
            if len(kexcl) == 3:
                return 2
            return 1
        if max_v+jcards == 1:
            return 0
        print(max_v, jcards, self.sorted_hand)

if __name__ == "__main__":
    with open(file, 'r') as open_file:
        data = open_file.read()

    hands = []
    for row in data.split("\n"):
        if not row:
            continue
        hand, bid = row.split(" ")
        hands.append(Hand(hand, int(bid)))

    rank = 1
    total = 0
    for i in sorted(hands):
        print("%d - %s %d %s" %(rank, i.hand, i.bid, i.type))
        total += rank * i.bid
        rank += 1
    print(total)
    print(rank)
