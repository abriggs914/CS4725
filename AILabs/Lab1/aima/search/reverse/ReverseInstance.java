package aima.search.reverse;

import java.util.ArrayList;
import java.util.List;

/**
 * @author Michael Fleming (modified Ravi Mohan's code)
 * 
 */

public class ReverseInstance {

        public static String TWO = "2";
        public static String THREE = "3";
        public static String FOUR = "4";
        public static String FIVE = "5";
        public static String SIX = "6";
        public static String SEVEN = "7";
        public static String EIGHT = "8";


	public int[] getInstance() {
		return instance;
	}

	int[] instance;

	public ReverseInstance() {
		instance = new int[] { 1, 2, 3, 4, 5, 6, 7, 8 };
	}

	public ReverseInstance(int[] anInstance) {
		instance = anInstance;
	}

        public int atLocation(int i) {
                return instance[i];
        }

        public void setValueAtLocation(int i, int v) {
		instance[i] = v;
        }

        public void setInstance(int[] nums) {
                for (int i = 0; i < 8; i++) {
                        this.setValueAtLocation(i,nums[i]);
                }
        }

        public int[] getList() {
		int[] arr = new int[] {0, 0, 0, 0, 0, 0, 0, 0};

                for (int i = 0; i < 8; i++) {
			arr[i] = this.atLocation(i);
                }
                return arr;
        }

        public void reverseFirstN(int n) {
		int temp, j;
		int max = n / 2;
		for (int i = 0; i < max; i++) {
			j = (n-1) - i;
			temp = this.atLocation(i);
			this.setValueAtLocation(i,this.atLocation(j));
			this.setValueAtLocation(j,temp);
			}
        }

	@Override
	public boolean equals(Object o) {

		if (this == o) {
			return true;
		}
		if ((o == null) || (this.getClass() != o.getClass())) {
			return false;
		}
		ReverseInstance anInstance = (ReverseInstance) o;

		for (int i = 0; i < 8; i++) {
			if (this.atLocation(i) != anInstance.atLocation(i)) {
				return false;
			}
		}
		return true;
	}


	@Override
	public String toString() {
		String retVal = instance[0] + " " + instance[1] + " " + instance[2] + " "
				+ instance[3] + " " + instance[4] + " " + instance[5] + " "
				+ instance[6] + " " + instance[7];
		return retVal;
	}

}

