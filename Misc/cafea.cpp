#include<iostream>
#include<fstream>
#include<windows.h>
#include<math.h>
using namespace std;
int main()
{
  int x,optiune;
  ifstream f("fis1.in");
  f>>x;
  if(x != 5)
    {
      x++;
      f.close();
      ofstream rez("fis1.in");
      rez<<x;
    }
  else
    {
      cout<<"Trebuie sa pui apa in espresor.";
      ofstream rez("fis1.in");
      x = 0;
      rez<<x;
      rez.close();
      return 0;
    }
  cout<<"Cine vrea sa-si faca cafea? \n1. Bobo. \n2. Mami. \n3. Tati. \nOptiune: ";
  cin>>optiune;
  if(optiune == 1)
    {
      cout<<"Cafeaua lui Bobo va fi gata in 3 minute.\n";
    Sleep(3000);
      cout<<"Cafeaua lui Bobo este gata.";
    }
  else if(optiune == 2)
    {
      cout<<"Cafeaua lui Mami va fi gata in 3 minute.\n";
    Sleep(3000);
      cout<<"Cafeaua lui Mami este gata.";
    }
  else if(optiune == 3)
    {
      cout<<"Cafeaua lui Tati va fi gata in 3 minute.\n";
    Sleep(3000);
      cout<<"Cafeaua lui Tati este gata.";
    }
}
