
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

# example with 5 airport sites, 6 flights, and their respective costs:

n = 5
m = 6
costs = [10, 5, 8, 12, 7]
flights = [
    [0, 1], # Flight from airport 0 to 1
    [1, 2], # Flight from airport 1 to 2
    [2, 3], # Flight from airport 2 to 3
    [3, 4], # Flight from airport 3 to 4
    [4, 0], # Flight from airport 4 to 0
    [2, 0]  # Flight from airport 2 to 0
]

selected_sites = build_service_facility(n, m, costs, flights)
print(selected_sites)


