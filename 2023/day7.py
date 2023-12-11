# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:03:47 2022

@author: NghiaServer
"""

with open('day7_input') as f:
    data = f.readlines()

data = [d.strip('\n') for d in data]

#part1
CARD_STRENGTH = "23456789TJQKA"
CARD_STRENGTH_LABEL = "abcdefghijklm"

HAND_TYPE = ["11111", "1112", "122", "113", "23", "14", "5"]

hands = [d.split(" ")[0] for d in data]
bids = [int(d.split(" ")[1]) for d in data]

def calculate_card_strength(hand):
    unique_card = list(set(hand))
    hand_type = "".join(sorted([str(hand.count(card)) for card in unique_card]))
    hand_label = [CARD_STRENGTH_LABEL[CARD_STRENGTH.index(card)] for card in hand]
    return str(HAND_TYPE.index(hand_type)) + "".join(hand_label)

sorted_bids = sorted(bids, key = lambda k: calculate_card_strength(hands[bids.index(k)]))

score = 0

for i, b in enumerate(sorted_bids):
    score += (i+1) * b


print(score)

#part2
CARD_STRENGTH = "J23456789TQKA"
CARD_STRENGTH_LABEL = "abcdefghijklm"

HAND_TYPE = ["11111", "1112", "122", "113", "23", "14", "5"]

hands = [d.split(" ")[0] for d in data]
bids = [int(d.split(" ")[1]) for d in data]

def calculate_card_strength_with_joker(hand):
    unique_card = list(set(hand))
    bonus = 0
    counter = []
    i = 0
    i_max = 0
    for card in unique_card:
        if card == "J":
            bonus = hand.count(card)
        else:
            counter.append(hand.count(card))
            if counter[i] > counter[i_max]:
                i_max = i
            
            i += 1
    
    if bonus == 5:
        counter.append(5)
    else:
        counter[i_max] += bonus
        
    hand_type = "".join(sorted(list(map(str, counter))))
    hand_label = [CARD_STRENGTH_LABEL[CARD_STRENGTH.index(card)] for card in hand]
    return str(HAND_TYPE.index(hand_type)) + "".join(hand_label)

sorted_bids = sorted(bids, key = lambda k: calculate_card_strength_with_joker(hands[bids.index(k)]))

score = 0

for i, b in enumerate(sorted_bids):
    score += (i+1) * b

print(score)
