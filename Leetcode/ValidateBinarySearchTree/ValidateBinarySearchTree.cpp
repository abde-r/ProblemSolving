vector<int> v1,v2;
void fill_vector( TreeNode* root )
{
        if (!root)
            return ;
        fill_vector(root->right);
        v1.push_back(root->val);
        fill_vector(root->left);
}

bool isValidBST(TreeNode* root)
{
        fill_vector(root);
        for (int i=1; i<v1.size(); i++)
            if (v1[i] >= v1[i-1])
                return false;
        return true;
}
