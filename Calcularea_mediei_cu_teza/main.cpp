#include<iostream>
#include<math.h>
#include<string.h>
using namespace std;
int main()
{
    float media_notelor=0,n1=0,n2=0,n3=0,nt=0,note,teza,media_finala=0;
    cout<<"Cate note ai? ";
    cin>>note;
    cout<<"Vrei media cu teza? 1 = (Da) ; 2 = (Nu) ";
    cin>>teza;
    if(note == 2)
        {
            if(teza == 1)
                {
                    cout<<"Ce note ai? ";
                    cin>>n1>>n2;
                    cout<<"Ce nota ai in teza? ";
                    cin>>nt;
                    media_notelor = (n1 + n2) / 2;
                    media_finala = (3*media_notelor + nt)/4;
                    cout<<"Media finala este: "<<media_finala;
                }
            if(teza == 2)
                {
                    cout<<"Ce note ai? ";
                    cin>>n1>>n2;
                    media_notelor = (n1 + n2)/2;
                    cout<<"Media finala este: "<<media_notelor;
                }
        }
    if(note == 3)
        {
            if(teza == 1)
                {
                    cout<<"Ce note ai? ";
                    cin>>n1>>n2>>n3;
                    cout<<"Ce nota ai in teza? ";
                    cin>>nt;
                    media_notelor = (n1 + n2 + n3)/3;
                    media_finala = (3*media_notelor + nt)/4;
                    cout<<"Media finala este: "<<media_finala;
                }
            if(teza == 2)
                {
                    cout<<"Ce note ai? ";
                    cin>>n1>>n2>>n3;
                    media_notelor = (n1 + n2 + n3)/3;
                    cout<<"Media finala este: "<<media_finala;
                }
        }
}