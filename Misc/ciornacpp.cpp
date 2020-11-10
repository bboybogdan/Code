#include<iostream>
#include<math.h>
using namespace std;
int main()
{
    int n,m,i,j,d,u,s;
    cout<<"Da primul nr";
    cin>>n;
    cout<<"Da al doilea nr";
    cin>>m;
    for(i=1;i<=n;i++)
        {
            if(n%i==0)
                s=i;
            for(j=1;j<=m;j++)
                if(m%j==0)
                    u=j;
            if(u==s)
                d=u+s;
        }
    cout<<d;
}