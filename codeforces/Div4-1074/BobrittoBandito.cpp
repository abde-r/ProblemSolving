#include <iostream>
#include <sstream>
#include <string>
#include <vector>

int main() {
    int n;
    std::cin >> n;
    std::cin.ignore();
    std::vector<std::vector<int>> line;

    for (int i=0; i<n; i++) {
        std::string name;
        std::getline(std::cin, name);

        std::istringstream iss(name);
        int num;
        std::vector<int> temp;

        while (iss >> num)
            temp.push_back(num);
        line.push_back(temp);
    }


    for (const std::vector<int>& v : line) {
        int _left=0;
        int _right=-1;
        for (int i=0; i<v[1];) {
            if (_right<v[3]) {
                _right++;
                i++;
            }
            if (_left>v[2]) {
                _left--;
                i++;
            }
            
            if (_left == v[2] || _right == v[3]) {
                if (_right==v[3] && _left>v[2]) {
                    _left--;
                    i++;
                }
                else if (_left==v[2] && _right<v[3]) {
                    _right++;
                    i++;
                }
            }
            // std::cerr << "_left: " << _left << " | _right: " << _right << std::endl;
        }
        std::cout << _left << " " << _right << std::endl;
    }
    return 0;
}