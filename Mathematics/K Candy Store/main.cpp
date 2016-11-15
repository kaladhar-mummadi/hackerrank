//
//  main.cpp
//  K Candy Store
//
//  Created by kaladhar reddy on 16/11/16.
//  Copyright © 2016 kaladhar reddy. All rights reserved.
//

#include <iostream>

#define ll long long int
#define mod 1000000000

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<long long int>> createPascal(int max) {
        vector<vector<long long int>> pascal;
        for (int i=0; i < max; i++) {
            vector<long long int> oneRow(i+1);
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
        vector<vector<ll>> pascal = createPascal(2000);
        int t;
        int n,k;
        cin >> t;
        for (int i = 0; i < t; i++) {
            cin >> n >> k;
            cout << pascal[n+k-1][n-1]<< endl;
        }
        
    }
};

int main(int argc, const char * argv[]) {
    Solution solution = Solution();
    solution.takeInput();
    return 0;
}
