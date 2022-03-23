#include<iostream>
#include<fstream>
#include<math.h>
#include<string.h>
using namespace std;
int main()
{
    int num1, num2;
    char ac;
    ofstream f("rez.out");
    cout<< "Enter the first number: ";
    cin>> num1;
    cout<<"Enter the second number: ";
    cin>> num2;
    cout<<"Choose action: Add(a), Sub(s), Mult(m), Div(d) -> ";
    cin>> ac;

    cout<<"The result is: "<< " ";
    if(ac == 'a')
        cout<<num1 + num2;
    else if(ac == 's')
        cout<< num1 - num2;
    else if(ac == 'm')
        cout<< num1 * num2;
    else
        cout<< num1 / num2;

    f.close();
}
