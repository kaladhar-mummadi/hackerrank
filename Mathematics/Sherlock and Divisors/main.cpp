//
//  main.cpp
//  Sherlock and Divisors
//
//  Created by kaladhar reddy on 12/11/16.
//  Copyright © 2016 kaladhar reddy. All rights reserved.
//
#define ll long long int

#include <iostream>
#include <map>
#include <cmath>
using namespace std;

class Solution {
public:
    void primeFactors(long int n) {
        map<int, int> factors;
        int i = 2;
        factors[2] = 0;
        while (n%i == 0) {

                factors[i]++;
            n /= 2;
        }
        
        i++;
        while (i <= sqrt(n)) {
            factors[i] = 0;
            while (n%i == 0) {
                factors[i] ++;
                n /= i;
            }
            i += 2;
        }
        
        if (n > 2) {
            factors[i] = 1;
        }
        int numberOfEvenFactors = factors[2] + 1;
        factors.erase(2);
        int totalNumberOfFactors = 1;
        for (const auto &it : factors) {
            totalNumberOfFactors *= (it.second + 1);
        }
        
        cout << totalNumberOfFactors*numberOfEvenFactors - totalNumberOfFactors << endl;
    }
    void takeInput() {
        int t;
        long int n;
        cin >> t;
        for (int i = 0; i < t; i++) {
            cin >> n;
            primeFactors(n);
//            if (n%2 != 0) {
//                cout << 0 << endl;
//            } else {
//                int numberOfDivisors = 0;
//                int j = 2;
//                while (j <= n/2) {
//                    
//                    if (n%j == 0) {
//                        numberOfDivisors++;
//                    }
//                    j += 2;
//                    
//                }
//                
//                cout << numberOfDivisors + 1 << endl;
//            }
        }
        
    }
};

int main(int argc, const char * argv[]) {
    Solution solution = Solution();
    solution.takeInput();
    return 0;
}
