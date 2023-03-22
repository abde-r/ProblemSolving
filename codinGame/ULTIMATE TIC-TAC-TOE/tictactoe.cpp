#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Play
{
    public:
        Play( int _id, int _type) : id(_id), type(_type) {}
        ~Play() {};

        int id;
        char type;
};

int main()
{
    vector<string> t;
    t.push_back("---");
    t.push_back("---");
    t.push_back("---");
    int index = 0;
    int play_first=0;
    int ko=0;
    int he_centered=0;
    int we_defend=0;
    string my_last_play="";
    string his_last_play="";
    string op_first_play="";

    while (1) {
        int opponent_row;
        int opponent_col;
        cin >> opponent_row >> opponent_col; cin.ignore();
        int valid_action_count;
        cin >> valid_action_count; cin.ignore();
            int row;
            int col;
        for (int i = 0; i < valid_action_count; i++) {
            cin >> row >> col; cin.ignore();
            cerr << row << " " << col << endl;
            if (opponent_row!= -1 && opponent_col!=-1)
            {
                if (index == 0)
                    op_first_play = to_string(opponent_row)+to_string(opponent_col);
                t[opponent_row][opponent_col] = 'O';
                his_last_play = to_string(opponent_row)+to_string(opponent_col);
            }
        }
        
        // we check if I play first
        if (opponent_row==-1 && opponent_col==-1 && index == 0)
        {
            // I put my X in the top right corner
            cout << "0 2" << endl;
            t[0][2] = 'X';

            // I indicate that I play first
            play_first = 1;
            my_last_play = "02";
        }
        else if (opponent_row!=-1 && opponent_col!=-1 && index == 0)
        {
            // I put my X in the top right corner if it's available, otherwise I put it in the center
            if (t[1][1] == '-')
            {
                cout << "1 1" << endl;
                t[1][1] = 'X';
            }
            else
            {
                cout << "0 2" << endl;
                t[0][2] = 'X';
            }
            // I indicate that he plays first
            play_first = 0;
        }
        if (index == 1 && play_first == 1) // the second roud and I played first
        {
            // all the cases
            if (his_last_play == "00")
            {
                cout << "2 2" << endl;
                t[2][2] = 'X';
            }
            else if (his_last_play == "01")
            {
                cout << "2 2" << endl;
                t[2][2] = 'X';
            }
            else if (his_last_play == "10")
            {
                cout << "2 2" << endl;
                t[2][2] = 'X';
            }
            else if (his_last_play == "12")
            {
                cout << "0 0" << endl;
                t[0][0] = 'X';
            }
            else if (his_last_play == "20")
            {
                cout << "0 0" << endl;
                t[0][0] = 'X';
            }
            else if (his_last_play == "21")
            {
                cout << "0 0" << endl;
                t[0][0] = 'X';
            }
            else if (his_last_play == "22")
            {
                cout << "0 0" << endl;
                t[0][0] = 'X';
            }
            else
            {
                cout << "2 0" << endl;
                t[2][0] = 'X';
                he_centered = 1;
            }

        }
        else if (index == 1 && play_first == 0) // the second roud and he played first
        {
            // we check his last play
            if ((t[0][2] == 'O' && t[2][0] == 'O') || (t[0][0] == 'O' && t[2][2] == 'O')) // if choose both the corners
            {
                cout << "1 2" << endl;
                t[1][2] = 'X';
                we_defend = 1;
            }
            else if ((t[0][2] == 'O' && t[0][1] == 'O') || (t[0][2] == 'O' && t[0][0] == 'O') || (t[0][2] == 'O' && t[1][2] == 'O') || (t[0][2] == 'O' && t[2][2] == 'O'))
            {
                // he got one play on the right top corner
                if (t[0][2] == 'O' && t[0][1] == 'O')
                {
                    cout << "0 0" << endl;
                    t[0][0] = 'X';
                }
                else if (t[0][2] == 'O' && t[0][0] == 'O')
                {
                    cout << "0 1" << endl;
                    t[0][1] = 'X';
                }
                else if (t[0][2] == 'O' && t[1][2] == 'O')
                {
                    cout << "2 2" << endl;
                    t[2][2] = 'X';
                }
                else if (t[0][2] == 'O' && t[2][2] == 'O')
                {
                    cout << "1 2" << endl;
                    t[1][2] = 'X';
                }
                we_defend = 1;
            }
            else if ((t[0][0] == 'O' && t[0][1] == 'O') || (t[0][0] == 'O' && t[0][2] == 'O') || (t[0][0] == 'O' && t[1][0] == 'O') || (t[0][0] == 'O' && t[2][0] == 'O'))
            {
                // he got one play on the left top corner
                if (t[0][0] == 'O' && t[0][1] == 'O')
                {
                    cout << "0 2" << endl;
                    t[0][2] = 'X';
                }
                else if (t[0][0] == 'O' && t[0][2] == 'O')
                {
                    cout << "0 1" << endl;
                    t[0][1] = 'X';
                }
                else if (t[0][0] == 'O' && t[1][0] == 'O')
                {
                    cout << "2 0" << endl;
                    t[2][0] = 'X';
                }
                else if (t[0][0] == 'O' && t[2][0] == 'O')
                {
                    cout << "1 0" << endl;
                    t[1][0] = 'X';
                }
                we_defend = 1;
            }
            else if ((t[2][2] == 'O' && t[1][2] == 'O') || (t[2][2] == 'O' && t[0][2] == 'O') || (t[2][2] == 'O' && t[2][0] == 'O') || (t[2][2] == 'O' && t[2][1] == 'O'))
            {
                // he got one play on the right bottom corner
                if (t[2][2] == 'O' && t[1][2] == 'O')
                {
                    cout << "0 2" << endl;
                    t[0][2] = 'X';
                }
                else if (t[2][2] == 'O' && t[0][2] == 'O')
                {
                    cout << "1 2" << endl;
                    t[1][2] = 'X';
                }
                else if (t[2][2] == 'O' && t[2][0] == 'O')
                {
                    cout << "2 1" << endl;
                    t[2][1] = 'X';
                }
                else if (t[2][2] == 'O' && t[2][1] == 'O')
                {
                    cout << "2 0" << endl;
                    t[2][0] = 'X';
                }
                we_defend = 1;
            }
            else if ((t[2][0] == 'O' && t[1][0] == 'O') || (t[2][0] == 'O' && t[0][0] == 'O') || (t[2][0] == 'O' && t[2][1] == 'O') || (t[2][0] == 'O' && t[2][2] == 'O'))
            {
                // he got one play on the left bottom corner
                if (t[2][0] == 'O' && t[1][0] == 'O')
                {
                    cout << "0 0" << endl;
                    t[0][0] = 'X';
                }
                else if (t[2][0] == 'O' && t[0][0] == 'O')
                {
                    cout << "1 0" << endl;
                    t[1][0] = 'X';
                }
                else if (t[2][0] == 'O' && t[2][1] == 'O')
                {
                    cout << "2 2" << endl;
                    t[2][2] = 'X';
                }
                else if (t[2][0] == 'O' && t[2][2] == 'O')
                {
                    cout << "2 1" << endl;
                    t[2][1] = 'X';
                }
                we_defend = 1;
            }
            else if ((t[0][1] == 'O' && t[2][1] == 'O') || (t[1][2] == 'O' && t[1][0] == 'O')) // he got a strict line
            {
                // mcha
                cout << "0 2" << endl;
                t[0][2] = 'X';
            }
            else
            {
                // i got to figure out the best corner to play in
                if (his_last_play == "21")
                {
                    cout << "2 2" << endl;
                    t[2][2] = 'X';
                }
                else if (his_last_play == "10")
                {
                    cout << "0 0" << endl;
                    t[0][0] = 'X';
                }
            }
        }

        if (index == 2 && play_first == 1 && he_centered == 0) // the third roud and I played first
        {
            if (t[0][2] == 'X' && t[1][2] == '-' && t[2][2] == 'X') // he didnt notice it
            {
                cout << "1 2" << endl;
            }
            else if (t[0][2] == 'X' && t[0][1] == '-' && t[0][0] == 'X')
            {
                cout << "0 1" << endl;
            }
            else if (t[2][0] == 'X' && t[2][1] == 'X' && t[2][2] == '-')
            {
                cout << "2 1" << endl;
            }
            else // if he noticed
            {
                if (t[1][0] == 'O' && t[1][2] == 'O')
                {
                    cout << "1 1" << endl;
                    t[1][1] = 'X';
                }
                else if (t[0][1] == 'O' && t[0][2] == 'O')
                {
                    cout << "1 1" << endl;
                    t[1][1] = 'X';
                }
                else if (op_first_play == "02")
                {
                    cout << "0 0" << endl;
                    t[0][0] = 'X';
                }
                else if (t[2][0] == '-')
                {
                    cout << "2 0" << endl;
                    t[2][0] = 'X';
                }
                else if (t[2][2] == '-')
                {
                    cout << "2 2" << endl;
                    t[2][2] = 'X';
                }
                else // Mzmoot
                {
                    if (t[0][2] == 'X' && t[1][1] == '-' && t[2][0] == 'X')
                        cout << "1 1" << endl;
                }
                ko = 1;
            }
        }
        else if (index == 2 && play_first == 1 && he_centered == 1) // the third roud and I played first and he centered
        {
            if (t[0][2] == 'X' && t[1][2] == '-' && t[2][2] == 'X') // he didnt notice it
            {
                cout << "1 2" << endl;
            }
            else if (t[0][2] == 'X' && t[0][1] == '-' && t[0][0] == 'X')
            {
                cout << "0 1" << endl;
            }
            else if (t[2][0] == 'X' && t[2][1] == 'X' && t[2][2] == '-')
            {
                cout << "2 1" << endl;
            }
            if (his_last_play == "22" || his_last_play == "00") // he filled the corners
            {
                // cho9ha
                if (his_last_play == "00")
                {
                    cout << "2 2" << endl;
                    t[2][2] = 'X';
                }
                else
                {
                    cout << "0 0" << endl;
                    t[0][0] = 'X';
                }
                ko = 1;
            }
            else
            {
                // we defend
                if (his_last_play == "00")
                {
                    cout << "2 2" << endl;
                    t[2][2] = 'X';
                }
                else if (his_last_play == "01")
                {
                    cout << "2 1" << endl;
                    t[2][1] = 'X';
                }
                else if (his_last_play == "10")
                {
                    cout << "1 2" << endl;
                    t[1][2] = 'X';
                }
                else if (his_last_play == "12")
                {
                    cout << "1 0" << endl;
                    t[1][0] = 'X';
                }
                else if (his_last_play == "21")
                {
                    cout << "0 1" << endl;
                    t[0][1] = 'X';
                }
                else
                {
                    cout << "0 0" << endl;
                    t[0][0] = 'X';
                }
                we_defend = 1;
            }
        }
        else if (index == 2 && play_first == 0) // the third roud and he played first
        {
            // if he didn't notice
            if (t[0][2] == 'X' && t[1][1] == 'X')
            {
                cout << "2 0" << endl;
            }
            else if (t[0][0] == 'X' && t[1][1] == 'X')
            {
                cout << "2 2" << endl;
            }
            else if (t[1][1] == 'X' && t[1][2] == 'X')
            {
                cout << "1 0" << endl;
            }
            else
            {
                // just anywhere
                if (t[0][0] == '-')
                {
                    cout << "0 0" << endl;
                    t[0][0] = 'X';
                }
                else if (t[0][1] == '-')
                {
                    cout << "0 1" << endl;
                    t[0][1] = 'X';
                }
                else if (t[0][2] == '-')
                {
                    cout << "0 2" << endl;
                    t[0][2] = 'X';
                }

                else if (t[1][0] == '-')
                {
                    cout << "1 0" << endl;
                    t[1][0] = 'X';
                }
                else if (t[1][1] == '-')
                {
                    cout << "1 1" << endl;
                    t[1][1] = 'X';
                }
                else if (t[1][2] == '-')
                {
                    cout << "1 2" << endl;
                    t[1][2] = 'X';
                }

                else if (t[2][0] == '-')
                {
                    cout << "2 0" << endl;
                    t[2][0] = 'X';
                }
                else if (t[2][1] == '-')
                {
                    cout << "2 1" << endl;
                    t[2][1] = 'X';
                }
                else if (t[2][2] == '-')
                {
                    cout << "2 2" << endl;
                    t[2][2] = 'X';
                }
                we_defend = 1;
            }
        }

        if (index == 3 && play_first == 1 && ko == 1) // the third roud and I played first
        {
            if (t[1][1] == '-')
                cout << "1 1" << endl;
            else if (t[2][0] == 'X' && t[2][1] == '-' && t[2][2] == 'X')
                cout << "2 1" << endl;
            else if (t[2][0] == 'X' && t[1][0] == '-' && t[0][0] == 'X')
                cout << "1 0" << endl;
            else if (t[0][0] == 'X' && t[1][0] == '-' && t[2][2] == 'X')
                cout << "1 0" << endl;
            
            else if (t[0][0] == 'X' && t[1][0] == 'X' && t[2][0] == '-')
                cout << "2 0" << endl;
            else if (t[0][0] == '-' && t[1][0] == 'X' && t[2][0] == 'X')
                cout << "0 0" << endl;
            
            else if (t[0][2] == 'X' && t[1][2] == 'X' && t[2][2] == '-')
                cout << "2 2" << endl;
            else if (t[0][2] == 'X' && t[1][2] == '-' && t[2][2] == 'X')
                cout << "1 2" << endl;
            
            else if (t[0][2] == 'X' && t[0][1] == '-' && t[0][0] == 'X')
                cout << "0 1" << endl;
            else if (t[0][2] == 'X' && t[0][1] == 'X' && t[0][0] == '-')
                cout << "0 0" << endl;
            
            else if (t[0][2] == 'X' && t[1][2] == '-' && t[2][2] == 'X')
                cout << "1 2" << endl;
            else if (t[0][2] == 'X' && t[1][2] == 'X' && t[2][2] == '-')
                cout << "2 2" << endl;
            
        }
        else if (index == 3 && play_first == 1 && we_defend == 1) // the third roud and I played first and we defend
        {
            if (t[1][1] == '-')
                cout << "1 1" << endl;
            else if (t[2][0] == 'X' && t[2][1] == '-' && t[2][2] == 'X')
                cout << "2 1" << endl;
            else if (t[2][0] == 'X' && t[1][0] == '-' && t[0][0] == 'X')
                cout << "1 0" << endl;
            else if (t[0][0] == 'X' && t[1][0] == '-' && t[2][2] == 'X')
                cout << "1 0" << endl;
            
            else if (t[0][0] == 'X' && t[1][0] == 'X' && t[2][0] == '-')
                cout << "2 0" << endl;
            else if (t[0][0] == '-' && t[1][0] == 'X' && t[2][0] == 'X')
                cout << "0 0" << endl;
            
            else if (t[0][2] == 'X' && t[1][2] == 'X' && t[2][2] == '-')
                cout << "2 2" << endl;
            else if (t[0][2] == 'X' && t[1][2] == '-' && t[2][2] == 'X')
                cout << "1 2" << endl;
            
            else if (t[0][2] == 'X' && t[0][1] == '-' && t[0][0] == 'X')
                cout << "0 1" << endl;
            else if (t[0][2] == 'X' && t[0][1] == 'X' && t[0][0] == '-')
                cout << "0 0" << endl;
            
            else if (t[0][2] == 'X' && t[1][2] == '-' && t[2][2] == 'X')
                cout << "1 2" << endl;
            else if (t[0][2] == 'X' && t[1][2] == 'X' && t[2][2] == '-')
                cout << "2 2" << endl;
            
        }
        else if (index == 3 && play_first == 0) // the third roud and he played first
        {
            // if he didn't notice
            if (t[0][2] == 'X' && t[1][1] == 'X')
            {
                cout << "2 0" << endl;
            }
            else if (t[0][0] == 'X' && t[1][1] == 'X')
            {
                cout << "2 2" << endl;
            }
            else if (t[1][1] == 'X' && t[1][2] == 'X')
            {
                cout << "1 0" << endl;
            }
            else if (t[1][0] == 'X' && t[1][1] == 'X')
            {
                cout << "1 2" << endl;
            }
            
            else if (t[2][1] == 'X' && t[2][2] == 'X')
            {
                cout << "2 0" << endl;
            }
            else if (t[2][0] == 'X' && t[2][2] == 'X')
            {
                cout << "2 1" << endl;
            }
            else if (t[2][0] == 'X' && t[2][1] == 'X')
            {
                cout << "2 2" << endl;
            }

            else if (t[0][1] == 'X' && t[0][2] == 'X')
            {
                cout << "0 1" << endl;
            }
            else if (t[0][0] == 'X' && t[0][2] == 'X')
            {
                cout << "0 1" << endl;
            }
            else if (t[0][0] == 'X' && t[0][2] == 'X')
            {
                cout << "0 1" << endl;
            }
            else
            {
                // we defend
                if (t[0][2] == 'O' && t[1][2] == '0')
                {
                    cout << "2 2" << endl;
                    t[2][2] = 'X';
                }
                else if (t[0][2] == 'O' && t[2][2] == '0')
                {
                    cout << "1 2" << endl;
                    t[1][2] = 'X';
                }
                else if (t[1][2] == 'O' && t[2][2] == '0')
                {
                    cout << "0 2" << endl;
                    t[0][2] = 'X';
                }

                else if (t[0][0] == 'O' && t[0][1] == '0')
                {
                    cout << "0 2" << endl;
                    t[0][2] = 'X';
                }
                else if (t[0][0] == 'O' && t[0][2] == '0')
                {
                    cout << "0 1" << endl;
                    t[1][2] = 'X';
                }
                else if (t[0][1] == 'O' && t[0][2] == '0')
                {
                    cout << "0 0" << endl;
                    t[0][0] = 'X';
                }

                else if (t[2][0] == 'O' && t[2][1] == '0')
                {
                    cout << "2 2" << endl;
                    t[2][2] = 'X';
                }
                else if (t[2][0] == 'O' && t[2][2] == '0')
                {
                    cout << "2 1" << endl;
                    t[2][1] = 'X';
                }
                else if (t[2][1] == 'O' && t[2][2] == '0')
                {
                    cout << "2 0" << endl;
                    t[2][0] = 'X';
                }

                else if (t[0][0] == 'O' && t[1][0] == '0')
                {
                    cout << "2 0" << endl;
                    t[2][0] = 'X';
                }
                else if (t[0][0] == 'O' && t[2][0] == '0')
                {
                    cout << "1 0" << endl;
                    t[1][0] = 'X';
                }
                else if (t[1][0] == 'O' && t[2][0] == '0')
                {
                    cout << "0 0" << endl;
                    t[0][0] = 'X';
                }
                we_defend = 1;
            }
        }
        
        if (index == 4 /*&& play_first == 1 && we_defend == 1*/)
        {
            if (t[0][0] == '-') // as always if he didn't notice
            {
                cout << "0 0" << endl;
            }
            else if (t[0][1] == '-')
                cout << "0 1" << endl;
            else if (t[1][0] == '-')
                cout << "1 0" << endl;
            else if (t[1][2] == '-')
                cout << "1 2" << endl;
            else if (t[2][1] == '-')
                cout << "2 1" << endl;
            else if (t[2][2] == '-')
                cout << "2 2" << endl;
            else // we defend
            {
                if (his_last_play == "00")
                {
                    cout << "2 2" << endl;
                    t[2][2] = 'X';
                }
                else if (his_last_play == "01")
                {
                    cout << "2 1" << endl;
                    t[2][1] = 'X';
                }
                else if (his_last_play == "10")
                {
                    cout << "1 2" << endl;
                    t[1][2] = 'X';
                }
                else if (his_last_play == "12")
                {
                    cout << "1 0" << endl;
                    t[1][0] = 'X';
                }
                else if (his_last_play == "21")
                {
                    cout << "0 1" << endl;
                    t[0][1] = 'X';
                }
                else
                {
                    cout << "0 0" << endl;
                    t[0][0] = 'X';
                }
                we_defend = 1;
            }
        }
        index++;
    }
}