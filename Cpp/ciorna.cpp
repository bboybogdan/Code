#include<iostream>
#include<math.h>
using namespace std;
int main()
{
    int n,x,y,z,t,k=0;
    n = 8;
    for(x=1;x<=n;x++)
        for(y=x+1;y<=9;y++)
            for(z=0;z<=y-1;z++)
                for(t=z+1;t<=9;t++)
                    {
                        k=x*1000 + y*100 + z*10 + t;
                        cout<<k<<" ";
                    }
}