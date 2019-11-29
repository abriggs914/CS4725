import poker_squares as ps
import output_utility_analyzer as util_analyzer

print("running main")

ps.simulate_poker_squares(200)
# util_analyzer.print_dict(util_analyzer.get_best_cards())
#
# print(util_analyzer.get_column_names())

# results_dict = {}
sims = 5
overall_card_utilities = {}

certainty_stats = {"c": 0,
                   "p": 0,
                   "n": 0,
                   "s": 0,
                   "C": 0,
                   "U": 0}


def init_results_dict():
    results_dict = {}
    for i in range(1, 53):
        results_dict[i] = dict(zip(util_analyzer.get_column_names(), [certainty_stats.copy() for j in range(25)]))
    return results_dict


# print("\n\tresults_dict\n")
# util_analyzer.print_dict(results_dict)


def run_poker_squares(x_simulations):
    results_dict = init_results_dict()
    for i in range(x_simulations):
        ps.simulate_poker_squares(10)
        best_cards_iter = util_analyzer.get_best_cards()
        for key, val in best_cards_iter.items():
            score = val[1]
            card = val[2]
            certainty_dict = val[3]
            print("certainty_dict: " + str(certainty_dict))
            results_dict[card][key]["c"] += certainty_dict[card]["c"]
            results_dict[card][key]["p"] += certainty_dict[card]["p"]
            results_dict[card][key]["n"] += certainty_dict[card]["n"]
            results_dict[card][key]["s"] += certainty_dict[card]["s"]
            results_dict[card][key]["C"] += certainty_dict[card]["C"]

    print("\n\tresults_dict\n")
    util_analyzer.print_dict(results_dict)
    return results_dict


def number_knowns(utilities):
    known = 0
    for k, v in utilities.items():
        if v != 0:
            known += 1
    return known


def obtain_x_known_utilities(x):
    cards_utilities = {}
    k = number_knowns(cards_utilities)
    print("k: " + str(k))
    while k < x:
        results_dict = run_poker_squares(sims)
        for key, val in results_dict.items():
            # lst = [s for s in ]
            scores = sum([square["s"] for square in val.values()])
            if key in cards_utilities:
                cards_utilities[key] = (cards_utilities[key] + (scores / sims)) / 2
            else:
                cards_utilities[key] = scores / sims
        k = number_knowns(cards_utilities)
        print("k: " + str(k))
        print("cards_utilities:")
        util_analyzer.print_dict(cards_utilities)

    util_analyzer.print_dict(cards_utilities)
    print("# known card utilites:")
    util_analyzer.print_dict(number_knowns(cards_utilities))


obtain_x_known_utilities(25)

