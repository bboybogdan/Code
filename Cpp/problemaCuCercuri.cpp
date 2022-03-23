#include<iostream>
#include<math.h>
using namespace std;
int main()
{
  int n,r1,r2,i,suma= 0,r;
  cout<<"Da nr de cercuri: ";
  cin>>n;
  for(i=1;i<=n;i++)
  {
    cin>>r;
    suma = (2*r) + suma;
  }
  cout<<"Suma razelor este: "<<suma;
}
