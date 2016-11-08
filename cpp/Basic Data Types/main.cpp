//
//  main.cpp
//  Basic Data Types
//
//  Created by kaladhar reddy on 30/10/16.
//  Copyright © 2016 kaladhar reddy. All rights reserved.
//

#include <iostream>
using namespace std;

class Solution {
public:
    void takeInput() {
        int i;
        long l;
        long long ll;
        char c;
        float f;
        double d;
        
        scanf("%d %ld %lld %c %f %lf", &i, &l, &ll, &c, &f, &d);
        printf("%d\n%ld\n%lld\n%c\n%.3f\n%.9f", i, l, ll, c, f, d);
        
        
    }
};

int main(int argc, const char * argv[]) {
    Solution solution = Solution();
    solution.takeInput();
    return 0;
}
