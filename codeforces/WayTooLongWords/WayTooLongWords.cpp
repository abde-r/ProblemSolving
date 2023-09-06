#include <iostream>

using namespace std;

int main() {
	int n;
	cin >> n;

	for (int i=0; i<n; i++)
	{
		string word;
		cin >> word;
		if (word.length()>=1 && word.length() > 10 && word.length()<=100)
		{
			cout << word[0] << word.length()-2 << word[word.length()-1] << endl;
		}
		else
			cout << word << endl;
		}
	return 0;
}
