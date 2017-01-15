//
//  main.cpp
//  Matrix Tracing
//
//  Created by kaladhar reddy on 11/01/17.
//  Copyright © 2017 kaladhar reddy. All rights reserved.
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
        int t;
        cin >> t;
        ll n, m;
        for (int i = 0; i < t; i++) {
            cin >> n >> m;
            ll border_nodes = (2 * (n+m) ) - 4;
            ll remaining_sum = fastExponent(4, (n*m) - (border_nodes));
            cout << remaining_sum + 2 << "\n";
        }
        
    }
    
    ll fastExponent(ll base, ll power) {
        ll ret = 1;
        ll temp = base;
        while (power) {
            if (power&1) {
                ret = (ret * temp) % mod;
            }
            
            temp = (temp * temp) % mod;
            power >>= 1;
        }
        
        return ret;
    }
    ll getPowerOf2(ll power) {
        ll prod = 1;
        while (power > 0) {
            prod *= 2;
            prod %= mod;
            power--;
        }
        
        return prod;
    }
};

int main(int argc, const char * argv[]) {
    Solution solution = Solution();
    solution.takeInput();
    return 0;
}
