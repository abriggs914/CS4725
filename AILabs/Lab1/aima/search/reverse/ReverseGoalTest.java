/*
 * Created on Sep 16, 2008
 *
 */
package aima.search.reverse;

import aima.search.framework.GoalTest;

/**
 * @author Michael Fleming (modified Ravi Mohan's code)
 * 
 */

public class ReverseGoalTest implements GoalTest {
	ReverseInstance goal = new ReverseInstance(new int[] { 1, 2, 3, 4, 5,
			6, 7, 8 });

	public boolean isGoalState(Object state) {
		ReverseInstance instance = (ReverseInstance) state;
		return instance.equals(goal);
	}

}
