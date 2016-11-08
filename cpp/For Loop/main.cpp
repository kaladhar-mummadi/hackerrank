//
//  main.cpp
//  For Loop
//
//  Created by kaladhar reddy on 30/10/16.
//  Copyright © 2016 kaladhar reddy. All rights reserved.
//

#include <iostream>
using namespace std;

class Solution {
public:
    void takeInput() {
        int a,b;
        string represents[11] = {"even","one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "odd"};
        cin >> a >> b;
        for (; a<=b; a ++) {
            if (a < 10){
                cout << represents[a];
            } else if(a%2 == 0){
                cout << represents[0];
            } else{
                cout << represents[10];
            }
            cout << "\n";
        }
    }
};

int main(int argc, const char * argv[]) {
    Solution solution = Solution();
    solution.takeInput();
    return 0;
}
