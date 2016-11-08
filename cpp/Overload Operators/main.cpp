//
//  main.cpp
//  Overload Operators
//
//  Created by kaladhar reddy on 30/10/16.
//  Copyright © 2016 kaladhar reddy. All rights reserved.
//
#include<iostream>
using namespace std;

class Complex
{
public:
    int a,b;
    void input(string s)
    {
        int v1=0;
        int i=0;
        while(s[i]!='+')
        {
            v1=v1*10+s[i]-'0';
            i++;
        }
        while(s[i]==' ' || s[i]=='+'||s[i]=='i')
        {
            i++;
        }
        int v2=0;
        while(i<s.length())
        {
            v2=v2*10+s[i]-'0';
            i++;
        }
        a=v1;
        b=v2;
    }
};
Complex operator+(Complex &x, Complex y) {
    Complex z = Complex();
    int a = x.a + y.a;
    int b = x.b + y.b;
    z.a = a;
    z.b = b;
    
    return z;
}

ostream & operator<<(ostream & stream, Complex z) {
    if (z.b < 0) {
        stream << z.a << "-i" << z.b;
    } else if(z.b >0) {
        stream << z.a << "+i" << z.b;
    } else {
        stream << z.a;
    }
    return stream;
}
int main()
{
    Complex x,y;
    string s1,s2;
    cin>>s1;
    cin>>s2;
    x.input(s1);
    y.input(s2);
    Complex z=x+y;
    cout<<z<<endl;
}
