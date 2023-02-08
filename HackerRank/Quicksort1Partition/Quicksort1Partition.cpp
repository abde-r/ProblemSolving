vector<int> quickSort(vector<int> arr)
{
    int p=arr[0];
    vector<int> right, left, equal;
    for (int i=0; i<arr.size(); i++)
    {
        if (arr[i] > p)
            right.push_back(arr[i]);
        if (arr[i] < p)
            left.push_back(arr[i]);
        else
            equal.push_back(arr[i]);
    }
    left.insert(left.end(), equal.begin(), equal.end());
    return left;
}
