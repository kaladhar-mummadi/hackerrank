//
//  main.cpp
//  Connecting Towns
//
//  Created by kaladhar reddy on 12/11/16.
//  Copyright © 2016 kaladhar reddy. All rights reserved.
//

#define ll long long int

#include <iostream>
using namespace std;

class Solution {
public:
    void takeInput() {
        int t;
        int n;
        int sum = 1;
        cin >> t;
        for (int i = 0; i < t; i++) {
            cin >> n;
            sum = 1;
            while ( n > 1) {
                int temp;
                cin >> temp;
                sum *= temp;
                sum %= 1234567;
                n--;
            }
            
            cout << sum << endl;
        }
        
    }
};

int main(int argc, const char * argv[]) {
    Solution solution = Solution();
    solution.takeInput();
    return 0;
}
