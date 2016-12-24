//
//  main.cpp
//  Halloween party
//
//  Created by kaladhar reddy on 22/12/16.
//  Copyright © 2016 kaladhar reddy. All rights reserved.
//

#define ll long long int
#define mod 1000000007

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    ll boxes(ll k) {
        ll horizontal_lines = (k / 2) + (k % 2);
        return horizontal_lines * (k/2);
    }
    void takeInput() {
        int t;
        ll k;
        cin >> t;
        for (int i = 0; i < t; i++) {
            cin >> k;
            cout << boxes(k)<< "\n";
        }
        
    }
};

int main(int argc, const char * argv[]) {
    Solution solution = Solution();
    solution.takeInput();
    return 0;
}
