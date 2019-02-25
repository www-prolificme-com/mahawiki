#include<iostream>
using namespace std;
#define mod 1000000007
int main()
{
  long long int t,n,i,j ;
  cin>>t ;
  //srand(time(0)) ;
  while(t--){
    cin>>n ;
    long long matr[100][100],ans=0 ;
    for (i=0;i<n;i++){
      for (j=0;j<n;j++){
        matr[i][j] = 0 ;
      }
    }
    matr[0][n/2] = 1 ;
    for (i=1;i<n;i++){
      for (j=0;j<n;j++){
        if (j==0){
          matr[i][j] = matr[i-1][j+1] ;
        }
        else if (j==(n-1)){
          matr[i][j] = matr[i-1][j-1] ;
        }
        else{
          matr[i][j] = matr[i-1][j-1] + matr[i-1][j+1] ;
        }
      }
    }
    for (i=0;i<n;i++)
        ans+=matr[n-1][i] ;
    cout<<ans<<endl ;  
  }

  return 0 ;
}

GridSolution.cpp
Displaying GridSolution.cpp.
