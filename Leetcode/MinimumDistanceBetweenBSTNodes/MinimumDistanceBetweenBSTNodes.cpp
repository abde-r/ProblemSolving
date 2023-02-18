vector<int> v;
void get_mindis( TreeNode *root )
{
        if (!root)
            return ;
        minDiffInBST(root->right);
        minDiffInBST(root->left);
        v.push_back(root->val);
}

int minDiffInBST(TreeNode* root)
{
        int temp = INT_MAX;
        get_mindis(root);
        sort(v.begin(), v.end());
        for (int i=1; i<v.size(); i++)
            if (temp > v[i]-v[i-1])
                temp = v[i]-v[i-1];
        return temp;
}

