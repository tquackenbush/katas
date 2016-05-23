def isStraightFlush(input_hand):
    #5 cards of the same suit with consecutive values. Ranked by the highest card in the hand.
    print "is flush"
    return False

def isPair(input_hand):
    print "is pair"
    return False

input_hand = "2H 3D 5S 9C KD"
#card = { "number": 1, "suit": 'K' }

hand_types = {
    "straightFlush": {"rank": 8, "verify": isFlush, "score": scoreFlush }
}

input_1_highest_hand = None

# for input 1
for handType in hand_types:
    if hand_types[handType]['verify'](input_hand):
        inout_1_higest_hand = hand
        break

input_2_highest_hand = None

# for input 2
for handType in hand_types:
    if hand_types[handType]['verify'](input_hand):
        input_2_higest_hand = hand
        break

if input_1_highest_hand == input_2_highest_hand:
    print "input 2 winner"


if input_1_highest_hand < input_2_highest_hand:
    print "input 2 winner"

if input_1_highest_hand > input_2_highest_hand:
    print "input 1 winner"






if not highest_hand:
    print "regular hand, hight card"

if equal, check highest card

# Straing Flush
# Four of a kind
# full house
# Flush
# straight
# trhee of a kind
# two pair
# pair
#
# ---
#
# high card
