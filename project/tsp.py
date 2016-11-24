from random import randint
TOWN_NUM = 10

class BruteSolution:
    def __init__(self, towns):
        self.towns = towns
        self.visited = [False] * len(towns)

    def solve(self):
        return min((self._recursive(town, town) for town in self.towns),
                    key=lambda item: item[1])

    def _recursive(self, current, start):
        self.visited[current] = True

        if all(v == True for v in self.visited):
            self.visited[current] = False
            return [current], self.towns[current][start]

        unvisited = [town for town in self.towns if self.visited[town] == False]

        best = {"route": [], "cost": -1}
        for target in unvisited:
            route, cost = self._recursive(target, start)
            cost += self.towns[current][target]
            if cost < best["cost"] or best["cost"] == -1:
                best["route"], best["cost"] = route, cost

        self.visited[current] = False
        return [current] + best["route"], best["cost"]



class NearestNeighbor:
    def __init__(self, towns):
        self.towns = towns

    def solve(self):
        length = len(self.towns)
        route = [ randint(0, length-1) ]
        cost = 0
        for i in range(1, length):
            target = min(((town, cost) for (town, cost)
                        in self.towns[route[-1]].items() if town not in route),
                        key = lambda item: item[1])
            route += [target[0]]
            cost += target[1]
        return route, cost + self.towns[route[-1]][route[0]]



towns = {}
for i in range(0, TOWN_NUM):
    towns[i] = {j : randint(0, 99) for j in range(0, TOWN_NUM) if j != i}

bs = BruteSolution(towns)
print(bs.solve())
nn = NearestNeighbor(towns)
print(nn.solve())

