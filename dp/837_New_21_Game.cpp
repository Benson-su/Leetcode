class Solution {
public:
    double new21Game(int n, int k, int maxPts) {
        if (k==0){
            return 1;
        }
        vector<double> dp(n+1, 0);
        dp[0] = 1.0;
        double sum = 1.0;
        for(int i = 1;i < n+1; i++){
            dp[i] = sum / maxPts;
            if(i < k){
                sum += dp[i];
            }
            if(i >= maxPts && i < k+maxPts){
                sum -= dp[i - maxPts];
            }
        }
        double ret = 0;
        for(int i=k; i < n+1; i++){
            ret += dp [i];
        }
        return ret;

    }
};
