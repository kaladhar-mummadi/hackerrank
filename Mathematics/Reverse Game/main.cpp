//
//  main.cpp
//  Reverse Game
//
//  Created by kaladhar reddy on 12/11/16.
//  Copyright © 2016 kaladhar reddy. All rights reserved.
//

#define ll long long int

#include <iostream>
using namespace std;

class Solution {
public:
    void takeInput() {
        int t;
        int n, k;
        cin >> t;
        for (int i = 0; i < t; i++) {
            cin >> n >> k;
            
            if (k < (n/2)) {
                cout << 2*k +1;
            } else if (n%2 == 0) {
                if (k != abs(n/2)) {
                    
                }
            }
            
        }
        
    }
};

int main(int argc, const char * argv[]) {
    Solution solution = Solution();
    solution.takeInput();
    return 0;
}
