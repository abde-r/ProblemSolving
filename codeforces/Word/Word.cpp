#include <iostream>

using namespace std;
int main() {
	int u=0, l=0;
	string word;
	cin >> word;

	for (int i=0; i<word.length(); i++) {
		if (int('A')<=int(word[i]) && int(word[i])<=int('Z'))
			u++;
		else if (int('a')<=int(word[i]) && int(word[i])<=int('z'))
			l++;
	}
	for (int i=0; i<word.length(); i++) {
		if (u>l && int(word[i])>int('Z'))
			cout << char(word[i]-32);
		else if (u<=l && int(word[i])<int('a'))
			cout << char(word[i]+32);
		else
			cout << word[i];
	}
	return 0;

}
