import json
import sys

class Network:
    def __init__(self, links):
        self.links = {}
        for link in links:
            point1, point2 = link["points"]
            capacity = link["capacity"]
            self.links[(point1, point2)] = capacity
            self.links[(point2, point1)] = capacity
        self.allocated = {link: 0 for link in self.links}

    def allocate(self, path, demand):
        for i in range(len(path) - 1):
            link = (path[i], path[i + 1])
            if self.allocated[link] + demand > self.links[link]:
                return False
        for i in range(len(path) - 1):
            link = (path[i], path[i + 1])
            self.allocated[link] += demand
        return True

    def deallocate(self, path, demand):
        for i in range(len(path) - 1):
            link = (path[i], path[i + 1])
            self.allocated[link] -= demand

def simulate(network, possible_circuits, simulation):
    events = []
    current_time = 0
    active_demands = []

    while current_time <= simulation["duration"]:
        for demand in simulation["demands"]:
            if demand["start-time"] == current_time:
                path = None
                for circuit in possible_circuits:
                    if circuit[0] == demand["end-points"][0] and circuit[-1] == demand["end-points"][1]:
                        path = circuit
                        break
                if path and network.allocate(path, demand["demand"]):
                    active_demands.append((demand, path))
                    events.append(f"{len(events) + 1}. igény foglalás: {demand['end-points'][0]}<->{demand['end-points'][1]} st:{current_time} – sikeres")
                else:
                    events.append(f"{len(events) + 1}. igény foglalás: {demand['end-points'][0]}<->{demand['end-points'][1]} st:{current_time} – sikertelen")

        for demand, path in active_demands[:]:
            if demand["end-time"] == current_time:
                network.deallocate(path, demand["demand"])
                active_demands.remove((demand, path))
                events.append(f"{len(events) + 1}. igény felszabadítás: {demand['end-points'][0]}<->{demand['end-points'][1]} st:{current_time}")

        current_time += 1

    return events

def main():
    if len(sys.argv) != 2:
        print("Használat: python3 client.py <json fájl>")
        return

    json_file = sys.argv[1]
    with open(json_file, 'r') as file:
        data = json.load(file)

    network = Network(data["links"])
    possible_circuits = data["possible-circuits"]
    simulation = data["simulation"]

    events = simulate(network, possible_circuits, simulation)
    for event in events:
        print(event)

if __name__ == "__main__":
    main()