﻿
public class TreeNode
{
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null)
    {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class Solution
{
    public static TreeNode InvertTree(TreeNode root)
    {
        TreeNode tempNode = root;
        if (root == null)
            return root;

        (root.right, root.left) = (root.left, root.right);

        InvertTree(root.right);
        InvertTree(root.left);

        return tempNode;
    }
}