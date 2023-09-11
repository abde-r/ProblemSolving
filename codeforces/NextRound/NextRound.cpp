#include <iostream>
#include <vector>

using namespace std;
int main() {
	int n, k, count=0;
	vector<int> t;
	cin >> n >> k;

	if (k>=1 && k<=n && n>=1 && n<=50) {
		for (int i=0; i<n; i++) {
			int cont;
			cin >> cont;
			t.push_back(cont);
		}
	}
	int v=t[k-1];
	for (int i=0; i<t.size(); i++) {
		if (t[i] >= v && t[i])
			count++;
	}
	cout << count << endl;
	return 0;
}
