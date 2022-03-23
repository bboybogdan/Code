#include<iostream>
#include<fstream>
#include<math.h>
using namespace std;
int main()
{
  int anul,secolul;
  cout<<"Al carui an vrei sa afli secolul?";
  cin>>anul;
  if(anul <= 1000)
    {
      secolul = anul / 100 % 10 + 1;
    }
  else
    {
      secolul = anul / 100 + 1;
    }
  cout<<"Secolul este "<<secolul;
  
}
