#include<iostream>
#include<string.h>
#include<cstring>
#include<fstream>
using namespace std;

struct {
    int mustangStock = 1;
} Stock;

struct {
    int opelStock = 1;
} opelStock;

struct {
    int aprovizionare = 0;
} aprovizionate;

int main()
{
    char optiune_model[101];
    cout<< "Alegeti masina dorita dintre Mustang si Opel ";
    cin>>optiune_model;
    cout<<Stock.mustangStock;

    if((optiune_model == "Mustang") && (Stock.mustangStock >= 1))
            {
                cout<<"Masina Mustang este valabila";
                Stock.mustangStock = Stock.mustangStock - 1;
            }
        else if(Stock.mustangStock < 1)
            {
                cout<<"Masina Mustang nu este valabila. O sa reaprovizionam in scurt timp";
                Stock.mustangStock = Stock.mustangStock + 10;

            }
        
}