
//
//  main.cpp
//  Find the Point
//
//  Created by kaladhar reddy on 30/10/16.
//  Copyright © 2016 kaladhar reddy. All rights reserved.
//
#define getSign(x) ((x>0) - (x<0))

#include <iostream>
using namespace std;

class Solution {
public:
    void takeInput() {
        int t;
        int p[2], q[2];
        
        cin >> t;
        for (int i = 0; i < t; i++) {
            cin >> p[0] >> p[1] >> q[0] >> q[1];
            
            int xCoordinate = 2 * q[0] - p[0];
            int yCoordinate = 2 * q[1] - p[1];
            
            cout << xCoordinate << " " << yCoordinate << "\n";
        }
    }
};

int main(int argc, const char * argv[]) {
    Solution solution = Solution();
    solution.takeInput();
    return 0;
}
