void print_vector( vector<int> v )
{
    for (int i=0; i<v.size(); i++)
    {
        cout << v[i];
        if (i != v.size()-1)
            cout << " ";
    }
    cout << endl;
}

void insertionSort2(int n, vector<int> arr)
{
    int temp, x;
    for (int i=1; i<arr.size(); i++)
    {
        x = i;
        while (arr[x] < arr[x-1])
        {
            temp = arr[x];
            arr[x] = arr[x-1];
            arr[x-1] = temp;
            x--;
        }
        print_vector(arr);
    }
}

