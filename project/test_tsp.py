#!/usr/bin/python
import tsp
import unittest

class TestPoint(unittest.TestCase):

    def setUp(self):
        self.t1 = {"Krakow": {1: 10}, 1: {"Krakow": 15}}
        self.t2 = {0: {1: 1, 2: 5}, 1: {0: 1, 2: 2}, 2: {0: 1000, 1: 10}}
        self.wrong1 = {0: {0: 5, 1: 10}, 1: {0: 7, 1: 20}}
        self.wrong2 = {0: {1: -1}, 1: {0: 1}}
        self.gen1 = tsp.generate_towns(5)
        self.gen2 = tsp.generate_towns(6)
        self.gen3 = tsp.generate_towns(7)
        self.gen4 = tsp.generate_towns(30)
        self.gen5 = tsp.generate_towns(50)
        self.euc1 = tsp.generate_euclidean_towns(4)
        self.euc2 = tsp.generate_euclidean_towns(6)
        self.euc3 = tsp.generate_euclidean_towns(8)

        self.euc4 = {}
        self.euc4["points"] = [(100, 100), (300, 300), (200, 150), (400, 100)]
        self.euc4["towns"] = tsp.calculate_distance(self.euc4["points"])

        self.euc5 = {}
        self.euc5["points"] = [(100, 100), (200, 150), (250, 320),
                               (322, 435), (455, 255)]
        self.euc5["towns"] = tsp.calculate_distance(self.euc5["points"])

    def test_validation(self):
        self.assertTrue(tsp.validate_towns(self.t1))
        self.assertTrue(tsp.validate_towns(self.t2))
        self.assertFalse(tsp.validate_towns(self.wrong1))
        self.assertFalse(tsp.validate_towns(self.wrong2))

    def test_generation(self):
        self.assertTrue(tsp.validate_towns(self.gen1))
        self.assertTrue(tsp.validate_towns(self.gen2))
        self.assertTrue(tsp.validate_towns(self.gen3))
        self.assertTrue(tsp.validate_towns(self.gen4))
        self.assertTrue(tsp.validate_towns(self.gen5))
        self.assertTrue(tsp.validate_towns(self.euc1["towns"]))

    def test_brute_precoded(self):
        # Pre-coded towns
        bs1 = tsp.BruteSolution(self.t1)
        nn1 = tsp.NearestNeighbor(self.t1)
        self.assertEqual(bs1.solve(), nn1.solve(1))

        bs2 = tsp.BruteSolution(self.t2)
        nn2 = tsp.NearestNeighbor(self.t2)
        self.assertLessEqual(bs2.solve()[1], nn2.solve()[1])

    def test_brute_gen(self):
        # Brute should never output worse solution than nearest neighbor
        bs1 = tsp.BruteSolution(self.gen1)
        nn1 = tsp.NearestNeighbor(self.gen1)
        self.assertLessEqual(bs1.solve()[1], nn1.solve()[1])

        bs2 = tsp.BruteSolution(self.gen2)
        nn2 = tsp.NearestNeighbor(self.gen2)
        self.assertLessEqual(bs2.solve()[1], nn2.solve()[1])

        bs3 = tsp.BruteSolution(self.gen3)
        nn3 = tsp.NearestNeighbor(self.gen3)
        self.assertLessEqual(bs3.solve()[1], nn3.solve()[1])

    def test_euclidean(self):
        tsp.graph_compare(self.euc1["towns"], self.euc1["points"])
        tsp.graph_compare(self.euc2["towns"], self.euc2["points"])
        tsp.graph_compare(self.euc3["towns"], self.euc3["points"])
        tsp.graph_compare(self.euc4["towns"], self.euc4["points"])
        tsp.graph_compare(self.euc5["towns"], self.euc5["points"])

    def tearDown(self): pass


if __name__ == "__main__":
    unittest.main()
