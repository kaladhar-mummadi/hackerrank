//
//  main.cpp
//  Handshake
//
//  Created by kaladhar reddy on 11/11/16.
//  Copyright © 2016 kaladhar reddy. All rights reserved.
//

#include <iostream>
using namespace std;

class Solution {
public:
    void takeInput() {
        int t;
        int n;
        cin >> t;
        for (int i = 0; i < t; i++) {
            cin >> n;
            calculateTotalHandshakes(n);
        }
    }
    
    void calculateTotalHandshakes(int n) {
        // (n * n-1) / 2
        cout << abs((n * (n-1)) / 2) << "\n";
    }
};

int main(int argc, const char * argv[]) {
    Solution solution = Solution();
    solution.takeInput();
    return 0;
}
