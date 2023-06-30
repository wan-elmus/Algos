
import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations

def create_network_diagram(n, m, qualifications, k):
    G = nx.DiGraph()  # Use DiGraph instead of Graph to indicate the direction of edges

    # Add nodes to the graph representing applicants
    for i in range(m):
        G.add_node(i, label=f"Applicant {i}")

    # Add edges based on overlapping qualifications
    for comb in combinations(range(m), k):
        sports_covered = set(range(n))
        for applicant in comb:
            sports_covered &= set(i for i, qualified in enumerate(qualifications[applicant]) if qualified)
            if not sports_covered:
                break
        if sports_covered:
            for u, v in combinations(comb, 2):
                G.add_edge(u, v)  # Add directed edge from u to v

    return G

def hire_counselors(n, m, qualifications, k):
    for comb in combinations(range(m), k):
        sports_covered = set(range(n))
        for applicant in comb:
            sports_covered &= set(i for i, qualified in enumerate(qualifications[applicant]) if qualified)
            if not sports_covered:
                break
        if sports_covered:
            return True
    return False

# Example usage
n = 3
m = 5
qualifications = [
    [True, False, True],  # Applicant 0 is qualified for baseball and basketball
    [False, True, False], # Applicant 1 is qualified for volleyball
    [True, True, True],   # Applicant 2 is qualified for all sports
    [False, True, True],  # Applicant 3 is qualified for volleyball and basketball
    [True, True, False]   # Applicant 4 is qualified for baseball and volleyball
]
k = 3

# Create the network diagram
G = create_network_diagram(n, m, qualifications, k)

# Draw the network diagram with arrows
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=12, font_weight='bold', edge_color='gray', arrows=True, arrowstyle='->', arrowsize=10)
plt.title("Qualifications Network Diagram")
plt.show()

# Hire counselors
result = hire_counselors(n, m, qualifications, k)
print("Hire counselors:", result)
