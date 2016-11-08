//
//  main.cpp
//  Variable Sized Arrays
//
//  Created by kaladhar reddy on 30/10/16.
//  Copyright © 2016 kaladhar reddy. All rights reserved.
//

#include <iostream>
using namespace std;

class Solution {
public:
    void takeInput() {
        int n, q, vary_size, **arr, **q_arr;
        cin >> n >> q;
        arr = new int*[n];
        q_arr = new int*[q];
        for (int i=0;i < n; i++) {
            cin >> vary_size;
            int *vary_size_arr;
            vary_size_arr = new int[vary_size];
            for(int j = 0; j < vary_size;j ++) {
                cin >> vary_size_arr[j];
            }
            arr[i] = vary_size_arr;
        }
        
        q_arr = new int*[q];
        for (int i=0;i < q; i++) {
            int *b;
            b = new int[2];
            cin >> b[0] >> b[1];
            q_arr[i] = b;
        }
        
        for (int i=0;i < q; i++) {
            cout << arr[q_arr[i][0]][q_arr[i][1]] << "\n";
        }
        
    }
};

int main(int argc, const char * argv[]) {
    Solution solution = Solution();
    solution.takeInput();
    return 0;
}
