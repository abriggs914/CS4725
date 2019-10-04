mother(lucy,dan).
mother(lucy,matt).
mother(lucy,sue).
mother(nancy,lucy).
mother(nancy,lola).
mother(nancy,brian).
mother(mary,bill).
mother(mary,mark).
mother(mary,ron).
mother(mary,michelle).
mother(sue,gabriel).
mother(karen,gabriel).
mother(wilma,betty).
mother(wilma,henry).
mother(wilma,isabelle).
mother(cheryl,brett).
mother(cheryl,andrew).
mother(cheryl,sam).

father(bill,dan).
father(bill,matt).
father(bill,sue).
father(walter,lucy).
father(walter,lola).
father(walter,brian).
father(richard,bill).
father(richard,mark).
father(richard,ron).
father(jeff,michelle).
father(matt,betty).
father(matt,henry).
father(matt,isabelle).
father(dan,brett).
father(dan,andrew).
father(dan,sam).

male(dan).
male(matt).
male(bill).
male(brian).
male(walter).
male(mark).
male(ron).
male(richard).
male(jeff).
male(henry).
male(brett).
male(andrew).
male(sam).

female(lucy).
female(sue).
female(nancy).
female(lola).
female(mary).
female(michelle).
female(karen).
female(betty).
female(isabelle).
female(wilma).
female(cheryl).

parent(X,Y) :- father(X,Y).
parent(X,Y) :- mother(X,Y).

child(X,Y) :- parent(Y,X).

sibling(X,Y) :- parent(Z,X), parent(Z,Y), X \== Y.

grandparent(X,Y) :- parent(Z,Y), parent(X,Z).

greatgrandparent(X,Y) :- grandparent(Z,Y), parent(X,Z).

ancestor(X,Y) :- parent(X,Y).
ancestor(X,Y) :- parent(Z,Y), ancestor(X,Z).

uncle(X,Y) :- parent(Z,Y), sibling(X,Z), male(X).

aunt(X,Y) :- parent(Z,Y), sibling(X,Z), female(X).

nephew(X,Y) :- sibling(Z,Y), child(X,Z), male(X).

niece(X,Y) :- sibling(Z,Y), child(X,Z), female(X).

firstcousin(X,Y) :- parent(Z,X), parent(W,Y), sibling(Z,W).
