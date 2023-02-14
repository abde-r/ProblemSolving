#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    int temp=INT_MAX;
    vector<int> t;
    cin >> n; cin.ignore();
    for (int i = 0; i < n; i++) {
        int pi;
        cin >> pi; cin.ignore();
        t.push_back(pi);
    }
    sort(t.begin(), t.end());
    for (int i = 0; i < t.size()-1; i++)
        if (temp > t[i+1]-t[i])
            temp = t[i+1]-t[i];
    cout << temp << endl;
}

