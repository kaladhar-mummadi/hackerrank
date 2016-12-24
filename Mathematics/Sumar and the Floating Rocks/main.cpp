//
//  main.cpp
//  Sumar and the Floating Rocks
//
//  Created by kaladhar reddy on 24/12/16.
//  Copyright © 2016 kaladhar reddy. All rights reserved.
//

#define ll long long int
#define ull unsigned long long int
#define mod 1000000007

#include <iostream>
#include <vector>
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
        ll x1, y1, x2, y2;
        cin >> t;
        for (int i = 0; i < t; i++) {
            cin >> x1 >> y1 >> x2 >> y2;
            cout << (gcd(abs(x1-x2), abs(y1-y2)) - 1) << "\n";
        }
    }
};

int main(int argc, const char * argv[]) {
    Solution solution = Solution();
    solution.takeInput();
    return 0;
}
