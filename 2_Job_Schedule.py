def job_sequencing(jobs, deadlines, profits):
    n = len(jobs)
    slots = [-1]*n
    order = sorted(range(n), key=lambda i: profits[i], reverse=True)
    total_profit = 0
    for i in order:
        for j in range(deadlines[i]-1, -1, -1):
            if j < n and slots[j] == -1:
                slots[j] = jobs[i]
                total_profit += profits[i]
                break
    print("Job order:", [j for j in slots if j != -1])
    print("Total Profit:", total_profit)

jobs = ['A','B','C','D']
deadlines = [2,1,2,1]
profits = [100,19,27,25]
job_sequencing(jobs, deadlines, profits)


# TIME COMPLEXITY: O(n²)