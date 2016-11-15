//
//  main.cpp
//  Maximum Draws
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
        while (t--) {
            cin >> n;
            cout << n + 1 << "\n";
        }
        
    }
};

int main(int argc, const char * argv[]) {
    Solution solution = Solution();
    solution.takeInput();
    return 0;
}
