class Solution {
public:
    bool isIsomorphic(string s, string t) {

        if (s.length()  != t.length()){
            return false;
        }

        unordered_map<char, char> mapST;
        unordered_map<char, char> mapTT;

        for (int i=0; i< s.length(); i++){

            char schar = s[i];
            char tchar = t[i];

            if (mapST.count(schar)){
                if (mapST[schar] != tchar){
                    return false;
                }

            } else {
                mapST[schar] = tchar;

            }

            if (mapTT.count(tchar)){
                if (mapTT[tchar] != schar){
                    return false;
                }

            } else {
                mapTT[tchar] = schar;

            }



        } 

        return true;


        
    }
};
