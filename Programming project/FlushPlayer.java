import java.util.Collections;
import java.util.Stack;

/**
 * FlushPlayer - a simple example implementation of the player interface for PokerSquares that 
 * attempts to get flushes in the first four columns.
 * Author: ________, based on code provided by Todd W. Neller and Michael Fleming
 */
public class FlushPlayer implements PokerSquaresPlayer {

        private final int SIZE = 5; // number of rows/columns in square grid
        private final int NUM_POS = SIZE * SIZE; // number of positions in square grid
        private final int NUM_CARDS = Card.NUM_CARDS; // number of cards in deck
        private Card[][] grid = new Card[SIZE][SIZE]; // grid with Card objects or null (for empty positions)

	
	/* (non-Javadoc)
	 * @see PokerSquaresPlayer#setPointSystem(PokerSquaresPointSystem, long)
	 */
	@Override
	public void setPointSystem(PokerSquaresPointSystem system, long millis) {
		// The FlushPlayer, like the RandomPlayer, does not worry about the scoring system.	
	}
	
	/* (non-Javadoc)
	 * @see PokerSquaresPlayer#init()
	 */
	@Override
	public void init() { 
                // clear grid
                for (int row = 0; row < SIZE; row++)
                        for (int col = 0; col < SIZE; col++)
                                grid[row][col] = null;

	}

	/* (non-Javadoc)
	 * @see PokerSquaresPlayer#getPlay(Card, long)
	 */
	@Override
	public int[] getPlay(Card card, long millisRemaining) {
		/*
		If a card’s suit is clubs, insert it in the first empty square in column 0 (the
		leftmost column). Similarly, use column 1 for diamonds, column 2 for hearts,
		and column 3 for spades.
		– If the appropriate column is already full, then insert the card in the first empty
		square in column 4 (the rightmost column).
		– If column 4 is also full, then insert the card in the first available square in the
		grid, trying column 0 first, then column 1, then column 2, and then column 3.
		*/
                int cardrow = 0;
                int cardcol = 0;

                int cardrank = card.getRank();
                int cardsuit = card.getSuit();
				int nextCol = -1;
				
				int nextRowInCol = nextAvailSpaceInCol(cardsuit);
				if (nextRowInCol < 0) {
					nextCol = 4;
					nextRowInCol = nextAvailSpaceInCol(nextCol);
					if (nextRowInCol < 0) {
						nextCol = -1;
						while (nextRowInCol < 0) {
							nextCol++;
							nextRowInCol = nextAvailSpaceInCol(nextCol);
							if (nextCol > 3) {
								nextCol = 0;
							}
						}
					}
				}
				
				cardrow = nextRowInCol;
				cardcol = ((nextCol < 0)? cardsuit : nextCol);

                grid[cardrow][cardcol] = card;

                int[] playPos = {cardrow, cardcol};
                return playPos;
	}
	
	public int nextAvailSpaceInCol(int colIdx) {
		for (int r = 0; r < SIZE; r++) {
			if (grid[r][colIdx] == null) {
				return r;
			}
		}
		// no room
		return -1;
	}
	
	/* (non-Javadoc)
	 * @see PokerSquaresPlayer#getName()
	 */
	@Override
	public String getName() {
		return "FlushPlayer";
	}

	/**
	 * Demonstrate FlushPlayer play with British point system.
	 * @param args (not used)
	 */
	public static void main(String[] args) {
		PokerSquaresPointSystem system = PokerSquaresPointSystem.getBritishPointSystem();
		System.out.println(system);
		new PokerSquares(new FlushPlayer(), system).play(); // play a single game
	}

}
