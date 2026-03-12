'''
A logistics platform encodes shipping routes as a colon-delimited string. Each entry contains
origin, destination, carrier, and cost. Parse the string and answer cost queries.
Input Format
"US,UK,UPS,5:US,CA,FedEx,3:CA,UK,DHL,7:CA,MX,FedEx,4"
Format per entry: origin,destination,carrier,cost
Part 1 — Direct Route Cost
Return the cost of a direct route, or -1 if none exists.
def get_direct_cost(route_string: str, origin: str, destination: str) -> int:
get_direct_cost("US,UK,UPS,5:US,CA,FedEx,3:CA,UK,DHL,7", "US", "UK") # 5
get_direct_cost("US,UK,UPS,5:US,CA,FedEx,3:CA,UK,DHL,7", "US", "MX") # -1
Part 2 — Cheapest Two-Hop Route
Find the cheapest route using exactly one intermediate stop, or -1 if none.
def get_cheapest_two_hop(route_string: str, origin: str, destination: str) -> int:
get_cheapest_two_hop("US,UK,UPS,5:US,CA,FedEx,3:CA,UK,DHL,7", "US", "UK") # 10
# US->CA (3) + CA->UK (7) = 10
Constraints
• cost is always a positive integer
• Multiple direct routes between same pair may exist — return cheapest
• Route string may be empty — return -1
Extension (Bonus)
Extend Part 2 to find cheapest route with any number of hops (shortest path problem)
'''

#part 1
def get_direct_cost(route_string: str, origin: str, destination: str) -> int:
    parsed_route_string = route_string.split(":")
    routes = []
    for entry in parsed_route_string:
        fields = entry.split(',')
        route = {
            "origin": fields[0],
            "destination": fields[1],
            "carrier": fields[2],
            "cost": int(fields[3])
        }
        routes.append(route)
    for route in routes:
        if route["origin"] == origin and route["destination"] == destination:
            print(f"cost: {route["cost"]}")
            return route["cost"]
    return -1

# get_direct_cost("US,UK,UPS,5:US,CA,FedEx,3:CA,UK,DHL,7", "US", "UK") # 5
# get_direct_cost("US,UK,UPS,5:US,CA,FedEx,3:CA,UK,DHL,7", "US", "MX") # -1


def parse_routes(route_string:str) ->dict:
    parsed_route_string = route_string.split(":")
    routes = []
    for entry in parsed_route_string:
        fields = entry.split(',')
        route = {
            "origin": fields[0],
            "destination": fields[1],
            "carrier": fields[2],
            "cost": int(fields[3])
        }
        routes.append(route)
    print(routes)
    return routes
#Part 2
def get_cheapest_two_hop(route_string: str, origin: str, destination: str) -> int:
    routes = parse_routes(route_string)
    best = -1
    for route1 in routes:
        for route2 in routes:
            if (route1["origin"] == origin and route2["destination"] and route1["destination"] == route2["origin"]):
                cost = route1["cost"] + route2["cost"]
                if best == -1 or cost < best:
                    best = cost
    print(best)
    return best
        
get_cheapest_two_hop("US,UK,UPS,5:US,CA,FedEx,3:CA,UK,DHL,7", "US", "UK")