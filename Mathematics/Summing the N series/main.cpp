//
//  main.cpp
//  Summing the N series
//
//  Created by kaladhar reddy on 12/11/16.
//  Copyright © 2016 kaladhar reddy. All rights reserved.
//

#define ll long long int
#define ull unsigned long long int
#define mod 1000000007

#include <iostream>
using namespace std;

class Solution {
public:
    void takeInput() {
        int t;
        ull n;
        cin >> t;
        for (int i = 0; i < t; i++) {
            cin >> n;
            n %= mod;
            cout << ((n*n) % mod) << endl;
        }
        
    }
};

int main(int argc, const char * argv[]) {
    Solution solution = Solution();
    solution.takeInput();
    return 0;
}
