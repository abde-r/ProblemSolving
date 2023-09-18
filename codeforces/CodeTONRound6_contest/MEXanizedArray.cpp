#include <iostream>

using namespace std;
int main() {
    int m;
    cin >> m;

    for (int i=0; i<m; i++) {
        int n,k,x;
        cin >> n >> k >> x;

        if (n>=k && x+1>=k) {
            int temp=0;
            for (int i=0;i<k;i++)
                temp+=i;
            if (x==k)
                x-=1;
            for (int i=0;i<(n-k);i++)
                temp+=x;
            cout << temp << endl;
        }
        else
            cout << -1 << endl;
    }
    return 0;
}