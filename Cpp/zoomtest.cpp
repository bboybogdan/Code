#include<iostream>
#include<math.h>
#include<vector>
#include<string.h>
#include<fstream>
using namespace std;
void numimp(int n, int v[101], int &c){
  int i;
  for(i=1;i<=n;i++)
    cin>>v[i];
  for(i=1;i<=n;i++)
    {
      if((v[i]%10)%2 == 0 || (v[i]%100)%2 == 0 )
        {
          c++;
        }
    }
}
int main()
{
  int n,v[101],c;
  cin>>n;
  numimp(n,v,c);
  cout<<c;
}