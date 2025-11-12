def binomial_coeff(n, k):
    C=[[0]*(k+1) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(min(i,k)+1):
            C[i][j]=1 if j==0 or j==i else C[i-1][j-1]+C[i-1][j]
    print("C(%d,%d) ="%(n,k), C[n][k])

binomial_coeff(5,2)


# TIME COMPLEXITY: O(nk)