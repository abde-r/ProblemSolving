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

int count(string s) {
  int count=0;

  for (int i=0; i<s.size(); i++)
    if (s[i]=='*')
      count++;
  return count;
}

vector<int> buildingHeights(int n, vector<string> building_map) {

  vector<int> r;
  for (int i=0; i<n; i++)
    r.push_back(count(building_map[i]));

  return r;
}