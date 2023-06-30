
import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations

def create_network_diagram(n, m, qualifications, k):
    G = nx.Graph()

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
                G.add_edge(u, v)

    return G

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

# Draw the network diagram
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=12, font_weight='bold', edge_color='gray')
plt.title("Qualifications Network Diagram")
plt.show()
