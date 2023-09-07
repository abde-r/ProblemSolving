#include <iostream>

using namespace std;
int main() {
	int n, count=0;
	cin >> n;

	for (int i=0; i<n; i++)
	{
		string statement;
		cin >> statement;
		if (statement == "X++" || statement == "++X")
			count++;
		else if (statement == "X--" || statement == "--X")
			count--;
	}
	cout << count << endl;
	return 0;
}
