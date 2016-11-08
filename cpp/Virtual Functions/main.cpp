//
//  main.cpp
//  Virtual Functions
//
//  Created by kaladhar reddy on 06/11/16.
//  Copyright © 2016 kaladhar reddy. All rights reserved.
//

#include <iostream>
using namespace::std;

class Person {
    char name[101];
    int age;
    public :
    virtual void getdata(){
        cin >> name >> age;
    };
    virtual void putdata() {
        cout << name << " " << age << " ";
    };
};

class Professor : public Person {
    int publications;
    int cur_id;
    static int global_id;
    
    void getdata() {
        global_id++;
        cur_id = global_id;
        Person::getdata();
        cin >> publications;
    };
    void putdata() {
        Person::putdata();
        cout << publications << " " << cur_id << "\n";
    };
};

class Student : public Person {
    int marks[6];
    int cur_id;
    static int global_id;
    int sum = 0;
    
    void getdata() {
        global_id++;
        cur_id = global_id;
        Person::getdata();
        for (int i =0; i < 6; i++) {
            cin >> marks[i];
            sum += marks[i];
        }
    }
    
    void putdata() {
        Person::putdata();
        cout << sum << " " << cur_id << "\n";
    }
    
};

int Professor::global_id = 0;
int Student::global_id = 0;

int main(int argc, const char * argv[]) {
    int n, val;
    cin >> n; //The number of objects that is going to be created.
    Person *per[n];
    
    for(int i = 0;i < n;i++){
        
        cin>>val;
        if(val == 1){
            // If val is 1 current object is of type Professor
            per[i] = new Professor;
            
        }
        else per[i] = new Student; // Else the current object is of type Student
        
        per[i]->getdata(); // Get the data from the user.
        
    }
    
    for(int i=0;i<n;i++)
        per[i]->putdata(); // Print the required output for each object.
    
    return 0;
}
