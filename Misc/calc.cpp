#include<iostream>
#include<fstream>
#include<math.h>
using namespace std;
int main()
{
    int num1, num2, ac;
    ofstream rez("rez.out");
    cout<< "Enter the first number: ";
    cin>> num1;
    cout<<"Enter the second number: ";
    cin>> num2;
    cout<<"Choose action: Add(1), Sub(2), Mult(3), Div(4) -> ";
    cin>> ac;

    rez<<"The result is: "<< " ";
    if(ac == 1)
        rez<<num1 + num2;
    else if(ac == 2)
        rez<< num1 - num2;
    else if(ac == 3)
        rez<< num1 * num2;
    else
        rez<< num1 / num2;

    rez.close();
}