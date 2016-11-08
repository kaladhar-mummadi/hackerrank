//
//  main.cpp
//  Arrays Introduction
//
//  Created by kaladhar reddy on 30/10/16.
//  Copyright © 2016 kaladhar reddy. All rights reserved.
//

#include <iostream>
using namespace std;

class Solution {
public:
    void takeInput() {
        int n;
        int *arr;
        cin >> n;
        arr = new int[n];
        for (int i = 0; i < n; i++) {
            cin >> arr[i];
        }
        
        for (int i = n-1; i >= 0; i--) {
            cout << arr[i] << " ";
        }
        
    }
};

int main(int argc, const char * argv[]) {
    Solution solution = Solution();
    solution.takeInput();
    return 0;
}
