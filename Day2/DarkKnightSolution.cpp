#include<iostream>
using namespace std;

int main(){

	long long int t ;
	cin>>t ;
	while(t--){
		long long int n,m ;
		cin>>n>>m ;
		if (n==1 || m==1)
			cout<<max(n,m)<<endl ;
		else if (n==2){
			if (m%4==1){
				cout<<m+1<<endl ;
			}
			else if (m%4==0){
				cout<<m<<endl ;
			}
			else{
				cout<<((m/4) + 1)*4<<endl ;
			}
		}
		else if (m==2){
			if (n%4==1){
				cout<<n+1<<endl ;
			}
			else if (n%4==0){
				cout<<n<<endl ;
			}
			else{
				cout<<((n/4) + 1)*4<<endl ;
			}
		}
		else if (n%2==0 || m%2==0)
			cout<<(n*m)/2<<endl ;
		else
			cout<<((n*m)/2 + 1)<<endl ;
	}
	return 0 ;
}
