#!/usr/bin/python
"""
This is a module presenting solutions to Travelling Salesman problem.
It feature functions to generate a map of towns, check its validity, and
compare solutions. There are two implemented TSP solutions - Brute Solution,
which checks every possible path, what amounts to really long execution time
when numer of towns > 10, since it's O(n!). The other solution is Nearest
Neighbor algorithm, a greedy algorithm, which performs pretty fast (it's
O(n^2), but doesn't always return the best solutions. This allows us to
compare fast and unreliable solution with slow and reliable one. We can also
generate towns on euclidean plane and use gnuplot to show, what path each
algorithm founds for given map.
"""
import Gnuplot
from random import randint
from math import sqrt


def validate_towns(towns):
    """Check if towns is a correct towns map.

    Args:
        towns: dictionary to check.

    Return:
        True if this is a correct towns map.
    """
    if not isinstance(towns, dict):
        return False
    town_set = set(towns.keys())
    if len(town_set) < 2:
        return False
    for itself, town in towns.items():
        if (not isinstance(town, dict) or
           set(town.keys()) != (town_set - set([itself])) or
           not all(distance >= 0 for distance in town.values())):
            return False
    return True


def calculate_distance(points):
    """Return distance between points on an euclidean plane

    Args:
        points: list of points as tuple(x, y).

    Return:
        Valid map of towns (dictionary).
    """
    towns = {}
    for idx, point in enumerate(points):
        towns[idx] = {}
        for jdx, neighbor in enumerate(points):
            if idx == jdx:
                continue
            towns[idx][jdx] = sqrt((point[0] - neighbor[0])**2 +
                                   (point[1] - neighbor[1])**2)
    return towns


def generate_euclidean_towns(num):
    """Generate valid euclidean towns and a map based on it.

    Args:
        num: number of towns to generate.

    Return:
        A dictionary-map of towns and list of points
    """
    points = [0] * num
    for idx in range(0, num):
        points[idx] = (randint(0, 500), randint(0, 500))
    towns = calculate_distance(points)
    return {"towns": towns, "points": points}


def generate_towns(num):
    """Generate a valid map of regular towns (not necessairly euclidean)

    Args:
        num: number of towns to generate

    Return:
        A dictionary-map
    """
    towns = {}
    for i in range(0, num):
        towns[i] = {j: randint(0, 99) for j in range(0, num) if j != i}
    return towns


def gnuplotify(route, points, title):
    """Transform towns route and points into gnuplot-readable data

    Args:
        route: list of points indexes to visit in order
        points: list of points on a euclidean plane as (x, y)
        title: string title for gnuplot plot

    Return:
        Gnuplot.py's PlotItem containing points connected in series of lines
    """
    out_points = []
    for stop in route:
        out_points += [points[stop]]
    out_points += [points[route[0]]]
    d = Gnuplot.Data(out_points,
                     title=title,
                     with_='lines')
    return d


class BruteSolution:
    """Brute solution for TSP problem

    Attributes:
        towns: map of towns to visit
        visited: a dictionary with boolean values to determine, which towns
            were visited.
    """
    def __init__(self, towns):
        self.towns = towns
        self.visited = {town: False for town in self.towns}

    def solve(self):
        return min((self.recursive(town, town) for town in self.towns),
                   key=lambda item: item[1])

    def recursive(self, current, start):
        """ The function which does all the work of finding the shortest path
        It's really time-expensive and may take a very long time for path
        consisting of more than 10 points.

        Attributes:
            current: currently visited town
            start: town from which we started (used for returning when all
                towns have been visited)
        Returns:
            Tuple: the list with points representing the best path from here
                to the end, and distance cost of this path
        """

        self.visited[current] = True

        unvisited = [t for t in self.towns if self.visited[t] is False]
        if not unvisited:
            self.visited[current] = False
            return [current], self.towns[current][start]

        best = {"route": [], "cost": -1}
        for target in unvisited:
            route, cost = self.recursive(target, start)
            cost += self.towns[current][target]
            if cost < best["cost"] or best["cost"] == -1:
                best["route"], best["cost"] = route, cost

        self.visited[current] = False
        return [current] + best["route"], best["cost"]


class NearestNeighbor:
    """Nearest Neighbor solution for TSP problem

    Attributes:
        towns: map of towns to visit
    """
    def __init__(self, towns):
        self.towns = towns

    def solve(self, start=0):
        """ The function which does all the work of finding the shortest path.
        It's pretty quick - O(n^2), but very often doesn't produce the best
        path.

        Attributes:
            current: currently visited town
            start: town from which we started (used for returning when all
                towns have been visited)
        Returns:
            Tuple: the list with points representing the best path from here
                to the end, and distance cost of this path
        """
        length = len(self.towns)
        route = [start]
        cost = 0
        for i in range(1, length):
            target = min(((town, cost) for (town, cost)
                         in self.towns[route[-1]].items()
                         if town not in route),
                         key=lambda item: item[1])
            route += [target[0]]
            cost += target[1]
        return route, cost + self.towns[route[-1]][route[0]]


def graph_compare(towns, points):
    """Compare Brute and Nearest Neighbor solution for given map of euclidean
    towns. Print out best ways, its' costs and show gnuplot image to visually
    compare paths.

    Attributes:
        towns: map of towns to visit
        points: list of points on a euclidean plane as (x, y)
    """
    g = Gnuplot.Gnuplot()

    print("Punkty: " + str(points))
    town_map = Gnuplot.Data([(x, y, idx) for (idx, (x, y))
                            in enumerate(points)],
                            with_='labels')
    bs1 = BruteSolution(towns)
    route, cost = bs1.solve()
    bs_data = gnuplotify(route, points, "Brute solution")
    print("BruteSolution\nCost:" + str(cost) + "\n" + str(route))

    nn1 = NearestNeighbor(towns)
    route, cost = nn1.solve()
    nn_data = gnuplotify(route, points, "Nearest neighbor")
    print("NearestNeighborSolution\nCost:" + str(cost) + "\n" + str(route))

    g.plot(bs_data, nn_data, town_map)
    raw_input("--- Press return ---")


