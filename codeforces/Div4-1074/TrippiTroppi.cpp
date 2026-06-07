#include <iostream>
#include <sstream>
#include <string>
#include <vector>

int main() {
    int n;
    std::cin >> n;
    std::cin.ignore();
    std::vector<std::string> output;

    for (int i=0; i<n; i++) {
        std::string name;
        std::getline(std::cin, name);

        std::istringstream iss(name);
        std::string words;
        std::string temp;

        while (iss >> words)
            temp += words[0];
        output.push_back(temp);
    }

    for (const std::string& i : output)
        std::cout << i << std::endl;
    return 0;
}