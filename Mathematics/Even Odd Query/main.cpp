//
//  main.cpp
//  Even Odd Query
//
//  Created by kaladhar reddy on 13/11/16.
//  Copyright © 2016 kaladhar reddy. All rights reserved.
//

#define ll long long int
#define mod 1000000007

#include <iostream>
#include <algorithm>
using namespace std;

class Solution {
public:
    void takeInput() {
        int n, q, left, right;
        int *numbers;
        cin >> n;
        numbers = new int[n];
        for (int i = 0; i < n; i++) {
            cin >> numbers[i];
        }
        cin >> q;
        while (q > 0) {
            cin >> left >> right;
            if (left > right) {
                cout << "Odd" << endl;
            } else if (numbers[left - 1] % 2 == 0) {
                if(numbers[left] == 0 and left != right) {
                    cout << "Odd" << endl;
                } else {
                    cout << "Even" << endl;
                }
            } else {
                cout << "Odd" << endl;
            }
            q--;
        }
    }
};

int main(int argc, const char * argv[]) {
    Solution solution = Solution();
    solution.takeInput();
    return 0;
}
