#include<fstream>
#include<iostream>
using namespace std;
int main()
{
    int s=0,nr,d,u; 
    ifstream fcit("fis1.in"); 
    ofstream rez("fis2.out"); 
    while(fcit>>nr)
        {s=s+nr;
        if(nr>u)
            u=nr;
            
        else
            nr=u;
        }
    rez<<u;

    fcit.close();
    rez.close(); 
} 