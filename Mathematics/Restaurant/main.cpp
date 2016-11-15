//
//  main.cpp
//  Restaurant
//
//  Created by kaladhar reddy on 12/11/16.
//  Copyright © 2016 kaladhar reddy. All rights reserved.
//

#define ll long long int

#include <iostream>

using namespace std;

class Solution {
public:
    int gcd(int a, int b)
    {
        if (a == 0)
            return b;
        return gcd(b%a, a);
    }
    
    void takeInput() {
        int t;
        int a,b;
        cin >> t;
        for (int i = 0; i < t; i++) {
            cin >> a >> b;
            int divisor = gcd(a,b);
            int q1 = a / divisor;
            int q2 = b / divisor;
            cout << q1*q2 << endl;
        }
        
    }
};

int main(int argc, const char * argv[]) {
    Solution solution = Solution();
    solution.takeInput();
    return 0;
}
