digit(1).
digit(2).
digit(3).
digit(4).

valid(X,W,Y,Z) :- X \== W, X \== Y, X \== Z, W \== Y, W \== Z, Y \== Z, digit(X), digit(W), digit(Y), digit(Z).

solve(A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P) :-
	valid(A, B, C, D),
	valid(E, F, G, H),
	valid(I, J, K, L),
	valid(M, N, O, P),

	valid(A, E, I, M),
	valid(B, F, J, N),
	valid(C, G, K, O),
	valid(D, H, L, P),

	valid(A, E, I, F),
	valid(B, C, D, H),
	valid(G, J, K, M),
	valid(L, N, O, P).
