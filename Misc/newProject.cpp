#include<iostream>
#include<fstream>
#include<math.h>
using namespace std;
int main()
{
  char litera;
  int optiune, raspunsCalculator,inFisierSauInFolder, num1, num2, literaMica, literaMare, numarulDeTermeni, i, t1 = 0, t2 = 1 ,uTermen, min, max,flag;
  ofstream rezultat("rez.out");
  cout<<"Alege una dintre urmatoarele optiuni: \n"<<"1. Calculator. \n"<<"2. Consoana sau vocala. \n"<<"3. Numarul lui Fibonacci. \n"<<"4. Numerele prime(dintr-un interval). \n"<<"5. Cum sa compilezi singur codul c++ in cmd. \n"<< "Optiune: ";
  cin>> optiune;

  if(optiune == 1)
    {
      cout<<"Apsa tasta 1 daca vrei ca rezultatul sa fie scris in CMD sau tasta 2 daca vrei sa fie scris intr-un fisier anume(rez.out): ";
      cin>> inFisierSauInFolder;
      cout<<"Introdu primul numar: ";
      cin>> num1;
      cout<<"Introdu al doilea numar: ";
      cin>> num2;
      cout<<"Alege o actiune: Adunare(1), Scadere(2), Inmultire(3), Impartitre(4) -> ";
      cin>>raspunsCalculator;
      if(inFisierSauInFolder == 1)
        {
          cout<<"Rezultatul este: "<<" ";
          if(raspunsCalculator == 1)
            cout<< num1 + num2;
          else if(raspunsCalculator == 2)
            cout<< num1 - num2;
          else if(raspunsCalculator == 3)
            cout<< num1 * num2;
          else
            cout<< num1 / num2;
        }
      else
        {
          rezultat<<"Rezultatul este: "<<" ";
          if(raspunsCalculator == 1)
            rezultat<< num1 + num2;
          else if(raspunsCalculator == 2)
            rezultat<< num1 - num2;
          else if(raspunsCalculator == 3)
            rezultat<< num1 * num2;
          else
            rezultat<< num1 / num2;
        }

    }
  else if(optiune == 2)
    {
      cout<<"Apsa tasta 1 daca vrei ca rezultatul sa fie scris in CMD sau tasta 2 daca vrei sa fie scris intr-un fisier anume(rez.out): ";
      cin>> inFisierSauInFolder;
      cout<< "Alege o litera din alfabet(International USA): ";
      cin>> litera;

      literaMica = (litera == 'a' || litera == 'e' || litera == 'i' || litera == 'o' || litera == 'u');
    	literaMare = (litera == 'A' || litera == 'E' || litera == 'I' || litera == 'O' || litera == 'U');

      if(inFisierSauInFolder == 1)
        {
          if(literaMica || literaMare)
            cout<< litera << " e o vocala";
          else
            cout<< litera << " e o consoana";
        }
      else
        {
          if(literaMica || literaMare)
            rezultat<< litera << " e o vocala";
          else
            rezultat<< litera << " e o consoana";
        }
    }
  else if(optiune == 3)
    {
        cout<<"Apsa tasta 1 daca vrei ca rezultatul sa fie scris in CMD sau tasta 2 daca vrei sa fie scris intr-un fisier anume(rez.out): ";
        cin>> inFisierSauInFolder;
        cout<<"Introdu numarul de termeni pana la cat sa fie numarul lui Fibonacci: ";
        cin>> numarulDeTermeni;
        if(inFisierSauInFolder == 1)
        {
          for(int i = 1; i<=numarulDeTermeni; i++)
          {
            if(i==1)
              {
                cout<< " "<< t1;
                continue;
              }
            if(i == 2)
              {
                cout<< t2<<" ";
                continue;
              }

            uTermen = t1 + t2;
            t1 = t2;
            t2 = uTermen;
            cout<< uTermen<< " ";
          }
        }
        else
        {
          for(int i = 1; i<=numarulDeTermeni; i++)
          {
            if(i==1)
              {
                rezultat<< " "<< t1;
                continue;
              }
            if(i == 2)
              {
                rezultat<< t2<<" ";
                continue;
              }

            uTermen = t1 + t2;
            t1 = t2;
            t2 = uTermen;
          rezultat<< uTermen<< " ";
        }
      }
    }
  else if(optiune == 4)
    {
      cout<<"Apsa tasta 1 daca vrei ca rezultatul sa fie scris in CMD sau tasta 2 daca vrei sa fie scris intr-un fisier anume(rez.out): ";
      cin>> inFisierSauInFolder;
      cout<< "Introdu doua numere ca interval: ";
      cin>> min>>max;
      if(inFisierSauInFolder == 1)
        {
          cout<<"Numerele prime dintre "<< min << " si "<<max<< " sunt: ";
          while(min<max)
            {
              flag = 0;

              for(i = 2; i<=min/2; i++)
                {
                  if(min % i == 0)
                    {
                      flag = 1;
                      break;
                    }
                }
            if(flag == 0)
              cout<< min<< " ";
            min++;
          }
        }
      else
      {
        rezultat<<"Numerele prime dintre "<< min << " si "<<max<< " sunt: ";
        while(min<max)
          {
            flag = 0;

            for(i = 2; i<=min/2; i++)
              {
                if(min % i == 0)
                  {
                    flag = 1;
                    break;
                  }
              }
          if(flag == 0)
            rezultat<< min<< " ";
          min++;
        }
      }
    }
  else
    {
      cout<<"Apsa tasta 1 daca vrei ca rezultatul sa fie scris in CMD sau tasta 2 daca vrei sa fie scris intr-un fisier anume(rez.out): ";
      cin>> inFisierSauInFolder;
      if(inFisierSauInFolder == 1)
        cout<<"Ca sa compilezi un program c++ ruleza aceste 2 comenzi in CMD: \n"<<"g++ FILE_NAME -o EXECUTABLE_NAME.exe \n"<< "EXECUTABLE_NAME";
      else
        rezultat<<"Ca sa compilezi un program c++ ruleza aceste 2 comenzi in CMD: \n"<< "g++ FILE_NAME -o EXECUTABLE_NAME.exe \n"<< "EXECUTABLE_NAME";
    }
    rezultat.close();
}
