//
//  main.cpp
//  Die Hard 3
//
//  Created by kaladhar reddy on 22/12/16.
//  Copyright © 2016 kaladhar reddy. All rights reserved.
//

#define ll long long int
#define mod 1000000007

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    string isPossible(int a, int b, int c) {
        if (c > a && c > b) {
            return "NO";
        }
        int gc1 = gcd(a,b);
        if (c % gc1 == 0) {
            return "YES";
        }
        
        return "NO";
    }
    
    int gcd(int a, int b)
    {
        if (a == 0)
            return b;
        return gcd(b%a, a);
    }
    int solve(int X){
        vector<int> number ;
        while(X){
            number.push_back(X % 10) ;
            X /= 10 ;
        }
        reverse(number.begin(),number.end()) ;
        int Z = -1 ;
        
        if(next_permutation(number.begin(),number.end())){
            // if next_permutation exists, update value of Z .
            Z = 0 ;
            for(int i=0;i<number.size();i++){
                Z = Z * 10 + number[i] ;
            }
        }
        return Z ; 
    }
    
    void takeInput() {
        cout << solve(784);
        
    }
};

int main(int argc, const char * argv[]) {
    Solution solution = Solution();
    solution.takeInput();
    return 0;
}
