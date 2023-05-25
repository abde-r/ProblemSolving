#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    vector<string> t;
    
    for (int i = 0; i < 3; i++) {
        string line;
        getline(cin, line);
        t.push_back(line);
    }

    int i=0;
    for (; i<t.size(); i++)
        if (count(t[i].begin(), t[i].end(), '.') != t[i].size())
            break;
    
    if (i == t.size())
    {
        cout << "false" << endl;
        exit(1);
    }
    else
    {
        string so1;
        so1 += t[0][0];
        so1 += t[1][0];
        so1 += t[2][0];

        string so2;
        so2 += t[0][1];
        so2 += t[1][1];
        so2 += t[2][1];

        string so3;
        so3 += t[0][2];
        so3 += t[1][2];
        so3 += t[2][2];
        
        string d1;
        d1 += t[0][0];
        d1 += t[1][1];
        d1 += t[2][2];

        string d2;
        d2 += t[0][2];
        d2 += t[1][1];
        d2 += t[2][0];


        // horizontals
        if (count(t[0].begin(), t[0].end(), 'O') == 2 && count(t[0].begin(), t[0].end(), '.') == 1)
            t[0] = "OOO";
        else if (count(t[1].begin(), t[1].end(), 'O') == 2 && count(t[1].begin(), t[1].end(), '.') == 1)
            t[1] = "OOO";
        else if (count(t[2].begin(), t[2].end(), 'O') == 2 && count(t[2].begin(), t[2].end(), '.') == 1)
            t[2] = "OOO";
    
        // verticals
        else if (count(so1.begin(), so1.end(), 'O') > 1 && count(so1.begin(), so1.end(), '.') == 1)
        {
            if (t[0][0] == '.') t[0][0] = 'O';
            else if (t[1][0] == '.') t[1][0] = 'O';
            else if (t[2][0] == '.') t[2][0] = 'O';
        }
        else if (count(so2.begin(), so2.end(), 'O') > 1 && count(so2.begin(), so2.end(), '.') == 1)
        {
            if (t[0][1] == '.') t[0][1] = 'O';
            else if (t[1][1] == '.') t[1][1] = 'O';
            else if (t[2][1] == '.') t[2][1] = 'O';
        }

        else if (count(so3.begin(), so3.end(), 'O') > 1 && count(so3.begin(), so3.end(), '.') == 1)
        {
            if (t[0][2] == '.') t[0][2] = 'O';
            else if (t[1][2] == '.') t[1][2] = 'O';
            else if (t[2][2] == '.') t[2][2] = 'O';
        }

        // diagonales
        else if (count(d1.begin(), d1.end(), 'O') > 1 && count(d1.begin(), d1.end(), '.') == 1)
        {
            if (t[0][0] == '.') t[0][0] = 'O';
            else if (t[1][1] == '.') t[1][1] = 'O';
            else if (t[2][2] == '.') t[2][2] = 'O';
        }
        else if (count(d2.begin(), d2.end(), 'O') > 1 && count(d2.begin(), d2.end(), '.') == 1)
        {
            if (t[0][2] == '.') t[0][2] = 'O';
            else if (t[1][1] == '.') t[1][1] = 'O';
            else if (t[2][0] == '.') t[2][0] = 'O';
        }
        else
        {
            cout << "false" << endl;
            exit(1);
        }
    
        for (int i=0; i<t.size(); i++)
            cout << t[i] << endl;
    }
}

