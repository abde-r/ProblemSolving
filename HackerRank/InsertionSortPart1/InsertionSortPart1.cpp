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

void insertionSort1(int n, vector<int> arr)
{
    int temp;
    int i= n-1;
    while (arr[i] < arr[i-1])
    {
        temp = arr[i];
        arr[i] = arr[i-1];
        print_vector(arr);
        arr[i-1] = temp;
        i--;
    }
    print_vector(arr);
}

