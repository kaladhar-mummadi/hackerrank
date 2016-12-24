//
//  main.cpp
//  Filling Jars
//
//  Created by kaladhar reddy on 22/12/16.
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
    void takeInput() {
        ll n, m, k;
        ull sum = 0;
        int a, b;
        
        cin >> n >> m;
        for (int j = 0; j< m; j++) {
            cin >> a >> b >> k;
            sum = sum + ((b-a+1) * k);
        }
        
        cout << sum/ n;
        
        
    }
};

int main(int argc, const char * argv[]) {
    Solution solution = Solution();
    solution.takeInput();
    return 0;
}
