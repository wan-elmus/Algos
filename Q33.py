
import networkx as nx
import matplotlib.pyplot as plt

def create_network_diagram(n, flights):
    G = nx.DiGraph()  # Use DiGraph instead of Graph to indicate the direction of flights

    # Add nodes to the graph representing airport sites
    for i in range(n):
        G.add_node(i, label=f"Airport {i}")

    # Add edges based on the flights
    for flight in flights:
        G.add_edge(flight[0], flight[1])

    return G

def build_service_facility(n, m, costs, flights):
    selected_sites = set()
    unserved_flights = set()

    for flight in flights:
        unserved_flights.add(flight[0])
        unserved_flights.add(flight[1])

    sorted_sites = sorted(range(n), key=lambda i: costs[i])

    for site in sorted_sites:
        if not unserved_flights:
            break

        site_covers_flight = False

        for flight in flights:
            if flight[0] == site or flight[1] == site:
                site_covers_flight = True
                unserved_flights.discard(flight[0])
                unserved_flights.discard(flight[1])

        if site_covers_flight:
            selected_sites.add(site)

    return selected_sites

# Example usage
n = 5
flights = [
    [0, 1], # Flight from airport 0 to 1
    [1, 2], # Flight from airport 1 to 2
    [2, 3], # Flight from airport 2 to 3
    [3, 4], # Flight from airport 3 to 4
    [4, 0], # Flight from airport 4 to 0
    [2, 0]  # Flight from airport 2 to 0
]

# Create the network diagram
G = create_network_diagram(n, flights)

# Draw the network diagram with arrows
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=12, font_weight='bold', edge_color='gray', arrows=True, arrowstyle='->', arrowsize=10)
plt.title("Airport Network Diagram")
plt.show()

# Build the service facility
m = len(flights)
costs = [10, 5, 8, 12, 7]
selected_sites = build_service_facility(n, m, costs, flights)
print("Selected Sites:", selected_sites)
