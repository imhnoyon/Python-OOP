#include<bits/stdc++.h>
using namespace std;
int main()
{
  int N;
  cin>>N;
  
  for(int i=0;i<N;i++)
  {     
      if(i==0){
        cout<<N<<endl;
      }
      for(int j=0;j<=i;j++)
      {
        cout<<'#';
      }
      cout<<endl;
  }
  return 0;
}