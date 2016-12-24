//
//  main.cpp
//  Die Hard 3
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
    string isPossible(int a, int b, int c) {
        if (c > a && c > b) {
            return "NO";
        }
        int gc1 = gcd(a,b);
        if (c % gc1 == 0) {
            return "YES";
        }
        
        return "NO";
    }
    
    int gcd(int a, int b)
    {
        if (a == 0)
            return b;
        return gcd(b%a, a);
    }
    void takeInput() {
        int t;
        int a, b, c;
        cin >> t;
        for (int i = 0; i < t; i++) {
            cin >> a >> b >> c;
            cout << isPossible(a, b, c) << "\n";
        }
        
    }
};

int main(int argc, const char * argv[]) {
    Solution solution = Solution();
    solution.takeInput();
    return 0;
}
