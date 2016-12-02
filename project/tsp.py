#!/usr/bin/python
import unittest
import Gnuplot
from random import randint
from math import sqrt
GEN_TOWN_NUM = 6


def _validate_towns(towns):
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


def _calculate_distance(points):
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


def _generate_euclidean_towns(num):
    """Generate valid euclidean towns and a map based on it.

    Args:
        num: number of towns to generate.

    Return:
        A dictionary-map of towns and list of points
    """
    points = [0] * num
    for idx in range(0, num):
        points[idx] = (randint(0, 500), randint(0, 500))
    towns = _calculate_distance(points)
    return {"towns": towns, "points": points}


def _generate_towns(num):
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


def _gnuplotify(route, points, title):
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
        return min((self._recursive(town, town) for town in self.towns),
                   key=lambda item: item[1])

    def _recursive(self, current, start):
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
            route, cost = self._recursive(target, start)
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


def _graph_compare(towns, points):
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
    bs_data = _gnuplotify(route, points, "Brute solution")
    print("BruteSolution\nCost:" + str(cost) + "\n" + str(route))

    nn1 = NearestNeighbor(towns)
    route, cost = nn1.solve()
    nn_data = _gnuplotify(route, points, "Nearest neighbor")
    print("NearestNeighborSolution\nCost:" + str(cost) + "\n" + str(route))

    g.plot(bs_data, nn_data, town_map)
    raw_input("--- Press return ---")


class TestPoint(unittest.TestCase):

    def setUp(self):
        self.t1 = {"Krakow": {1: 10}, 1: {"Krakow": 15}}
        self.t2 = {0: {1: 1, 2: 5}, 1: {0: 1, 2: 2}, 2: {0: 1000, 1: 10}}
        self.wrong1 = {0: {0: 5, 1: 10}, 1: {0: 7, 1: 20}}
        self.wrong2 = {0: {1: -1}, 1: {0: 1}}
        self.gen1 = _generate_towns(5)
        self.gen2 = _generate_towns(6)
        self.gen3 = _generate_towns(7)
        self.gen4 = _generate_towns(30)
        self.gen5 = _generate_towns(50)
        self.euc1 = _generate_euclidean_towns(4)
        self.euc2 = _generate_euclidean_towns(6)
        self.euc3 = _generate_euclidean_towns(8)

        self.euc4 = {}
        self.euc4["points"] = [(100, 100), (300, 300), (200, 150), (400, 100)]
        self.euc4["towns"] = _calculate_distance(self.euc4["points"])

        self.euc5 = {}
        self.euc5["points"] = [(100, 100), (200, 150), (250, 320),
                               (322, 828), (555, 355)]
        self.euc5["towns"] = _calculate_distance(self.euc4["points"])

    def test_validation(self):
        self.assertTrue(_validate_towns(self.t1))
        self.assertTrue(_validate_towns(self.t2))
        self.assertFalse(_validate_towns(self.wrong1))
        self.assertFalse(_validate_towns(self.wrong2))

    def test_generation(self):
        self.assertTrue(_validate_towns(self.gen1))
        self.assertTrue(_validate_towns(self.gen2))
        self.assertTrue(_validate_towns(self.gen3))
        self.assertTrue(_validate_towns(self.gen4))
        self.assertTrue(_validate_towns(self.gen5))
        self.assertTrue(_validate_towns(self.euc1["towns"]))

    def test_brute_precoded(self):
        # Pre-coded towns
        bs1 = BruteSolution(self.t1)
        nn1 = NearestNeighbor(self.t1)
        self.assertEqual(bs1.solve(), nn1.solve(1))

        bs2 = BruteSolution(self.t2)
        nn2 = NearestNeighbor(self.t2)
        self.assertLessEqual(bs2.solve()[1], nn2.solve()[1])

    def test_brute_gen(self):
        # Brute should never output worse solution than nearest neighbor
        bs1 = BruteSolution(self.gen1)
        nn1 = NearestNeighbor(self.gen1)
        self.assertLessEqual(bs1.solve()[1], nn1.solve()[1])

        bs2 = BruteSolution(self.gen2)
        nn2 = NearestNeighbor(self.gen2)
        self.assertLessEqual(bs2.solve()[1], nn2.solve()[1])

        bs3 = BruteSolution(self.gen3)
        nn3 = NearestNeighbor(self.gen3)
        self.assertLessEqual(bs3.solve()[1], nn3.solve()[1])

    def test_euclidean(self):
        _graph_compare(self.euc1["towns"], self.euc1["points"])
        _graph_compare(self.euc2["towns"], self.euc2["points"])
        _graph_compare(self.euc3["towns"], self.euc3["points"])
        _graph_compare(self.euc4["towns"], self.euc4["points"])
        _graph_compare(self.euc5["towns"], self.euc5["points"])

    def tearDown(self): pass


if __name__ == "__main__":
    unittest.main()
