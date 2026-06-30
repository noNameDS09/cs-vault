// 838. Push Dominoes
// Solved
// Medium
// Topics
// premium lock icon
// Companies
// There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

// After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

// When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

// For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

// You are given a string dominoes representing the initial state where:

// dominoes[i] = 'L', if the ith domino has been pushed to the left,
// dominoes[i] = 'R', if the ith domino has been pushed to the right, and
// dominoes[i] = '.', if the ith domino has not been pushed.
// Return a string representing the final state.

 

// Example 1:

// Input: dominoes = "RR.L"
// Output: "RR.L"
// Explanation: The first domino expends no additional force on the second domino.
// Example 2:


// Input: dominoes = ".L.R...LR..L.."
// Output: "LL.RR.LLRRLL.."


class Solution {
public:
    string pushDominoes(string dom) {
        int n = dom.size();
        vector<int> leftR(n, -1); 
        vector<int> rightL(n, -1); 

        for(int i = 0; i < n; i++){
            if(dom[i] == 'R') leftR[i] = i;
            else if(dom[i] == 'L') leftR[i] = -1; 
            else if(i > 0) leftR[i] = leftR[i-1];
        }

        for(int i = n-1; i >= 0; i--){
            if(dom[i] == 'L') rightL[i] = i;
            else if(dom[i] == 'R') rightL[i] = -1; 
            else if(i < n-1) rightL[i] = rightL[i+1];
        }

        string res = "";
        for(int i = 0; i < n; i++){
            if(dom[i] != '.') {
                res.push_back(dom[i]);
                continue;
            }

            int l = leftR[i];
            int r = rightL[i];

            if(l == -1 && r == -1) res.push_back('.');
            else if(l == -1) res.push_back('L');
            else if(r == -1) res.push_back('R');
            else {
                int distL = i - l;
                int distR = r - i;
                if(distL < distR) res.push_back('R');
                else if(distR < distL) res.push_back('L');
                else res.push_back('.');
            }
        }
        return res;
    }
};
