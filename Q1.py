
def minimize_weighted_completion_times(jobs, weights):
    n = len(jobs)
    total_time = sum(jobs)
    DP = [[0] * (total_time + 1) for _ in range(n + 2)]

    # Step 1: Create the dynamic programming table DP
    for i in range(n, 0, -1):
        for t in range(total_time, -1, -1):
            if t + jobs[i-1] <= total_time:
                Ci = max(DP[i+1][t], t + jobs[i-1])
                if t < total_time:
                    DP[i][t] = min(weights[i-1] * Ci + DP[i+1][t+1], DP[i+1][t])
                else:
                    DP[i][t] = weights[i-1] * Ci
            else:
                DP[i][t] = DP[i+1][t]

    ordering = []
    i = 1
    t = 0

    # Step 2: Backtrack to determine the optimal job ordering
    while i <= n:
        if weights[i-1] * max(DP[i+1][t], t + jobs[i-1]) + DP[i+1][t+1] > DP[i+1][t]:
            ordering.append(i)
            t = t + jobs[i-1]
        i = i + 1

    return ordering

# Example usage:
jobs = [4, 3, 2, 1]
weights = [2, 1, 3, 4]
ordering = minimize_weighted_completion_times(jobs, weights)
print(ordering)



