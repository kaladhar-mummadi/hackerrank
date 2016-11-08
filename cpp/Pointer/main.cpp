//
//  main.cpp
//  Pointer
//
//  Created by kaladhar reddy on 30/10/16.
//  Copyright © 2016 kaladhar reddy. All rights reserved.
//

#include <iostream>
using namespace std;

class Solution {
public:
    void takeInput() {
        int a, b;
        int *pa = &a, *pb = &b;
        
        scanf("%d %d", &a, &b);
        update(pa, pb);
        printf("%d\n%d", a, b);
    }
    
    void update(int *a, int *b) {
        int temp = *a + *b;
        *b = abs(*b - *a);
        *a = temp;
    }
};

int main(int argc, const char * argv[]) {
    Solution solution = Solution();
    solution.takeInput();
    return 0;
}
