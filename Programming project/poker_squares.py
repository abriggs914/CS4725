import traceback
import random
import copy
import sys
import re
import datetime

hands = {"RF": 4,
         "SF": 36,
         "4K": 624,
         "FH": 3744,
         "F": 5108,
         "S": 10200,
         "3K": 54912,
         "2P": 123552,
         "1P": 1098240,
         "HC": 1302540
         }

american_scoring = {"RF": 100,
                    "SF": 75,
                    "4K": 50,
                    "FH": 25,
                    "F": 20,
                    "S": 15,
                    "3K": 10,
                    "2P": 5,
                    "1P": 2,
                    "HC": 0}

british_scoring = {"RF": 30,
                   "SF": 30,
                   "4K": 16,
                   "FH": 10,
                   "F": 5,
                   "S": 12,
                   "3K": 6,
                   "2P": 3,
                   "1P": 1,
                   "HC": 0}

check_deck = {"hearts": [[2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"], 0],
              "spades": [[2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"], 0],
              "diamonds": [[2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"], 0],
              "clubs": [[2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"], 0]}

fact = lambda n: 1 if n <= 0 else n * fact(n - 1)
choose = lambda n, r: (fact(n) / (fact(r) * (fact(n - r))))

p_one_pair = (choose(13, 1) * choose(4, 2) * choose(12, 3) * (choose(4, 1) ** 3)) / choose(52, 5)
p_two_pair = (choose(13, 2) * choose(4, 2) * choose(4, 2) * choose(11, 1) * choose(4, 1)) / choose(52, 5)
p_3_of_kind = (choose(13, 1) * choose(4, 3) * choose(12, 2) * (choose(4, 1) ** 2)) / choose(52, 5)
p_full_house = (choose(13, 1) * choose(4, 3) * choose(12, 1) * choose(4, 2)) / choose(52, 5)
p_4_of_kind = (choose(13, 1) * choose(4, 4) * choose(12, 1) * choose(4, 1)) / choose(52, 5)
p_straight = ((10 * (choose(4, 1) ** 5)) - 40) / choose(52, 5)
p_flush = (choose(4, 1) * choose(13, 5) - 40) / choose(52, 5)
p_straight_flush = 36 / choose(52, 5)
p_royal_flush = 4 / choose(52, 5)
p_no_hand = ((choose(13, 5) - 10) * ((4 ** 5) - 4)) / choose(52, 5)

probabilities = {"p_one_pair": p_one_pair,
                 "p_two_pair": p_two_pair,
                 "p_3_of_kind": p_3_of_kind,
                 "p_full_house": p_full_house,
                 "p_4_of_kind": p_4_of_kind,
                 "p_straight": p_straight,
                 "p_flush": p_flush,
                 "p_straight_flush": p_straight_flush,
                 "p_royal_flush": p_royal_flush,
                 "p_no_hand": p_no_hand}


class Hand:
    def __init__(self, hand):
        # print("hand creation: " + str(hand) + ", type: " + str(type(hand)))
        self.hand = hand

    def __repr__(self):
        return str(self.hand)

    def gen_hash_identifier(self):
        return "".join([str(val) + key.title()[0] for key, val in self.hand])

    def is_scoring_poker_hand(self):
        poker_hand = False
        all_checked = False
        type_of_hand = None
        to_check = ["RF", "SF", "4K", "FH", "F", "S", "3K", "2P", "1P"]
        while not poker_hand and not all_checked:
            checking = to_check[0]
            to_check.remove(checking)
            # print("is a " + checking + ", " + str(poker_hand))
            poker_hand = (poker_hand or self.check_hand(checking))
            if poker_hand:
                type_of_hand = checking
            if len(to_check) == 0:
                all_checked = True
        return poker_hand, type_of_hand

    def check_hand(self, checking):
        scores = False
        if checking == "RF":
            scores = self.check_royal_flush()
        elif checking == "SF":
            scores = self.check_straight_flush()
        elif checking == "4K":
            scores = self.check_4_of_kind()
        elif checking == "FH":
            scores = self.check_full_house()
        elif checking == "F":
            scores = self.check_flush()
        elif checking == "S":
            scores = self.check_straight()
        elif checking == "3K":
            scores = self.check_3_of_kind()
        elif checking == "2P":
            scores = self.check_2_pair()
        elif checking == "1P":
            scores = self.check_pair()
        return scores

    def check_flush(self):
        suits = [card[0] for card in self.hand]
        return len(set(suits)) == 1

    def check_pair(self):
        vals = [card[1] for card in self.hand]
        return len(set(vals)) < 5

    def check_2_pair(self):
        vals = [card[1] for card in self.hand]
        return len(set(vals)) < 4

    def check_4_of_kind(self):
        vals = [card[1] for card in self.hand]
        counts = [vals.count(val) for val in vals]
        return 4 in counts

    def check_3_of_kind(self):
        vals = [card[1] for card in self.hand]
        counts = [vals.count(val) for val in vals]
        return 3 in counts

    def check_full_house(self):
        vals = [card[1] for card in self.hand]
        counts = [vals.count(val) for val in vals]
        return 3 in counts and 2 in counts

    def check_straight(self):
        vals = [card[1] for card in self.hand if type(card[1]) == int]
        face_vals = [card[1] for card in self.hand if type(card[1]) == str]
        # print("\tvals:\t" + str(vals))
        # print("\tface_vals:\t" + str(face_vals))
        if len(vals) > 0:
            lowest = min(vals)
            highest = max(vals)
        else:
            lowest = 0
            highest = 0
        face_val_lookup = {"A": 14, "K": 13, "Q": 12, "J": 11}
        if len(face_vals) > 0:
            for face_val in face_vals:
                lowest = lowest if face_val_lookup[face_val] > lowest else face_val_lookup[face_val]
                if face_val_lookup[face_val] > highest:
                    highest = face_val_lookup[face_val]
        return (highest - lowest) == 4

    def check_straight_flush(self):
        return (self.check_straight() and self.check_flush())

    def check_royal_flush(self):
        vals = [card[1] for card in self.hand]
        # print("vals: " + str(vals))
        return (self.check_straight_flush() and ("A" in vals and 10 in vals))


def probability_of(hand):
    return hands[hand] / total_hands


def shuffle_deck(deck):
    for suit in deck:
        random.shuffle(deck[suit])


def gen_deck():
    deck = {"hearts": [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"],
            "spades": [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"],
            "diamonds": [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"],
            "clubs": [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]}
    shuffle_deck(deck)
    return deck


def draw_hand(n_cards, deck):
    cards_left = sum([len(val) for val in deck.values()])
    if cards_left >= n_cards:
        return [draw_card(deck) for i in range(n_cards)]


def draw_card(deck):
    suits = ["hearts", "spades", "diamonds", "clubs"]
    # random.seed(datetime.time.second)
    suit = random.choice(suits)
    while len(deck[suit]) == 0 and len(suits) > 0:
        suits.remove(suit)
        suit = random.choice(suits)
    val = random.choice(deck[suit])
    # print("suit: " + str(suit) + ", val: " + str(val))
    deck[suit].remove(val)
    check_deck[suit][1] += 1
    return suit, val


def get_all_hands(poker_hands):
    new_poker_hands = poker_hands
    for i in range(5):
        vertical_hand = []
        for j in range(5):
            vertical_hand.append(poker_hands[j][i])
        new_poker_hands.append(vertical_hand)
    return new_poker_hands


def shuffle_generated_hands(generated_hands):
    # shuffled_hands = copy.deepcopy(generated_hands)
    cards = [card for hand in generated_hands for card in hand]
    shuffled_hands = []
    # print("\ncards:\t" + str(cards))
    # random.seed(datetime.time.second)
    for i in range(len(generated_hands)):
        new_hand = []
        for j in range(len(generated_hands[i])):
            card = random.choice(cards)
            new_hand.append(card)
            cards.remove(card)
        shuffled_hands.append(new_hand)
    # print("generated_hands:\t" + str(generated_hands))
    # print("shuffled_hands:\t" + str(shuffled_hands))
    return shuffled_hands


# def generate_boards_output_file(generated_boards):
#     try:
#         print("WRITING")
#         file = "boards_output.txt"
#         f = open(file, "w")
#         for board in generated_boards:
#             board_string = ""
#             for hand in board:
#                 board_string += Hand(hand).gen_hash_identifier()
#             f.write(board_string)
#             f.write("\n")
#         f.close()
#     except:
#         print("ERROR IN FILE WRITING")
#         print('>>> traceback <<<')
#         traceback.print_exc()
#         print('>>> end of traceback <<<')


def generate_boards_heuristic_output_file(generated_boards):
    try:
        print("WRITING")
        file = "boards_output.csv"
        f = open(file, "w")
        num_boards = len(generated_boards)
        board_size = 0 if num_boards == 0 else len(generated_boards[0]) // 2
        col_names = ""
        for i in range(board_size):
            for j in range(board_size):
                col_name = "[" + str(i) + ":" + str(j) + "]"
                col_names += col_name + ","
        col_names = col_names + "score\n"
        f.write(col_names)
        for board in generated_boards:
            board_string = ""
            board_score = 0
            for hand in board[:len(board) // 2]:
                hand_object = Hand(hand)
                hand_identifier = hand_object.gen_hash_identifier()
                # print("hand_identifier:\t{" + str(hand_identifier) + "}")
                res_list = re.split(r"[HDSC]", hand_identifier)[:-1]
                suits_list = re.split(r"[0-9AKQJ]", hand_identifier)
                suits_list = [suit for suit in suits_list if len(suit) > 0]
                face_val_lookup = {"A": 14, "K": 13, "Q": 12, "J": 11}
                suit_lookup = {"H": 1, "S": 2, "D": 3, "C": 4}
                for i in range(len(res_list)):
                    card = res_list[i]
                    if len(card) == 1:
                        if 45 >= ord(card) or ord(card) >= 58:
                            # lookup
                            card = face_val_lookup[card]
                        else:
                            card = int(card)
                    else:
                        card = int(card)
                    res_list[i] = card * suit_lookup[suits_list[i]]
                # print("res_list: " + str(res_list))
                board_string += ",".join(list(map(str, res_list))) + ","
                win_status = hand_object.is_scoring_poker_hand()
                if win_status:
                    if win_status[1]:
                        board_score += british_scoring[win_status[1]]
            f.write(board_string[:-1] + "," + str(board_score))
            f.write("\n")
        f.close()
    except:
        print("ERROR IN FILE WRITING")
        print('>>> traceback <<<')
        traceback.print_exc()
        print('>>> end of traceback <<<')


# --------------------------------------------------------------------------------
'''
######################
TESTING for Hand class
######################
'''
total_hands = sum([val for key, val in hands.items()])

american_expected_value = 0
british_expected_value = 0

for hand in hands:
    print(str(hand) + ":\t" + "%.5f" % (probability_of(hand)) + "\t\tBS:\t" + str(
        british_scoring[hand]) + "\tAS:\t" + str(american_scoring[hand]))
    american_expected_value += probability_of(hand) * american_scoring[hand]
    british_expected_value += probability_of(hand) * british_scoring[hand]

print("american_expected_value: " + str(american_expected_value))
print("british_expected_value: " + str(british_expected_value))

'''
deck = gen_deck()
poker_hands = []
for i in range(5) :
    new_hand = []
    for j in range(5) :
        new_hand.append(draw_card(deck))
    poker_hands.append(new_hand)
        
print("\n\tdeck\n" + str(deck))

print("\n\tpoker_hands\n")
for poker_hand in poker_hands : 
    print(poker_hand)
    
print("\n\tall poker_hands\n")
for poker_hand in get_all_hands(poker_hands) : 
    print(poker_hand)
    
print("\n\tcheck_deck\n" + str(check_deck))

print("\n\n")
for poker_hand in poker_hands :
    print("\n" + str(poker_hand) + ":\n\t=> " + str(Hand(poker_hand).is_scoring_poker_hand()))

test_hand = [('hearts', 9), ('hearts', "Q"), ('hearts', "J"), ('hearts', "A"), ('hearts', 10)]
print("\n\tTest Hand:\n" + str(test_hand) + ":\n\t=> " + str(Hand(test_hand).is_scoring_poker_hand()))
'''

'''
################################
TESTING for draw_hand
################################

print(sum(list(hands.values())))
deck = gen_deck()
print("deck: " + str(deck) + ", size: " + str(len(deck)))
first_hand = draw_hand(5, deck)
print(first_hand)
print(first_hand.gen_hash_identifier())
print(first_hand.is_scoring_poker_hand())
second_hand = draw_hand(5, deck)
print(second_hand)
print(second_hand.gen_hash_identifier())
print(second_hand.is_scoring_poker_hand())
sorted_probabilities = sorted(probabilities.items(), key=lambda kv: kv[1])
print("sorted_probabilities:\t" + str(sorted_probabilities))
'''


def simulate_poker_squares(n):
    sample_size = min(5000, max(1, n))
    generated_boards = []
    index = 0
    generated_hands = []
    deck = gen_deck()
    for j in range(5):
        h = draw_hand(5, deck)
        generated_hands.append(h)
    #     print("SELECTED: " + str(h))
    # print("\n\tUNUSED:\n" + str(deck))
    index = 0
    max_board_score = -sys.maxsize - 1
    min_board_score = sys.maxsize
    for i in range(sample_size):
        # print("\tgenerated_hands:\n" + str(generated_hands))
        shuffled_hands = shuffle_generated_hands(generated_hands)
        # if i == 0:
        #     print("\tshuffled_hands:\n" + str(shuffled_hands))
        generated_boards.append(get_all_hands(shuffled_hands))
        board_score = 0
        # print(str(i) + "\t" + "".join(["#" for i in range(112)]))
        for j in range(len(generated_boards[index])):
            hand = Hand(generated_boards[index][j])
            # print("hand:\t" + str(hand))
            score_status = hand.is_scoring_poker_hand()
            if score_status:
                win_type = score_status[1]
                if win_type:
                    board_score += british_scoring[win_type]
        # print("hand.is_scoring_poker_hand():\t" + str(score_status) + "\tscore:\t" + str(board_score))
        # print("\tBOARD SCORE:\t" + str(board_score))
        max_board_score = max_board_score if board_score < max_board_score else board_score
        min_board_score = min_board_score if board_score > min_board_score else board_score
        # print("".join(["#" for i in range(120)]))
        index += 1

    # print("MIN BOARD SCORE:\t" + str(min_board_score))
    # print("MAX BOARD SCORE:\t" + str(max_board_score))

    # print("generated_hands[index]:\t" + str(generated_hands[index]))
    # index += 1
    #	generated_boards.append(get_all_hands(generated_hands))

    # print("\n\tDECK:\n" + str(deck) + "\n")

    generate_boards_heuristic_output_file(generated_boards)
