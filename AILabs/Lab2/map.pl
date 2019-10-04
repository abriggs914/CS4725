colour(red).
colour(green).
colour(blue).
solution(WA,NT,Q,NSW,V,SA,T) :- 
  colour(WA), colour(NT), colour(Q), colour(NSW), colour(V), colour(SA), colour(T),
  WA \== NT,
  WA \== SA,
  NT \== SA,
  NT \== Q,
  Q \== SA,
  Q \== NSW,
  NSW \== SA,
  NSW \== V,
  V \== SA.
