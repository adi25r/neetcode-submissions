class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // we want to accumulate the max profit
        int min = INFINITY;
        int maxP = 0;
        for (int num : prices) {
            if (num < min) min = num;
            if (num - min > maxP) maxP = num - min;
        }
        return maxP;
    }
};
