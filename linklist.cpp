#include<iostream>
using namespace std;

struct student{
    int roll_no;
    string name;
    float marks;
    struct student
     *next;
};

int main(){
    struct student s;
    cout<<"Enter Roll no :"<<endl;
    cin>>s.roll_no;
    cout<<"Enter name of the student :"<<endl;
    cin>>s.name;
    cout<<"Enter the marks of the student :"<<endl;
    cin>>s.marks;
    cout<<"Roll no: "<<s.roll_no<<endl;
    cout<<"Name :"<<s.name<<endl;
    cout<<"Marks :"<<s.marks<<endl;
    return 0;
}