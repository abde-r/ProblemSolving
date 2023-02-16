#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

int main()
{
    string s[255][255];
    int w;
    cin >> w; cin.ignore();
    int h;
    cin >> h; cin.ignore();
    int i=0, j=0;
    for (i = 0; i < h; i++) {
        for (j = 0; j < w; j++) {
            int v;
            cin >> v; cin.ignore();
            s[i][j] = to_string(v);
        }
    }
    for (int x = 0; x < i; x++)
    {
        for (int y = 0; y < j; y++)
        {
            if (s[x][y] == "0")
            {
                if ((x == 0 && y == 0) || (x == 0 && y == w-1) || (x == h-1 && y == 0) || (x == h-1 && y == w-1))
                {
                    if (x == 0 && y == 0)
                    {
                        if (s[x][y+1] == "1" && s[x+1][y] == "1" && s[x+1][y+1] == "1")
                        {
                            cout << x << " " << y << endl;
                            return 0;
                        }
                    }
                    else if (x == 0 && y == w-1)
                    {
                        if (s[x][y-1] == "1" && s[x+1][y] == "1" && s[x+1][y-1] == "1")
                        {
                            cout << x << " " << y << endl;
                            return 0;
                        }
                    }
                    else if (x == h-1 && y == 0)
                    {
                        if (s[x][y+1] == "1" && s[x-1][y] == "1" && s[x-1][y+1] == "1")
                        {
                            cout << x << " " << y << endl;
                            return 0;
                        }
                    }
                    else if (x == h-1 && y == w-1)
                    {
                        if (s[x][y-1] == "1" && s[x-1][y] == "1" && s[x-1][y-1] == "1")
                        {
                            cout << x << " " << y << endl;
                            return 0;
                        }
                    }
                }
                else if (x == 0 || x == h-1 || y == 0 || y == w-1)
                {
                    if (x == 0 || x == h-1)
                    {
                        if (x == 0)
                        {
                            if (s[x][y+1] == "1" && s[x][y-1] == "1" && s[x+1][y] == "1" && s[x+1][y-1] == "1" && s[x+1][y+1] == "1")
                            {
                                cout << y << " " << x << endl;
                                return 0;
                            }
                        }
                        else if (x == h-1)
                        {
                            if (s[x][y+1] == "1" && s[x][y-1] == "1" && s[x-1][y] == "1" && s[x-1][y-1] == "1" && s[x-1][y+1] == "1")
                            {
                                cout << y << " " << x << endl;
                                return 0;
                            }
                        }
                    }
                    else
                    {
                        if (y == 0)
                        {
                            if (s[x][y+1] == "1" && s[x+1][y] == "1" && s[x+1][y+1] == "1" && s[x-1][y] == "1" && s[x-1][y+1] == "1")
                            {
                                cout << y << " " << x << endl;
                                return 0;
                            }
                        }
                        else if (y == w-1)
                        {
                            if (s[x][y-1] == "1" && s[x+1][y] == "1" && s[x+1][y-1] == "1" && s[x-1][y] == "1" && s[x-1][y-1] == "1")
                            {
                                cout << y << " " << x << endl;
                                return 0;
                            }
                        }
                    }
                }
                else
                {
                    if (s[x][y+1] == "1" && s[x][y-1] == "1" && s[x-1][y] == "1" && s[x+1][y] == "1" && s[x-1][y-1] == "1" && s[x-1][y+1] == "1" && s[x+1][y-1] == "1" && s[x+1][y+1] == "1")
                    {
                        cout << y << " " << x << endl;
                        return 0;
                    }
                }
            }
            
        }
        
    }
}

