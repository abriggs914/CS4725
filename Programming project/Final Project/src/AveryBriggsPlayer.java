import java.util.*;

/**
 * AveryBriggsPlayer - a simple example implementation of the player interface for PokerSquares that
 * makes random placements.
 * Author: Avery Briggs
 */
public class AveryBriggsPlayer implements PokerSquaresPlayer {

    /**
     * a stack of all unchosen plays represented as row-major indices. Row-major indices: play (r, c) is recorded as a single integer r * SIZE + c.
     * (See <a href="http://en.wikipedia.org/wiki/Row-major_order">http://en.wikipedia.org/wiki/Row-major_order</a>.)
     */
    private Stack<Integer> plays = new Stack<Integer>();


    private final int SIZE = 5; // number of rows/columns in square grid
    private final int NUM_POS = SIZE * SIZE; // number of positions in square grid
    private final int NUM_CARDS = Card.NUM_CARDS; // number of cards in deck
    private Card[][] grid = new Card[SIZE][SIZE]; // grid with Card objects or null (for empty positions)
    private PokerSquaresPointSystem system; // point system
    private int numPlays = 0; // number of Cards played into the grid so far
    private Card[] simDeck;

    /* (non-Javadoc)
     * @see PokerSquaresPlayer#setPointSystem(PokerSquaresPointSystem, long)
     */
    @Override
    public void setPointSystem(PokerSquaresPointSystem system, long millis) {
        // The AveryBriggsPlayer cares about as much about the score system as a honey badger.
        this.system = system;
    }

    /* (non-Javadoc)
     * @see PokerSquaresPlayer#init()
     */
    @Override
    public void init() { // Create a stack of a random permutation of 25 play positions (0-24) for random plays
        plays.clear();
        for (int i = 0; i < 25; i++)
            plays.push(i);
        Collections.shuffle(plays);

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
//        int play = plays.pop(); // get the next random position for play
//        int row, col;
//        int[] playPos = {row, col}; // decode it into row and column
        int[] playPos = genMove(card, millisRemaining);
        grid[playPos[0]][playPos[1]] = card;
//        System.out.println("rows & cols: " + genRowAndColLists());
        return playPos; // return it
    }

    public int[] genMove(Card card, long millisRemaining) {
        int maxScore = Integer.MIN_VALUE;
        int[] maxRC = new int[2];
        for (int i = 0; i < SIZE; i++) {
            for (int j = 0; j < SIZE; j++) {
                if (grid[i][j] == null) {
                    int score = simPlacement(card, i, j);
                    if (score == 0) {
                        scoreIsZero(card, i, j);
                    }
                    else if (maxScore < score) { // card completes a pokerhand for immediate points
                        maxScore = score;
                        maxRC[0] = i;
                        maxRC[1] = j;
                    }
                }
            }
        }
        return maxRC;
    }

    public int simPlacement(Card card, int r, int c) {
        Card[][] gridCopy = Arrays.copyOf(grid, grid.length);
        gridCopy[r][c] = card;
//        System.out.println("gridCopy: ");
//        for (Card[] gc : gridCopy) {
//            System.out.println(Arrays.toString(gc));
//        }
        int score = system.getScore(gridCopy);
        gridCopy[r][c] = null;
        return score;
    }

    public void scoreIsZero(Card card, int r, int c) {
        System.out.println("SCORE IS ZERO");
        simDeck = Card.getAllCards();
        System.out.println("simdeck after\n" + Arrays.toString(simDeck));

        int cardIndex = numPlays;
        while (!card.equals(simDeck[cardIndex]))
            cardIndex++;
        simDeck[cardIndex] = simDeck[numPlays];
        simDeck[numPlays] = card;

        System.out.println("simdeck before\n" + Arrays.toString(simDeck));
    }

    /* (non-Javadoc)
     * @see PokerSquaresPlayer#getName()
     */
    @Override
    public String getName() {
        return "Avery Briggs Player";
    }

    /**
     * Demonstrate AveryBriggsPlayer play with British point system.
     * @param args (not used)
     */
    public void main(String[] args) {
        PokerSquaresPointSystem system = PokerSquaresPointSystem.getBritishPointSystem();
//        System.out.println(system);
        new PokerSquares(new AveryBriggsPlayer(), system).play(); // play a single game
    }

    public String getMaxPosition(HashMap<String, ArrayList<Card>> rc) {
        Set<Map.Entry<String, ArrayList<Card>>> rcEntries = rc.entrySet();
        String maxID = "";
        for (Object o: rcEntries) {
            Map.Entry entry = (Map.Entry) o;
            String key = (String) entry.getKey();
            ArrayList<Card> a = (ArrayList<Card>) entry.getValue();
            if (maxID.equals("")) {
                maxID = key;
            }
            else if (system.getHandScore(rc.get(maxID).toArray(new Card[0])) < system.getHandScore(rc.get(key).toArray(new Card[0]))) {
                maxID = key;
            }
//            System.out.println(system.getHandScore(rc.get(maxID).toArray(new Card[0])));
        }
        return maxID;
    }

    private HashMap<String, ArrayList<Card>> genRowAndColLists() {
        HashMap<String, ArrayList<Card>> rowsAndCols = new HashMap<>();
        for (int i = 0; i < SIZE; i++) { // loop rows
            rowsAndCols.put(("r: " + (i + 1)), new ArrayList<Card>(Arrays.asList(grid[i])));
        }
        for (int c = 0; c < SIZE; c++) { // loop cols
            ArrayList<Card> cols = new ArrayList<>();
            for (int r = 0; r < SIZE; r++) { // loop rows
//                System.out.println("row: " + Arrays.toString(row) + ", col: " + col);
                cols.add(grid[r][c]);
            }
            rowsAndCols.put(("c: " + (c + 1)), cols);
        }
//        System.out.println("score: " + system.getScore(grid));
//        System.out.println("grid best row or col: " + getMaxPosition(rowsAndCols));
        return rowsAndCols;
    }

}