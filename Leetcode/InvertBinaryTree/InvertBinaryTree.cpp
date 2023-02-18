TreeNode* invertTree(TreeNode* root)
{
	if (!root)
            return NULL;
        invertTree(root->right);
        invertTree(root->left);
        TreeNode *temp = root->right;
        root->right = root->left;
        root->left = temp;
        return root;
}

