#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;

    for (int i=0; i<n; i++) {
        int a, r=1, key=0, min_value;
        cin >> a;
        vector<int> t;

        for (int x=0; x<a; x++) {
            int m;
            cin >> m;
            t.push_back(m);
        }

        min_value = *(std::min_element(t.begin(), t.end()));
        
        for (int x=0; x<a; x++) {
            if (t[x] == min_value && !key) {
                t[x]+=1;
                key=1;
            }
            r*=t[x];
        }
        cout << r << endl;
    }

    return 0;
}