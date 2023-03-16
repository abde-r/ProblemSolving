#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int n;
    cin >> n; cin.ignore();
    for (int i = 0; i < n; i++) {
        string line;
        getline(cin, line);

        int count=0;
        for (int x=0; x<line.size(); x++)
        {
            if (line[x] == 'f' && (line[x+1] == 'f' || line[x+2] == 'f'))
            {
                count+=1;
                x+=2;
            }
            else if (line[x] == 'f' && (line[x+1] != 'f' || line[x+2] != 'f'))
                count+=1;
        }
        cout << count << endl;
    }
}

