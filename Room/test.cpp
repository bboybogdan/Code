#include<iostream>
#include<math.h>
using namespace std;
int main()
{
    int axis_x,axis_y,m, n , A[101][101],i,j;
    cout<<"Alege cate coloane sa aibe ";
    cin>>m;
    cout<<"Alege cate linii sa aibe ";
    cin>>n;
    cout<<"Alege linia unde sa se afle punctul ";
    cin>> axis_x;
    cout<<"Alege coloana unde sa se afle punctul ";
    cin>> axis_y;
    for (i = 1;i<=m;i++)
        for (j = 1; j<= n ;j++)
            {
                if(i == axis_x && j == axis_y)
                    A[i][j] = 1;
                else 
                    A[i][j] = 0;
            }

    for( i = 1;i<=m ;i++){cout<<endl;
        for( j = 1; j<= n ;j++)     
            cout<<A[i][j]<<" ";}   
}