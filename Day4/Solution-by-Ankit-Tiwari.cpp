/*
 * mahawiki3.cpp
 *
 *  Created on: Feb 2, 2019
 *      Author: ankit
 */
#include <math.h>
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
typedef long long ll;
#define M 1000000007

using namespace std;
vector<vector <ll> > dp;
ll ans;
ll cal_ways(int n, int i, int j)
{

    if(i == n-1)
        return 1;

    if(dp[i][j] != -1)
        return dp[i][j];

    if(j ==  0)
        ans = cal_ways( n, i+1, j+1)%M;
    else if(j == n-1)
        ans = cal_ways(n,i+1, j-1)%M;
    else
        ans =  ( cal_ways(n, i+1, j+1) + cal_ways(n,i+1, j-1) )%M;

    dp[i][j] = ans;
    return ans;
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int t, n;
    cin >> t;

    while(t--)
    {
        ans = 0;
        cin >> n;
        dp.resize(n);
        for(int i =0 ;i < n; i++)
        {
            dp[i].resize(n);
            for(int j =0 ;j < n ;j++)
            {
                dp[i][j] = -1;
            }
        }
        ans = cal_ways(n, 0, (n-1)/2);//size, i, j
        cout << ans << "\n";
    }
    return 0;
}
