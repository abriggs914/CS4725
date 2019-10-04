digit(0).
digit(1).
digit(2).
digit(3).
digit(4).
digit(5).
digit(6).
digit(7).
digit(8).
digit(9).
carry(0).
carry(1).
solution(T,W,O,F,U,R) :-

  digit(T), digit(W), digit(O), digit(F), digit(U), digit(R), 
  carry(C10), carry(C100), carry(C1000),

  fd_all_different([T,W,O,F,U,R]),

  O + O =:= R + 10 * C10,
  W + W + C10 =:= U + 10 * C100,
  T + T + C100 =:= O + 10 * C1000,
  C1000 =:= F,

  F =\= 0,
  T =\= 0.
