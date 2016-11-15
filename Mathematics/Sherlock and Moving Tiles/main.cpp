//
//  main.cpp
//  Sherlock and Moving Tiles
//
//  Created by kaladhar reddy on 11/11/16.
//  Copyright © 2016 kaladhar reddy. All rights reserved.
//

#define ll long long int
#define li long int

#include <iostream>
#include <cmath>
#include <limits>


using namespace std;

typedef numeric_limits< double > dbl;

class Solution {
public:
    void takeInput() {
        li l, s1, s2;
        int Q;
        cin >> l >> s1 >> s2;
        cin >> Q;
        ll query;
        double val;
        for (int i = 0; i < Q; i++) {
            cin >> query;
            val = (l*sqrt(2) - sqrt(2*query) ) / (abs(s1-s2));
            cout.precision(dbl::max_digits10);
            cout << val << "\n";
            
        }
        
    }
};

int main(int argc, const char * argv[]) {
    Solution solution = Solution();
    solution.takeInput();
    return 0;
}
