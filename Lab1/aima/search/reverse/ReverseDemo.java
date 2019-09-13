/*
 * Created on Sep 16, 2008; last edited on Sept. 21, 2017
 *
 */
package aima.search.reverse;

import java.util.Iterator;
import java.util.List;
import java.util.Properties;
import java.io.*;

import aima.search.reverse.ReverseInstance;
import aima.search.reverse.ReverseGoalTest;
import aima.search.reverse.ReverseSuccessorFunction;
//import aima.search.reverse.ReverseMisplacedHeuristicFunction;
import aima.search.framework.GraphSearch;
import aima.search.framework.Problem;
import aima.search.framework.Search;
import aima.search.framework.SearchAgent;
import aima.search.framework.TreeSearch;
import aima.search.uninformed.BreadthFirstSearch;
import aima.search.uninformed.DepthFirstSearch;
import aima.search.uninformed.DepthLimitedSearch;
import aima.search.uninformed.IterativeDeepeningSearch;
//import aima.search.informed.GreedyBestFirstSearch;
//import aima.search.informed.AStarSearch;

/**
 * @author Michael Fleming (modified Ravi Mohan's code)
 * 
 */

public class ReverseDemo {
	static ReverseInstance instance1 = new ReverseInstance(
			new int[] { 4, 5, 6, 7, 3, 2, 1, 8 });;

	static ReverseInstance instance2 = new ReverseInstance(
			new int[] { 6, 7, 8, 3, 5, 4, 2, 1 });;

	static ReverseInstance instance3 = new ReverseInstance(
			new int[] { 8, 7, 1, 5, 4, 3, 6, 2 });;

	static ReverseInstance instance4 = new ReverseInstance(
			new int[] { 3, 7, 1, 4, 6, 2, 5, 8 });;

	static ReverseInstance instance5 = new ReverseInstance(
			new int[] { 2, 1, 6, 7, 3, 8, 4, 5 });;
//			new int[] { 2, 5, 4, 8, 7, 3, 1, 6 });;

	public static void main(String[] args) {

		ReverseInstance test = instance1;
		int searchType = 0;
		int testCase = 0;
		int depthLimit = 0;

		System.out.println("\nTest cases:");
		System.out.println("   Case 1:    " + instance1.toString());
		System.out.println("   Case 2:    " + instance2.toString());
		System.out.println("   Case 3:    " + instance3.toString());
		System.out.println("   Case 4:    " + instance4.toString());
		System.out.println("   Case 5:    " + instance5.toString() + "\n");

		System.out.print("Test case (1-5): ");
		try {
		  BufferedReader br = new BufferedReader(new InputStreamReader(System.in));		
		testCase = Integer.parseInt(br.readLine());
		}
		catch (IOException e) {
		   System.err.println("Error: " + e);
		}

		System.out.print("Search type (1 = BFS, 2 = DLS, 3 = IDS): ");
		try {
		  BufferedReader br2 = new BufferedReader(new InputStreamReader(System.in));		
		  searchType = Integer.parseInt(br2.readLine());
		}
		catch (IOException e) {
		   System.err.println("Error: " + e);
		}


                switch (testCase) {
                case 1:
                        test = instance1;
                        break;
                case 2:
                        test = instance2;
                        break;
                case 3:
                        test = instance3;
                        break;
                case 4:
                        test = instance4;
                        break;
                case 5:
                        test = instance5;
                        break;
		}

                switch (searchType) {
                case 1:
			reverseBFSDemo(test);
                        break;
                case 2:
			System.out.print("Depth limit: ");
			try {
			  BufferedReader br3 = new BufferedReader(new InputStreamReader(System.in));		
			  depthLimit = Integer.parseInt(br3.readLine());
			}
			catch (IOException e) {
			   System.err.println("Error: " + e);
			}
			reverseDLSDemo(test,depthLimit);
                        break;
                case 3:
			reverseIDSDemo(test);
                        break;

//                case 4:
//			reverseAStarDemo(test);
//                        break;

                }
	}

	private static void reverseBFSDemo(ReverseInstance instance) {
                System.out.println("\nReverseDemo BFS for test case " + instance.toString() + " -->");
		try {
			Problem problem = new Problem(instance,
					new ReverseSuccessorFunction(),
					new ReverseGoalTest());
			Search search = new BreadthFirstSearch(new TreeSearch());
			SearchAgent agent = new SearchAgent(problem, search);
			printActions(agent.getActions());
			printInstrumentation(agent.getInstrumentation());
		} catch (Exception e) {
			e.printStackTrace();
		}

	}

        private static void reverseDFSDemo(ReverseInstance instance) {
                System.out.println("\nReverseDemo DFS for test case " + instance.toString() + " -->");
                try {
                        Problem problem = new Problem(instance,
                                        new ReverseSuccessorFunction(), new ReverseGoalTest());
                        Search search = new DepthFirstSearch(new GraphSearch());
                        SearchAgent agent = new SearchAgent(problem, search);
                        printActions(agent.getActions());
                        printInstrumentation(agent.getInstrumentation());
                } catch (Exception e) {
                        e.printStackTrace();
                }
        }



        private static void reverseDLSDemo(ReverseInstance instance, int depth) {
                System.out.println("\nReverseDemo DLS (depth " + depth + ") for test case " + instance.toString() + " -->");
                try {
                        Problem problem = new Problem(instance,
                                        new ReverseSuccessorFunction(),
                                        new ReverseGoalTest());
                        Search search = new DepthLimitedSearch(depth);
                        SearchAgent agent = new SearchAgent(problem, search);
                        printActions(agent.getActions());
                        printInstrumentation(agent.getInstrumentation());
                } catch (Exception e) {
                        e.printStackTrace();
                }
	}


        private static void reverseIDSDemo(ReverseInstance instance) {
                System.out.println("\nReverseDemo IDS for test case " + instance.toString() + " -->");
                try {
                        Problem problem = new Problem(instance,
                                        new ReverseSuccessorFunction(), new ReverseGoalTest());
                        Search search = new IterativeDeepeningSearch();
                        SearchAgent agent = new SearchAgent(problem, search);

                        System.out.println();
                        printActions(agent.getActions());
                        printInstrumentation(agent.getInstrumentation());
                } catch (Exception e) {
                        e.printStackTrace();
                }
        }

/*
        private static void reverseGreedyBestFirstDemo(ReverseInstance instance) {
		System.out.println("\nReverseDemo Greedy for test case " + instance.toString() + " -->");
                try {
                        Problem problem = new Problem(instance,
                                        new ReverseSuccessorFunction(),
                                        new ReverseGoalTest(),
                                        new ReverseMisplacedHeuristicFunction());
                        Search search = new GreedyBestFirstSearch(new GraphSearch());
                        SearchAgent agent = new SearchAgent(problem, search);
                        printActions(agent.getActions());
                        printInstrumentation(agent.getInstrumentation());
                } catch (Exception e) {
                        e.printStackTrace();
                }
                
        }

	private static void reverseAStarDemo(ReverseInstance instance) {
		System.out.println("\nReverseDemo A* for test case " + instance.toString() + " -->");
		try {
			Problem problem = new Problem(instance,
					new ReverseSuccessorFunction(),
					new ReverseGoalTest(),
					new ReverseMisplacedHeuristicFunction());
			Search search = new AStarSearch(new GraphSearch());
			SearchAgent agent = new SearchAgent(problem, search);
			printActions(agent.getActions());
			printInstrumentation(agent.getInstrumentation());
		} catch (Exception e) {
			e.printStackTrace();
		}

	}
*/

	private static void printInstrumentation(Properties properties) {
		Iterator keys = properties.keySet().iterator();
		while (keys.hasNext()) {
			String key = (String) keys.next();
			String property = properties.getProperty(key);
			System.out.println(key + " : " + property);
		}

	}

	private static void printActions(List actions) {
		for (int i = 0; i < actions.size(); i++) {
			String action = (String) actions.get(i);
			System.out.println(action);
		}
	}

}
