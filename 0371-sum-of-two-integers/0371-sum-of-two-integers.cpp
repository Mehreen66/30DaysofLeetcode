class Solution {
public:
    int getSum(int a, int b) {
    if(b>0){
      while(b>0)
      {
          a++;
          b--;
      }
        return a;
    }
    
    else
    {while(b<0)
      {
          a--;
          b++;
      }
        return a;
        }
    }
    
};