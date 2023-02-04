vector<int> compareTriplets(vector<int> a, vector<int> b)
{
    vector<int> v;
    int _a=0 ,_b=0;
    
    for (int i=0; i<a.size(); i++)
    {
        if (a[i] > b[i])
            _a++;
        else if (a[i] < b[i])
            _b++;
    }
    v.push_back(_a);
    v.push_back(_b);
    return v;
}

