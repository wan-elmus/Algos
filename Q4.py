
def find_maximum_reward(n, rewards, conflicts):
    DP = [0] * (n + 1)

    for i in range(1, n + 1):
        DP[i] = max(DP[i - 1], DP[i - 2] + rewards[i - 1])

    selected_jobs = set()
    i = n

    while i > 0:
        if i == n or conflicts[i - 2][i - 1]:
            selected_jobs.add(i - 1)
            i -= 2
        else:
            i -= 1

    return selected_jobs

# Example usage
n = 5
rewards = [10, 15, 5, 8, 12]
conflicts = [
    [False, True, False, True, False],
    [True, False, True, False, True],
    [False, True, False, True, False],
    [True, False, True, False, True],
    [False, True, False, True, False]
]

selected_jobs = find_maximum_reward(n, rewards, conflicts)
print(selected_jobs)

