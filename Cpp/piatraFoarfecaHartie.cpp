#include<iostream>
#include<cstring>
#include<stdlib.h>
using namespace std;
int main()
{
  char alegere[2];
  int n;
  cout<<"Alege: Piatra(p), Forfeca(f), Hartie(h) -> ";
  cin>>alegere;
  n = rand() % 4;

  if(n == 1)
    if(alegere == "p")
      cout<<"Alegerea mea este piatra. Egalitate.";
    else if(alegere == "f")
      cout<<"Alegerea mea este piatra. M-ai batut.";
    else if(alegere == "h")
      cout<<"Alegerea mea a fost piatra. Te-am batut.";
  else if(n == 2)
    if(alegere == "p")
      cout<<"Alegerea mea a fost foarfeca. M-ai batut.";
    else if(alegere == "f")
      cout<<"Alegerea mea a fost foarfeca. Egalitate.";
    else if(alegere == "h")
      cout<<"Alegerea mea a fost foarfeca. Te-am batut.";
  else if(n == 3)
    if(alegere == "p")
      cout<<"Alegerea mea a fost hartie. Te-am batut.";
    else if(alegere == "f")
      cout<<"Alegerea mea a fost hartie. M-ai batut.";
    else if(alegere == "h")
      cout<<"Alegerea mea a fost hartie. Egalitate.";
}
