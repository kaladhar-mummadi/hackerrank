//
//  mylib.h
//  Mathematics
//
//  Created by kaladhar reddy on 12/11/16.
//  Copyright © 2016 kaladhar reddy. All rights reserved.
//

#ifndef mylib_h
#define mylib_h


#endif /* mylib_h */

#include <vector>
#define mod 1000000000

int gcd(int a, int b)
{
    if (a == 0)
        return b;
    return gcd(b%a, a);
}

vector<vector<long long int>> createPascal(int max) {
    vector<vector<long long int>> pascal;
    for (int i=0; i < max; i++) {
        vector<long long int> oneRow(i+1);
        oneRow[0] = 1;
        
        for (int j = 1; j < i; j++) {
            
            oneRow[j] = (pascal[i-1][j-1] + pascal[i-1][j]) % mod;
            
        }
        oneRow[i] = 1;
        pascal.push_back(oneRow);
    }
    
    return pascal;
}
