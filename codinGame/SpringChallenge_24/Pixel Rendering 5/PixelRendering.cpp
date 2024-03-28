#include <iostream>
#include <cstring>
#include <unordered_map>
#include <vector>
#include <set>
#include <locale>
using namespace std;



/**
 * @param n The size of the image
 * @param target_image The rows of the desired image, from top to bottom
 */

bool check_cols(vector<string> v, vector<string> t, int j) {
    for (int i=0; i<v.size(); i++)
      if (v[i][j] != t[i][j] && v[i][j] == '#')
        return true;
    return false;
}

bool check_rows(vector<string> v, vector<string> t, int i) {
    for (int j=0; j<v.size(); j++)
      if (v[i][j] != t[i][j] && v[i][j] == '.')
        return true;
    return false;
}

void update_image_cols(vector<string> &v, int j) {
  for (unsigned long i=0; i<v.size(); i++){
      v[i][j] = '#';
    }
}

void update_image_rows(vector<string> &v, int i) {
  for (unsigned long j=0; j<v.size(); j++){
      v[i][j] = '.';
    }
}

vector<string> init_image(int n) {
  vector<string> v;

  for (int i=0; i<n; i++) {
    string temp="";

    for (int j=0; j<n; j++)
      temp+='.';
    v.push_back(temp);
  }
  return v;
}

vector<string> solve(int n, vector<string> target_image) {
  // Write your code here

  vector<string> commands;
  vector<string> image = init_image(n);

  while ((image != target_image)) {
    
    for (int i=0; i<n; i++) {
        if (check_cols(target_image, image, i)) {
          commands.push_back("C "+to_string(i));
          update_image_cols(image, i);
      }
    }

    for (int i=0; i<n; i++) {
        if (check_rows(target_image, image, i)) {
          commands.push_back("R "+to_string(i));
          update_image_rows(image, i);
      }
    }
  }

  return commands;
}
