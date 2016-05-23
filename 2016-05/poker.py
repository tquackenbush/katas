def isStraightFlush(input_hand):
    #5 cards of the same suit with consecutive values. Ranked by the highest card in the hand.
    print "is straight flush"
    return False

def isHighCard(input_hand):
    print "is high card"
    return True

def scoreStraightFlush(input_hand):
    # sort cards by number/suit, take highest
    # next highest card?
    return 10 # king or something

def scoreHighCard(input_hand):
    # sort cards by number/suit, take highest
    # next highest card?
    return 10 # king or something

def findHighestHand(input_hand):
    highest_hand = None
    for handType in hand_types:
        if hand_types[handType]['verify'](input_hand):
            print "setting hand"
            highest_hand = hand_types[handType]
            break
    return highest_hand

input_1 = "2H 3D 5S 9C KD"
input_2 = "2C 3H 4S 8C AH"
#card = { "number": 1, "suit": 'H' }

hand_types = {
    "straightFlush": {"rank": 8, "verify": isStraightFlush, "score": scoreStraightFlush },
    # ...
    "highCard": {"rank": 0, "verify": isHighCard, "score": scoreHighCard }
}

input_1_highest_hand = findHighestHand(input_1)
input_2_highest_hand = findHighestHand(input_2)

print input_1_highest_hand
print input_2_highest_hand

if input_1_highest_hand['rank'] < input_2_highest_hand['rank']:
    print "input 2 winner"

if input_1_highest_hand['rank'] > input_2_highest_hand['rank']:
    print "input 1 winner"

if input_1_highest_hand == input_2_highest_hand:
    input_1_score = input_1_highest_hand['score'](input_1)
    input_2_score = input_2_highest_hand['score'](input_2)
    if input_1_score < input_2_score:
        print "input 2 wins"
    else:
        print "input 1 wins"

# Straing Flush
# Four of a kind
# full house
# Flush
# straight
# trhee of a kind
# two pair
# pair
# high card
