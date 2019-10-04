bigorder(Cust) :- order(Cust, X, Y), Y > 100.

notenough(Cust, Part) :- order(Cust, PN1, Q1), inventory(PN1, Q2), Q1 > Q2, part(Part, PN1, Y). 

orderedmore(C1, C2) :- order(C1, PN1, Q1), order(C2, PN2, Q2), PN1 =:= PN2, Q1 > Q2.
