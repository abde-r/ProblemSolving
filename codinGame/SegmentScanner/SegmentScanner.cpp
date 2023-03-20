#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    string line_1;
    getline(cin, line_1);
    string line_2;
    getline(cin, line_2);
    string line_3;
    getline(cin, line_3);

    for (int i=0; i<line_1.size(); i++)
    {
        if (line_1[i+1] == '_' && (line_2[i] == '|' && line_2[i+1] == ' ' && line_2[i+2] == '|') && line_3[i+1] == '_')
            cout << 0;
        else if (line_1[i+1] == '_' && (line_2[i] == '|' && line_2[i+1] == '_' && line_2[i+2] == '|') && (line_3[i] == '|' && line_3[i+1] == '_' && line_3[i+2] == '|'))
            cout << 8;
        else if (line_1[i+1] == '_' && (line_2[i] == '|' && line_2[i+1] == '_' && line_2[i+2] == '|') && (line_3[i+1] == '_' && line_3[i+2] == '|'))
            cout << 9;
        else if (line_1[i+1] == ' ' && (line_2[i] == ' ' && line_2[i+1] == ' ' && line_2[i+2] == '|') && (line_3[i] == ' ' && line_3[i+1] == ' ' && line_3[i+2] == '|'))
            cout << 1;
        else if (line_1[i+1] == '_' && (line_2[i+2] == '|' && line_2[i+1] == '_') && (line_3[i+1] == '_') && line_3[i] == '|')
            cout << 2;
        else if (line_1[i+1] == '_' && (line_2[i] == ' ' && line_2[i+1] == '_' && line_2[i+2] == '|') && (line_3[i] == ' ' && line_3[i+1] == '_' && line_3[i+2] == '|'))
            cout << 3;
        else if (line_1[i+1] == ' ' && (line_2[i] == '|' && line_2[i+1] == '_' && line_2[i+2] == '|') && (line_3[i] == ' ' && line_3[i+1] == ' ' && line_3[i+2] == '|'))
            cout << 4;
        else if (line_1[i+1] == '_' && (line_2[i] == '|' && line_2[i+1] == '_') && (line_3[i] == '|' && line_3[i+1] == '_' && line_3[i+2] == '|'))
            cout << 6;
        else if (line_1[i+1] == '_' && (line_2[i] == ' ' && line_2[i+1] == ' ' && line_2[i+2] == '|') && line_3[i+2] == '|')
            cout << 7;
        else if (line_1[i+1] == '_' && (line_2[i] == '|' && line_2[i+1] == '_') && (line_3[i+1] == '_') && line_3[i+2] == '|')
            cout << 5;
    }
}

