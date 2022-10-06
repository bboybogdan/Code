#include<iostream>
#include<math.h>
using namespace std;
int main()
{
    int n,i;
    for(i=100;i<=999;i++)
        {
            if(i%10 == (i%100/10) + (i%1000%100/10))
                cout<<i<<endl;
        }
}