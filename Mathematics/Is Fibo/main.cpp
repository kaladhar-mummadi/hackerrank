//
//  main.cpp
//  Is Fibo
//
//  Created by kaladhar reddy on 22/12/16.
//  Copyright © 2016 kaladhar reddy. All rights reserved.
//

#define ll long long int
#define ull unsigned long long int
#define mod 1000000007
#define max_limit 10000000000

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void takeInput() {
        int t;
        cin >> t;
        ull n;
        ull fibs[100];
        fibs[0] = 0;
        fibs[1] = 1;
        
        int j = 2;
        while (fibs[j-1] <= max_limit) {
            fibs[j] = fibs[j-1] + fibs[j-2];
            j++;
        }
        for (int i = 0; i < t; i++) {
            cin >> n;
            int j = 0;
            while (j< 100) {
                if (fibs[j] == n) {
                    cout << "IsFibo" << "\n";
                    break;
                }
                j++;
            }
            
            if (fibs[j] != n) {
                cout << "IsNotFibo"<< "\n";
            }
        }
        
    }
};

int main(int argc, const char * argv[]) {
    Solution solution = Solution();
    solution.takeInput();
    return 0;
}
