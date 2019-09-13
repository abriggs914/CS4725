/*
 * Created on Sep 16, 2008
 *
 */
package aima.search.reverse;

import java.util.ArrayList;
import java.util.List;

import aima.search.framework.Successor;
import aima.search.framework.SuccessorFunction;

/**
 * @author Michael Fleming (modified Ravi Mohan's code)
 * 
 */

public class ReverseSuccessorFunction implements SuccessorFunction {

	public List getSuccessors(Object state) {
		ReverseInstance instance = (ReverseInstance) state;
		List<Successor> successors = new ArrayList<Successor>();
			ReverseInstance newInstance2 = copyOf(instance);
			ReverseInstance newInstance3 = copyOf(instance);
			ReverseInstance newInstance4 = copyOf(instance);
			ReverseInstance newInstance5 = copyOf(instance);
			ReverseInstance newInstance6 = copyOf(instance);
			ReverseInstance newInstance7 = copyOf(instance);
			ReverseInstance newInstance8 = copyOf(instance);

			newInstance2.reverseFirstN(2);
			successors.add(new Successor(ReverseInstance.TWO, newInstance2));

			newInstance3.reverseFirstN(3);
			successors.add(new Successor(ReverseInstance.THREE, newInstance3));

			newInstance4.reverseFirstN(4);
			successors.add(new Successor(ReverseInstance.FOUR, newInstance4));

			newInstance5.reverseFirstN(5);
			successors.add(new Successor(ReverseInstance.FIVE, newInstance5));

			newInstance6.reverseFirstN(6);
			successors.add(new Successor(ReverseInstance.SIX, newInstance6));

			newInstance7.reverseFirstN(7);
			successors.add(new Successor(ReverseInstance.SEVEN, newInstance7));

			newInstance8.reverseFirstN(8);
			successors.add(new Successor(ReverseInstance.EIGHT, newInstance8));

		return successors;
	}

	private ReverseInstance copyOf(ReverseInstance instance) {
		ReverseInstance newInstance = new ReverseInstance();
		newInstance.setInstance(instance.getList());
		return newInstance;
	}

}
