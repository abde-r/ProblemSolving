vector<int> reverseArray(vector<int> a)
{
    int x = a.size()-1;
    for (int i = 0; i<=x; i++)
    {
        a.push_back(a[x-i]);
        a.erase(next(a.begin(), x-i));
    }
    return a;
}

