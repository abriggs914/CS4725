import random
import numpy as np
import pandas as pd

file = "boards_output.csv"


def read_file():
    return pd.read_csv(file)

df = None


card_placement_count = {}


    # print(df.head())


def print_dict(d):
    print("\n\tPRINTING DICT:\n")
    for key, val in d.items():
        print(str(key) + ":\t" + str(val))
    print("\n")


def select_best_card_for_square(placement_counts):
    best_cards = {}
    for col, cardList in placement_counts.items():  # loop possible boards that used each card
        if col != "score":
            # print("\tcardList: " + str(cardList))
            max_score = -1
            best_card = -1
            best_board = -1
            certainty_stats = {"c": 0,
                               "p": 0,
                               "n": 0,
                               "s": 0,
                               "C": 0,
                               "U": 0}
            card_certainties = dict(zip([i for i in range(1, 53)], [certainty_stats for i in range(1,53)]))
            # print("card_certainties BEFORE")
            # print_dict(card_certainties)
            for cardIndex in cardList:  # loop cards 1-52
                # print("\t\tcardIndex: " + str(cardIndex))
                idx = cardList.index(cardIndex) + 1
                if len(cardIndex) > 0:
                    for game in cardIndex:
                        card_certainties[idx]["c"] += 1
                        card_certainties[idx]["s"] += game[1]
                        # print("\t\t\tgame: " + str(game))
                        if game[1] > max_score:
                            best_card = game[2]
                            max_score = game[1]
                            best_board = game[0]
                            card_certainties[idx]["p"] += 1
                        else :
                            card_certainties[idx]["n"] += 1
            # print("card_certainties AFTER")
            # print_dict(card_certainties)
            best_cards[col] = (best_board, max_score, best_card, card_certainties)
    return best_cards


sample_size = 0


def init_card_placement_count():
    """Initializes card_placement_count dictionary.
    values are of form (game #, game score) where value index is card #"""
    global sample_size
    for col in df.columns:
        lst = list(df[col])
        sample_size = len(lst)
        # print("lst: " + str(lst))
        if col == "score":
            card_placement_count[col] = [lst.count(i) for i in range(320)]
            # space = "".join(["-" for i in range(2 * len(lst))])
            # print(space + "\n\tSCORE:\n" + str(card_placement_count[col]) + "\n" + space + "\n")
        else:
            card_placement_count[col] = [[(j, df["score"][j], df[col][j]) for j in range(len(lst)) if lst[j] == i] for i
                                         in
                                         range(1, 53)]
            # print("col: " + str(col) + "\t->\t" + str(card_placement_count[col]) + ", # items: " + str(
            #     len(card_placement_count[col])) + ", #empty: " + str(num_empty_spaces))


def get_best_cards():
    global df
    df = read_file()
    init_card_placement_count()
    # print_dict(card_placement_count)
    # print("sample_size: " + str(sample_size))

    best_cards_dict = select_best_card_for_square(card_placement_count)
    # print_dict(best_cards_dict)
    return best_cards_dict


def get_column_names():
    global df
    df = read_file()
    return list(df.columns)

# for square in df.columns :
#
#
# def calc_utility(score) :
#
