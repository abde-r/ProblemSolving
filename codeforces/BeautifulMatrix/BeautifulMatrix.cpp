#include <iostream>
#include <vector>

using namespace std;

vector<int> one_position(int t[5][5]) {
	for (int i=0; i<5; i++) {
		for (int j=0; j<5; j++) {
			if (t[i][j] == 1) {
				vector<int> v={i+1,j+1};
				return v;
			}
		}
	}
	return  {-1, -1};
}

int main() {
	vector<int> v;
	int t[5][5];
	int moves=0;

	for (int i=0; i<5; i++) {
		for (int j=0; j<5; j++) {
			int n;
			cin >> n;
			t[i][j] = n;
		}
	}

	v = one_position(t);
	
	if (v[0] == 1 || v[0] == 5)
		moves+=2;
	if (v[0] == 2 || v[0] == 4)
		moves++;
	if (v[1] == 1 || v[1] == 5)
		moves+=2;
	if (v[1] == 2 || v[1] == 4)
		moves++;
	cout << moves << endl;
	return 0;
}
