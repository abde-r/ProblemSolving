#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;

    for (int i=0; i<n; i++) {
        int score=0;
        vector<string> t;

        for (int x=0; x<10; x++) {
            string s;
            cin >> s;

            t.push_back(s);
        }

        for (int x=0; x<10; x++) {
            for (int y=0; y<10; y++) {
                if (t[x][y] == 'X') {
                    if (x==0 || x==9 || y==0 || y==9)
                        score+=1;
                    else if ((x==1 || x==8) && (y>=1 && y<=8))
                        score+=2;
                    else if ((x==2 || x==7) && (y>=2 && y<=7))
                        score+=3;
                    else if ((x==3 || x==6) && (y>=3 && y<=6))
                        score+=4;
                    else if ((x==4 || x==5) && (y>=4 && y<=5))
                        score+=5;
                    
                    else if ((y==3 || y==6) && (x>=3 && x<=6))
                        score+=4;
                    else if ((y==2 || y==7) && (x>=2 && x<=7))
                        score+=3;
                    else if ((y==1 || y==8) && (x>=1 && x<=8))
                        score+=2;
                }
            }
        }
        cout << score << endl;
    }

    return 0;
}