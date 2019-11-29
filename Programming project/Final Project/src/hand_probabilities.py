
def gen_deck() :
    deck = {"hearts": [2,3,4,5,6,7,8,9,10,"J","Q","K","A"],
            "spades": [2,3,4,5,6,7,8,9,10,"J","Q","K","A"],
            "diamonds": [2,3,4,5,6,7,8,9,10,"J","Q","K","A"],
            "clubs": [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]}
    shuffle_deck(deck)
    return deck

fact = lambda n : 1 if n <= 0 else n*fact(n-1)
choose = lambda n, r : (fact(n) / (fact(r)*(fact(n-r))))

p_one_pair = (choose(13,1)*choose(4,2)*choose(12,3)*(choose(4,1)**3)) / choose(52,5)
p_two_pair = (choose(13,2)*choose(4,2)*choose(4,2)*choose(11,1)*choose(4,1)) / choose(52,5)
p_3_of_kind = (choose(13,1)*choose(4,3)*choose(12,2)*(choose(4,1)**2)) / choose(52,5)
p_full_house = (choose(13,1)*choose(4,3)*choose(12,1)*choose(4,2)) / choose(52,5)
p_4_of_kind = (choose(13,1)*choose(4,4)*choose(12,1)*choose(4,1)) / choose(52,5)
p_straight = (((10*(choose(4,1)**5))-40)) / choose(52,5)
p_flush = (choose(4,1)*choose(13,5)-40) / choose(52,5)
p_straight_flush = (36) / choose(52,5)
p_royal_flush = (4) / choose(52,5)
p_no_hand = ((choose(13,5)-10)*((4**5)-4)) / choose(52,5)

probabilities = {	"p_one_pair": p_one_pair,
					"p_two_pair": p_two_pair,
					"p_3_of_kind": p_3_of_kind,
					"p_full_house": p_full_house,
					"p_4_of_kind": p_4_of_kind,
					"p_straight": p_straight,
					"p_flush": p_flush,
					"p_straight_flush": p_straight_flush,
					"p_royal_flush": p_royal_flush,
					"p_no_hand": p_no_hand} 

print("p_one_pair: " + str(p_one_pair))
print("p_two_pair: " + str(p_two_pair))
print("p_3_of_kind: " + str(p_3_of_kind))
print("p_full_house: " + str(p_full_house))
print("p_4_of_kind: " + str(p_4_of_kind))
print("p_straight: " + str(p_straight))
print("p_flush: " + str(p_flush))
print("p_straight_flush: " + str(p_straight_flush))
print("p_royal_flush: " + str(p_royal_flush))
print("p_no_hand: " + str(p_no_hand))
print("choose(52, 5): " + str(choose(52, 5)))

print(sum(list(probabilities.values())))