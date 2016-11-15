//
//  main.cpp
//  Possible Path
//
//  Created by kaladhar reddy on 11/11/16.
//  Copyright © 2016 kaladhar reddy. All rights reserved.
//

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
        int a,b,x,y;
        cin >> t;
        for (int i = 0; i < t; i++) {
            cin >> a >> b >> x >> y;
            if (gcd(a, b) == gcd(x,y)) {
                cout << "YES" << "\n";
            } else {
                cout << "NO" << "\n";
            }
        }
        
    }
};

int main(int argc, const char * argv[]) {
    Solution solution = Solution();
    solution.takeInput();
    return 0;
}
