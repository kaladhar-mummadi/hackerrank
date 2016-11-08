//
//  main.cpp
//  Functions
//
//  Created by kaladhar reddy on 30/10/16.
//  Copyright © 2016 kaladhar reddy. All rights reserved.
//
#include <iostream>
#include <cstdio>
using namespace std;

class Solution {
public:
    void takeInput() {
        int a, b, c, d;
        scanf("%d %d %d %d", &a, &b, &c, &d);
        int ans = max_of_four(a, b, c, d);
        printf("%d", ans);
    }
    
    int max_of_four(int a, int b, int c, int d) {
        int max = 0;
        int arr[4] = {a,b,c,d};
        for (int i=0; i < 4; i++) {
            if (max < arr[i]) {
                max = arr[i];
            }
        }
        return max;
    }
};

int main(int argc, const char * argv[]) {
    Solution solution = Solution();
    solution.takeInput();
    return 0;
}
