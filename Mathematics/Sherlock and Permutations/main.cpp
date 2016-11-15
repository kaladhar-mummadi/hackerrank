//
//  main.cpp
//  Sherlock and Permutations
//
//  Created by kaladhar reddy on 13/11/16.
//  Copyright © 2016 kaladhar reddy. All rights reserved.
//

#define ll long long int
#define mod 1000000007

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    
    vector<vector<ll>> createPascal(int max) {
        vector<vector<ll>> pascal;
        for (int i=0; i < max; i++) {
            vector<ll> oneRow(i+1);
            oneRow[0] = 1;
            
            for (int j = 1; j < i; j++) {
                
                oneRow[j] = (pascal[i-1][j-1] + pascal[i-1][j]) % mod;
                
            }
            oneRow[i] = 1;
            pascal.push_back(oneRow);
        }
        
        return pascal;
    }
    
    void takeInput() {
        vector<vector<ll>> pascal = createPascal(2001);
        int t;
        int n, m;
        cin >> t;
        for (int i = 0; i < t; i++) {
            cin >> n >> m;
            cout << pascal[n+m-1][n] << endl;
        }
        
    }
};

int main(int argc, const char * argv[]) {
    Solution solution = Solution();
    solution.takeInput();
    return 0;
}
