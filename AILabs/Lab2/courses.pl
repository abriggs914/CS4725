hastaken(dave,cs1000).
hastaken(dave,cs1200).
hastaken(dave,cs1400).

hastaken(bill,cs1000).
hastaken(bill,cs1200).
hastaken(bill,cs1600).
hastaken(bill,cs2000).

cantake(X,cs2000) :- hastaken(X,cs1000), hastaken(X,cs1200), \+ hastaken(X,cs2000).
cantake(X,cs2500) :- hastaken(X,cs1600), \+ hastaken(X,cs2500).
cantake(X,cs2500) :- hastaken(X,cs1200), hastaken(X,cs1400), \+ hastaken(X,cs2500).
cantake(X,cs3000) :- hastaken(X,cs2000), \+ hastaken(X,cs3000).
