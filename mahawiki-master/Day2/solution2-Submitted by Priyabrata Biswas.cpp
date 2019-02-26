//************************************************************************************************************************
//
// Submitted by Priyabrata Biswas
//Approach - I implemented the brute force method in solving this problem! Here is my solution:
//
//************************************************************************************************************************


#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#define ll long long
using namespace std;

int main() {
    int T;
    cin >> T;
    ll n, m;
    while(T--) {
        ll count_m[2], count_n[2], res;
        cin >> n >> m;
        if(n == 1) res = m;
        else if(m == 1) res = n;
        else if((n == 2 && m > 4) && (m & 1)) res = m + 1;
        else if((n == 2 && m > 4) && !(m & 1) && (m % 4)) res = m + 2;
        else if((m == 2 && n > 4) && (n & 1)) res = n + 1;
        else if((m == 2 && n > 4) && !(n & 1) && (n % 4)) res = n + 2;
        else if(n + m == 3) res = 2;
        else if(n + m == 4 || n + m == 5) res = 4;
        else if(m & 1) {
            count_m[0] = (m + 1) / 2;
            count_m[1] = (m - 1) / 2;
            if(n & 1) {
                count_n[0] = ((n + 1) / 2) * count_m[0];
                count_n[1] = ((n - 1) / 2) * count_m[1];
                res = count_n[0] + count_n[1];
            } else {
                count_n[0] = (n / 2) * count_m[0];
                count_n[1] = (n / 2) * count_m[1];
                res = count_n[0] + count_n[1];
            }
        } else {
            count_m[0] = m / 2;
            res = count_m[0] * n;
        }
        cout << res << endl;
    }
    return 0;
}

