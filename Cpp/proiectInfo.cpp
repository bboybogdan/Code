#include<iostream>
#include<fstream>
#include<math.h>
using namespace std;
int main()
{
  int u, optiune,num1,num2, i, V[100],n,nr=0,m,A[100][100],j,s=0,d;
  cout<<"Alege una dintre urmatoarele optiuni: \n"<<"1. Algoritmi elementari. \n"<<"2. Vector. \n"<<"3. Matrici. \n"<<"4. Fisiere \n"<<"Optiune: ";
  cin>> optiune;
  if(optiune == 1)
    {
      cout<<"Un algoritm elementar este aflarea maximului dintre 2 numere: \n"<<"Introdu primul numar: ";
      cin>> num1;
      cout<<"Introdu al doilea nr: ";
      cin>> num2;
      if(num1 > num2)
        u = num1;
      else
        u = num2;
      cout<<"Numarul mai mare este: "<< u;
    }
  else if(optiune == 2)
    {
      cout<<"Un vector se construieste astfel: \n";
      cout<<"for(i=1;i<=n;i++) \n cin>>V[i]\n";
      cout<<"Exemplu de problema cu vectori unde sa se afle care este cel mai mare numar din vector: \n";
      cout<<"Introdu cate numere sa se afle in vector: ";
      cin>> n;
      for(i=1;i<=n;i++)
        {
          cout<<"Introdu numerele care sa se afle in vector: ";
          cin>> V[i];
          if(V[i] > nr)
            u = V[i];
          else
            u = nr;
        }
      cout<<"Numarul mai mare este "<<u;
    }
  else if(optiune == 3)
    {
      cout<<"O matrice se construieste astfel: \n"<<"for(i=1;i<=n;i++) \n  for(j=1;j<=m;j++) \n  cin>>A[i][j]";
      cout<<"Exemplu de problema cu matrici: \n";
      cout<<"Introdu numarul de coloane: ";
      cin>>n;
      cout<<"Introdu numarul de linii: ";
      cin>>m;
      for(i=1;i<=n;i++)
        for(j=1;j<=m;j++)
          {
          cout<<"Introdu numerele care sa se afle inauntrul matricei: ";
          cin>>A[i][j];
          }

      cout<<"Matricea arata astfel: ";
      for(i=1;i<=n;i++)
        {
          cout<<endl;
          for(j=1;j<=m;j++)
            cout<<A[i][j]<<" ";
        }
    }
  else if(optiune == 4)
    {
      cout<<"Citirea dintr-un fisier arata astfel: ifstream NUMELE_CU_CARE_SA_FIE_FOLOSIT_IN_PROGRAM ('NUMELE_FISIERULUI'); \n";
      cout<<"Scrierea intr-un fisier arata astfel: ofstream NUMELE_CU_CARE_SA_FIE_FOLOSIT_IN_PROGRAM ('NUMELE_FISIERULUI');\n ";
      cout<<"Exemplu de citire si scriere dintr-un fisier: \n";
      cout<<"Scrierea rezultatului se afla in folderul rez.out \n";
      ofstream rez("rez.out");
      cout<<"Introdu numarul care sa fie testat daca este numar perfect: ";
      cin>>n;
      for(d=1;d<=n/2;d++)
        if(n%d==0)
          s=s+d;
      if(n==s)
        rez<<"Numarul "<<n<<" este numar perfect";
      else
        rez<<"Numarul "<<n<<" nu este numar perfect";
    }
}
