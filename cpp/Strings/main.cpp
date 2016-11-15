//
//  main.cpp
//  Strings
//
//  Created by kaladhar reddy on 09/11/16.
//  Copyright © 2016 kaladhar reddy. All rights reserved.
//

#include <iostream>
using namespace std;

class Solution {
public:
    void takeInput() {
        string a,b;
        cin >> a;
        cin >> b;
        output(a, b);
    }
    
    void output(string a, string b) {
        string concatenatedString = a + b;
        char a1 = a[0];
        char b1 = b[0];
        cout << a.size() << " " << b.size() << "\n";
        cout << concatenatedString << "\n";
        a[0] = b1;
        b[0] = a1;
        cout << a << " " << b;
        
    }
};

int main(int argc, const char * argv[]) {
    Solution solution = Solution();
    solution.takeInput();
    return 0;
}
