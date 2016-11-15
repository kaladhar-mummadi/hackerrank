//
//  main.cpp
//  Leonardo's Prime Factors
//
//  Created by kaladhar reddy on 11/11/16.
//  Copyright © 2016 kaladhar reddy. All rights reserved.
//

#include <iostream>
using namespace std;

class Solution {
public:
    int primes[26] =  {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101};
    void takeInput() {
        int t;
        unsigned long long int n;
        cin >> t;
        for (int i = 0; i < t; i++) {
            cin >> n;
            unsigned long long int val = 1, factors = 0;
            while ( val <= n) {
                val *=primes[factors];
                factors ++;
            }
            cout << factors-1 << "\n";
        }
        
    }
};

int main(int argc, const char * argv[]) {
    Solution solution = Solution();
    solution.takeInput();
    return 0;
}
