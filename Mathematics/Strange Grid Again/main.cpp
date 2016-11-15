//
//  main.cpp
//  Strange Grid Again
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
        long int a,b;
        cin >> a >> b;
        long int add = abs((a-1)/2) * 10;
        long int mod = (a-1) % 2;
        long int val = add + mod + (2*(b-1));
        cout << val << endl;
    }
};

int main(int argc, const char * argv[]) {
    Solution solution = Solution();
    solution.takeInput();
    return 0;
}
