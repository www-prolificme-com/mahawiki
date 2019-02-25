#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <bits/stdc++.h>
#define ll long long
using namespace std;


int main() {
    int t;
    cin >> t;
    while(t--) {
        ll a, b, res;
        cin >> a >> b;
        ll m_x = max(a, b);
        ll m_n = min(a, b);
        if(!(m_x % m_n)) res = m_x / m_n;
        else res = m_x / __gcd(m_x, m_n);
        cout << res << endl;
    }
    return 0;
}
