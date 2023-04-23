bool isSameTree(TreeNode* p, TreeNode* q)
{
        if (!p && !q)
            return 1;
        if ((!p && q) || (p && !q))
            return 0;
        if (p->val != q->val)
            return 0;
        return isSameTree(p->right, q->left) && isSameTree(p->left, q->right);
}

    bool isSymmetric(TreeNode* root)
{
	return isSameTree(root->right, root->left);
}
