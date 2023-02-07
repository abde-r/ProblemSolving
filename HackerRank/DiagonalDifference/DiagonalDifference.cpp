int diagonalDifference(vector<vector<int>> arr)
{
    int d1=0, d2=0, x=arr.size()-1;
    for (int i=0; i<arr.size(); i++)
    {
        d1+= arr[i][i];
        d2+= arr[i][x];
        x--;
    }
    return abs(d1-d2);
}

