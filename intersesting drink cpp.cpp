#include<bits/stdc++.h>
using namespace std;
#define ll long long 
int main()
{
	ll n,m,cd;
	ll arr[n]={0};
	cin>>n;
	for(int i=0;i<n;i++)
	{
		ll a;
		cin>>a;
		arr[i]=a;
	}
	sort(arr,arr+n)
	cin>>m;
	for(int i=0;i<m;i++)
	{
		cin>>cd;
		cou<<lower_bound(a,a+n,cd)-arr<<endl;
	}





}