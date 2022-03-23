#include<iostream>
#include<fstream>
#include<math.h>
using namespace std;
int main()
{ 
  int n,u,ogl=0,nr=0,p=1;
  cin>>n;
  while(n!=0)
    {
      u=n%10;
      if(u%2==0)
        {
          nr = nr+u*p;
          p= p*10;
        }
      n=n/10;
    }
  cout<<nr;
}
