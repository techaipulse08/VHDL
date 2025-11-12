def solve_knapsack():
    val=[50,100,150,200] #value array
    wt=[8,16,32,40] # Weight array
    W=64
    n=len(val) - 1
    def knapsack(W,n): # (Remaining Weight, Number of items checked)
        #base case
        if n<0 or W<=0:
            return 0
        
        #Higher weight than available
        if wt[n]>W:
            return knapsack(W, n-1)
        
        else:
            return max(val[n] + knapsack(W-wt[n],n-1),knapsack(W,n-1))
            # max(including , not including)
    print(knapsack(W,n))

if __name__=="__main__":
    solve_knapsack()
    
    
    
# def knapsack(W, wt, val, n):
#     dp = [[0]*(W+1) for _ in range(n+1)]
#     for i in range(1,n+1):
#         for w in range(1,W+1):
#             if wt[i-1]<=w:
#                 dp[i][w]=max(val[i-1]+dp[i-1][w-wt[i-1]],dp[i-1][w])
#             else:
#                 dp[i][w]=dp[i-1][w]
#     print("Maximum value:", dp[n][W])

# knapsack(50, [10,20,30], [60,100,120], 3)

# TIME COMPLEXITY: O(nW)
