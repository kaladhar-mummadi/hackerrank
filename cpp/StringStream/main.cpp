//
//  main.cpp
//  StringStream
//
//  Created by kaladhar reddy on 11/11/16.
//  Copyright © 2016 kaladhar reddy. All rights reserved.
//

#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str) {
    vector<int> numbers;
    stringstream ss(str);
    int n;
    char ch = ',';
    while (!ss.eof()) {
        ss >> n >> ch;
        numbers.push_back(n);
    }
    
    return numbers;
}

int main() {
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }
    
    return 0;
}
