#include <iostream>

using namespace std;
int main() {
	int r=0;
	string s1, s2;
	cin >> s1 >> s2;

	for (int i=0; s1[i] && s2[i]; i++) {
		if (isupper(s1[i])) {
			if (toupper(s2[i]) > s1[i])
				r = -1;
			else if (toupper(s2[i]) < s1[i])
				r = 1;
		}
		else if (islower(s1[i])) {
			if (tolower(s2[i]) > s1[i])
				r = -1;
			else if (tolower(s2[i]) < s1[i])
				r = 1;
		}
		if (r != 0)
			break;
	}
	cout << r << endl;
	return 0;

}
