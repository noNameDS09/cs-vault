// You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.

// Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

// Return a list of integers representing the size of these parts.

 

// Example 1:

// Input: s = "ababcbacadefegdehijhklij"
// Output: [9,7,8]
// Explanation:
// The partition is "ababcbaca", "defegde", "hijhklij".
// This is a partition so that each letter appears in at most one part.
// A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
// Example 2:

// Input: s = "eccbbbbdec"
// Output: [10]
 

// Constraints:

// 1 <= s.length <= 500
// s consists of lowercase English letters.

class Solution {
public:
    vector<int> partitionLabels(string s) {
        unordered_map<char, int> mp;

        for(int i=0; i<s.size(); i++){
            mp[s[i]]=i;
        }
        
        vector<int> ans;
        int res=0;

        int i=0, j=0;
        int n=s.size();
        while(i<n){
            int end = mp[s[i]];
            while(j < n && j < end){
                if(end < mp[s[j]]) end= max(end, mp[s[j]]);
                j++;
                if(end == j) break;
            }
            ans.push_back(j-i+1);
            i=j+1;
        }

        return ans;
    }
};