#include<iostream>
using namespace std;

int __gcd(int a, int b) 
{ 
    if (b == 0) 
        return a; 
    return __gcd(b, a % b);  
      
} 

int main(){

	long long int t,a,b ;
	cin>>t ;
	while(t--){
		cin>>a>>b ;
		cout<<max(a,b)/__gcd(a,b)<<endl ;
	}
	return 0 ;
}
