#include <bits/stdc++.h>
using namespace std;

vector<int> kmp(string s, string p){
    int n=s.size(), m=p.size(), i=0, j=0;
    vector<int> lps(m), ans;
    for(int i=1, j=0; i<m;){
        if(p[i] == p[j]) lps[i++]=++j;
        else if (j) j=lps[j-1];
        else lps[i++]=0;
    }
    i=0, j=0;
    while(i<n){
        if(s[i] == p[j]) i++, j++;
        if(j==m) ans.push_back(i-j), j=lps[j-1];
        else if (i<n && s[i]!=p[j]) j?j=lps[j-1]:i++;
    }
    return ans;
}

int main() {
	// your code goes here
    ios::sync_with_stdio(0);
    cin.tie(0);
    string s, p; cin >> s >> p;
    for(int x: kmp(s, p)) cout << x << " ";
}
    