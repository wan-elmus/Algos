
import networkx as nx
import matplotlib.pyplot as plt

def create_network_diagram(n, rewards, conflicts):
    G = nx.DiGraph()

    # Add nodes to the graph representing jobs
    for i in range(n):
        G.add_node(i, reward=rewards[i])

    # Add edges based on the conflicts
    for i in range(n):
        for j in range(i):  # Consider only the lower triangular part of the conflicts matrix
            if conflicts[i][j]:
                G.add_edge(j, i)  # Reverse the direction of the edge

    return G

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

# Create the network diagram
G = create_network_diagram(n, rewards, conflicts)

# Draw the network diagram with arrows
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=12, font_weight='bold', edge_color='gray', arrows=True, arrowstyle='->', arrowsize=10)
plt.title("Job Network Diagram")
plt.show()

# Find the maximum reward jobs
selected_jobs = find_maximum_reward(n, rewards, conflicts)
print("Selected Jobs:", selected_jobs)
