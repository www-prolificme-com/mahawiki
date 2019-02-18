/*
@author -> Aman Gupta
*/
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int t;
    cin>>t;
    while(t--) {
        long long n,ans;
        cin>>n;
        if(n<5) ans = n;
        else if(n==8) ans = 3;
        else if(n==9 or n==14 or n == 19) ans = 4;
         else ans = (n %6 == 0)?n/6:n/6+1;
        cout<<ans<<'\n';
        }
    return 0;
}
