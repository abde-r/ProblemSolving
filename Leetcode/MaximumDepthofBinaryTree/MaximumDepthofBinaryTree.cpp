int maxDepth(TreeNode* root)
{
	if (!root)
            return 0;
        int count1=maxDepth(root->right), count2=maxDepth(root->left);
        if (count1 > count2)
            return count1+1;
        return count2+1;
}

