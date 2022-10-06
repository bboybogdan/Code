#include<iostream>
#include<string.h>
#include<vector>
using namespace std;
int v[11];
int suma(int n, int s){
	int u,i,a,p=1,b;
	while(n!=0)
		{
			u=n%10;
			v[u]++;
			n=n/10;
		}
	for(i=1;i<=9;i++)
		if(v[i] != 0 && i%2==1)
			s = s + i;
	for(i=0;i<=10;i++)
		if(v[i] != 0)
			cout<<i<<" apare de "<<v[i]<<" ori"<<endl;
	for(i=10;i>=0;i--)
		{
			if(v[i] != 0)
				if(v[i] > 1)
					cout<<i<<i;
			else
				cout<<i;
		}
	cout<<endl;
	return s;
}

int main()
{
	int n,s;
	cin>>n;
	cout<<suma(n,s);
}
