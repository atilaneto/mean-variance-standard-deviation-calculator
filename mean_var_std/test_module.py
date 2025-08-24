# test_module.py
import unittest
import mean_var_std


class UnitTests(unittest.TestCase):
    def test_calculate(self):
        actual = mean_var_std.calculate([2,6,2,8,4,0,1,5,7])
        expected = {
            'mean': [[3.6666666667, 5.0, 3.0],
                     [3.3333333333, 4.0, 4.3333333333],
                     3.8888888889],
            'variance': [[9.5555555556, 0.6666666667, 8.6666666667],
                         [3.5555555556, 10.6666666667, 6.3333333333],
                         6.987654321],
            'standard deviation': [[3.0912, 0.8165, 2.9439],
                                   [1.8856, 3.2659863237, 2.5166],
                                   2.6434],
            'max': [[8, 6, 7],
                    [6, 8, 7],
                    8],
            'min': [[1, 0, 2],
                    [2, 0, 1],
                    0],
            'sum': [[11, 15, 9],
                    [10, 12, 13],
                    35]
        }

        # Verificações
        for key in expected:
            for i in range(3):
                if isinstance(expected[key][i], list):
                    for j in range(3):
                        self.assertAlmostEqual(actual[key][i][j], expected[key][i][j], places=4,
                                               msg=f"{key} mismatch at position {i},{j}")
                else:
                    self.assertAlmostEqual(actual[key][i], expected[key][i], places=4,
                                           msg=f"{key} mismatch at total value")


if __name__ == "__main__":
    unittest.main()
