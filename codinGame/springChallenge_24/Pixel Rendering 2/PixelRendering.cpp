#include <iostream>
#include <string.h>
#include <vector>
#include <algorithm>
#include <stdio.h>
using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

vector<string> init_pic(int n) {
    vector<string> pic;

    for(int i=0; i<n; i++) {
        string temp = "";
        for(int j=0; j<n; j++)
            temp+='.';
        pic.push_back(temp);
    }
    return pic;
}

vector<string> parse_command(string command) {
    char *v = &command[0]; 
    vector<string> s;

    char *ptr = strtok(v, " "); 
    while (ptr != NULL)  
    {  
        s.push_back(ptr);
        ptr = strtok(NULL, " ");  
    }
    return s; 
}

int main()
{
    int n;
    cin >> n; cin.ignore();

    vector<string> pic = init_pic(n);

    // game loop
    while (1) {
        string command;
        getline(cin, command);
        vector<string> s = parse_command(command);

        for (int i = 0; i < n; i++) {
            if (s[0] == "C") {
                for(int j=0; j<n; j++)
                    if (j == stoi(s[1]))
                        pic[i][j] = '#';
            }
            else if (s[0] == "R" && i == stoi(s[1])) {
                for(int j=0; j<n; j++)
                    pic[i][j] = '.';
            }
        }

        for (int i=0; i<n; i++)
            cout << pic[i] << endl;   
    }
}