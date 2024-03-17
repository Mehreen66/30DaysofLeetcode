class Solution {
public:
    bool isPalindrome(int x) {
       int64_t rev=0;
       int org=x;
       int remainder=0;
       while(x>0)
       {
        remainder=x%10;
        rev=(rev*10)+remainder;
        x=x/10;
       }
        
        if(org==rev)
        {
            return true;
        }
        else
        {
            return false;
        }
       
        }
};