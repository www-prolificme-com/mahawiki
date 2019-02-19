#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

long long int maxi(long long int x, long long int y) 
{
if(x>y){
    return x;
}
else{
return y;
}
}
long long int mini(long long int x, long long int y){
if(x<y){
return x;
}
else
return y;
}


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
long long int t;

    cin>>t;
    long long int m,n, ans=0;

    for(long long int i = 0;i < t; i++)
    {
        cin>>m>>n;

        if( m ==1||n ==1)
        {
            ans =  maxi(m,n);
        }
        else if( m == 2 || n == 2)
        {
            ans=(maxi(m,n)/4) *4;

            if( maxi(m,n)%4==1)
            {
                ans=ans+2;
            }
            else if( maxi(m,n)%4>1)
            {
                ans+=4;}
        }
        else
        {
            ans = ((m * n)+ 1) / 2; 
        }

        cout<< ans<<"\n";

    }     
    return 0;
}


