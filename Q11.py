
import networkx as nx
import matplotlib.pyplot as plt

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

def create_network_diagram(ordering, jobs):
    n = len(ordering)
    G = nx.DiGraph()

    # Add nodes to the graph
    for i in range(n):
        job = ordering[i]
        G.add_node(job, weight=jobs[job-1])

    # Add edges to the graph based on job dependencies
    for i in range(n-1):
        job1 = ordering[i]
        job2 = ordering[i+1]
        G.add_edge(job1, job2)

    return G

# Example usage:
jobs = [4, 3, 2, 1]
weights = [2, 1, 3, 4]
ordering = minimize_weighted_completion_times(jobs, weights)
print("Job Ordering:", ordering)

# Create the network diagram
G = create_network_diagram(ordering, jobs)

# Draw the network diagram
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=12, font_weight='bold', edge_color='gray')
plt.title("Job Dependencies Network Diagram")
plt.show()
