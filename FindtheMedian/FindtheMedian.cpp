int findMedian(vector<int> arr)
{
    sort(arr.begin(), arr.end());
    cout << arr[arr.size()/2] << endl;
    return arr[arr.size()/2];
}

