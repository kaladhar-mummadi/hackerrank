//
//  main.cpp
//  Diwali Lights
//
//  Created by kaladhar reddy on 12/11/16.
//  Copyright © 2016 kaladhar reddy. All rights reserved.
//

#define ll long long int
#define ull unsigned long long int

#include <iostream>
using namespace std;

class Solution {
public:
    int powerOf(int n , int power, int mod) {
        int res = 1;
        while (power--) {
            res *= 2;
            res %= mod;
        }
        
        return res;
    }
    void takeInput() {
        int t;
        int n;
        cin >> t;
        for (int i = 0; i < t; i++) {
            cin >> n;
            cout << powerOf(2, n, 100000) - 1 << endl;
        }
        
    }
};

int main(int argc, const char * argv[]) {
    Solution solution = Solution();
    solution.takeInput();
    return 0;
}
