void staircase(int n) {
    int i,j;
    for (i=1; i<=n; i++)
    {
        j = 0;
        while (j<n-i)
        {
            cout << " ";
            j++;
        }
        while (j<n)
        {
            cout << "#";
            j++;
        }
        cout << endl;
    }
}

