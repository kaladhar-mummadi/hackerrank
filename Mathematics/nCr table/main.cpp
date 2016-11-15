//
//  main.cpp
//  nCr table
//
//  Created by kaladhar reddy on 13/11/16.
//  Copyright © 2016 kaladhar reddy. All rights reserved.
//

#define ll long long int
#define mod 1000000000

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<long long int>> pascal;
    void createPascal(int max) {
        for (int i=0; i < max; i++) {
            vector<long long int> oneRow(i+1);
            oneRow[0] = 1;
            
            for (int j = 1; j < i; j++) {

                    oneRow[j] = (pascal[i-1][j-1] + pascal[i-1][j]) % mod;

            }
            oneRow[i] = 1;
            pascal.push_back(oneRow);
        }
    }
    void takeInput() {
        createPascal(1000);
        int t;
        int n;
        cin >> t;
        for (int i = 0; i < t; i++) {
            cin >> n;
            for(int j =0;  j < pascal[n].size(); j++) {
                cout << pascal[n][j] << " ";
            }
            cout << endl;
        }
        
    }
};

int main(int argc, const char * argv[]) {
    Solution solution = Solution();
    solution.takeInput();
    return 0;
}
