#!/usr/bin/python
import unittest
import Gnuplot
from random import randint
from math import sqrt
GEN_TOWN_NUM = 6


def _validate_towns(towns):
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


def _generate_euclidean_towns(num):
    towns = {}
    points = [0] * num
    for idx in range(0, num):
        points[idx] = (randint(0, 500), randint(0, 500))
    for idx, point in enumerate(points):
        towns[idx] = {}
        for jdx, neighbor in enumerate(points):
            if idx == jdx:
                continue
            towns[idx][jdx] = sqrt((point[0] - neighbor[0])**2 +
                                   (point[1] - neighbor[1])**2)
    return {"towns": towns, "points": points}


def _generate_towns(num):
    towns = {}
    for i in range(0, num):
        towns[i] = {j: randint(0, 99) for j in range(0, num) if j != i}
    return towns


def _plot(route, points, title):
    out_points = []
    for stop in route:
        out_points += [points[stop]]
    out_points += [points[route[0]]]
    d = Gnuplot.Data(out_points,
                     title=title,
                     with_='lines')
    return d


class BruteSolution:
    def __init__(self, towns):
        self.towns = towns
        self.visited = {town: False for town in self.towns}

    def solve(self):
        return min((self._recursive(town, town) for town in self.towns),
                   key=lambda item: item[1])

    def _recursive(self, current, start):
        self.visited[current] = True

        if all(v is True for v in self.visited.values()):
            self.visited[current] = False
            return [current], self.towns[current][start]

        unvisited = [t for t in self.towns if self.visited[t] is False]
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

    def solve(self, start=0):
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


def _graph_compare(euclidean_towns):
    g = Gnuplot.Gnuplot(debug=1)

    print("Punkty: " + str(euclidean_towns["points"]))
    town_map = Gnuplot.Data([(x, y, idx) for (idx, (x, y))
                            in enumerate(euclidean_towns["points"])],
                            with_='labels')
    bs1 = BruteSolution(euclidean_towns["towns"])
    route, cost = bs1.solve()
    bs_data = _plot(route, euclidean_towns["points"], "brute solution")
    print("BruteSolution\nKoszt:" + str(cost) + "\n" + str(route))

    nn1 = NearestNeighbor(euclidean_towns["towns"])
    route, cost = nn1.solve()
    nn_data = _plot(route, euclidean_towns["points"], "nearest neighbor")
    print("NearestNeighborSolution\nKoszt:" + str(cost) + "\n" + str(route))

    g.plot(bs_data, nn_data, town_map)
    raw_input("--- Nacisnij enter ---")


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
        _graph_compare(self.euc1)
        _graph_compare(self.euc2)
        _graph_compare(self.euc3)

    def tearDown(self): pass


if __name__ == "__main__":
    unittest.main()
