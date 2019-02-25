/*
@author -> Aman Gupta
*/

#include<bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);    

    int T;
    cin>>T;

    while(T--) {
        long long n, m, ans = 0;
        cin>>n>>m;
        
        if(min(n, m) == 1) cout<<max(n, m)<<'\n';
        else if(min(n, m) == 2) 
        {
            long long x = max(n, m);
            long long g = (x % 4 == 0)? x/4 : x/4+1;
            long long rp = 2 + (g - 1) * 4;
            if(x % 4 == 1) cout<<rp<<'\n';
            else cout<<rp+2<<'\n';
        }
        else if((n * m) % 2 == 0) cout<<(n*m)/2<<'\n';
        else cout<<(n*m + 1)/2<<'\n';
    }
}
