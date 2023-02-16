#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    vector<int> p,g;
    int n;
    cin >> n; cin.ignore();
    for (int i = 0; i < n; i++) {
        int t;
        cin >> t; cin.ignore();
        (t>0) ? p.push_back(t) : g.push_back(t);
    }

    if (p.size() || g.size())
    {
        int min_pos, min_neg;
        (p.size()) ?  min_pos = *min_element(p.begin(), p.end()) : min_pos = 5526;
        (g.size()) ? min_neg = *max_element(g.begin(), g.end()) : min_neg = -273;
        (min_pos > abs(min_neg)) ? cout <<  min_neg << endl : cout <<  min_pos << endl;
    }
    else
        cout <<  0 << endl;
}

