class Solution {
public:
    bool isAnagram(string s, string t) {
        sort(t.begin(),t.end());
        sort(s.begin(),s.end());
        std::cout << "Sorted string: " << t<< std::endl;
        if(s==t)
        {return true;}
         else   
        return false;
    }
};