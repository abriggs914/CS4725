/*
*	CS2383
*	Programming Assignment 2
*   Nov 2018
*	Question 2
* 	Avery Briggs
*	3471065	
*
*
*	Java Program to print out
*   the preOrder, inOrder and
*   postOrders of a given binary
*   tree.
*/

public class TreeOrder{

    public static Node root;    // root of the tree
    public static int n;    // holds the array size
    public static int count;   // used for printing purposes

    private static class Node{
        int iD;
        int data;
        Node parent;
        Node left;
        Node right;
    }

    public static void main(String[] args){
        int[] treeArr = {12, 10, 19, 13, 15, 14, 18};
        n = treeArr.length;
        printArr(treeArr);
        Node[] tree = initTree(treeArr);
        System.out.println("\nPreOrder:");
        preOrder(root);
        System.out.println("\nInOrder:");
        inOrder(root);
        System.out.println("\nPostOrder:");
        postOrder(root);
    }

    // Prints the contents of an array
    public static void printArr(int[] arr){
        int i;
        System.out.print("Array { ");
        for(i = 0; i < n; i++){
            System.out.print(arr[i] + ((i < n - 1)? ",":"") + " ");
        }
        System.out.println("}");
    }

    // Prints the data of a node and stores the value to the trees corresponding array 
    public static void visit(Node node, int i){
        if(count == 0){
            System.out.print("\t{ ");
        }
        System.out.print(node.data + ((i < n - 1)? ",":"") + " ");
        if(count == n - 1){
            System.out.println("}");
            count = 0;
        }
        else{
            count++;
        }
    }

    public static void preOrder(Node node){
        if(node != null){
            visit(node, count);
            preOrder(node.left);
            preOrder(node.right);
        }
    }

    public static void inOrder(Node node){
        if(node != null){
            inOrder(node.left);
            visit(node, count);
            inOrder(node.right);
        }
    }

    public static void postOrder(Node node){
        if(node != null){
            postOrder(node.left);
            postOrder(node.right);
            visit(node, count);
        }
    }

    // Tree is hard coded using previous knowledge of how
    // it is supposed to be structured.
    public static Node[] initTree(int[] arr){
        int i;
        Node[] tree = new Node[n];
        Node node;
        for(i = 0; i < n; i++){
            node = new Node();
            node.data = arr[i];
            tree[i] = node;
        }
        tree[0].data = arr[0];
        tree[1].data = arr[1];
        tree[2].data = arr[2];
        tree[3].data = arr[3];
        tree[4].data = arr[4];
        tree[5].data = arr[5];
        tree[6].data = arr[6];

        tree[0].parent = null;
        tree[0].left = tree[1];
        tree[0].right = tree[2];

        tree[1].parent = tree[0];
        tree[1].left = null;
        tree[1].right = tree[3];

        tree[2].parent = tree[0];
        tree[2].left = tree[4];
        tree[2].right = null;
        
        tree[3].parent = tree[1];
        tree[3].left = null;
        tree[3].right = null;

        tree[4].parent = tree[2];
        tree[4].left = tree[5];
        tree[4].right = tree[6];

        tree[5].parent = tree[4];
        tree[5].left = null;
        tree[5].right = null;

        tree[6].parent = tree[4];
        tree[6].left = null;
        tree[6].right = null;

        root = tree[0];
        return tree;   
    }

    // I had implemented the algorithms to place all nodes for a binary
    // search tree. Then I noticed that the tree in the question isn't a
    // binary search tree.

    // public static void bstInsertRecurs(Node rt, Node node){
    //     if(node.data <= rt.data){
    //         if(rt.left == null){
    //             rt.left = node;
    //             node.parent = rt;
    //         }
    //         else{
    //             bstInsertRecurs(rt.left, node);
    //         }
    //     }
    //     else{
    //         if(rt.right == null){
    //             rt.right = node;
    //             node.parent = rt;
    //         }
    //         else{
    //             bstInsertRecurs(rt.right, node);
    //         }
    //     }
    // }

    // public static Node bstInsert(Node rt, int val, int index){
    //     int i;
    //     Node node = new Node();
    //     node.data = val;
    //     node.iD = index;
    //     node.left = node.right = null;
    //     if(rt == null){
    //         root = node;
    //         return node;
    //     }
    //     bstInsertRecurs(rt, node);
    //     // for(i = 0; i < n; i++){
    //     //     System.out.println("i: " + i);
    //     //     node.data = arr[i];
    //     //     tree[i] = node;
    //     //     if(i == 0){
    //     //         root = node;
    //     //         root.left = root.right = null;
    //     //     }
    //     // }
    //     return node;
    // }
}