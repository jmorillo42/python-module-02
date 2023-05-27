import unittest

from src.ex05.TinyStatistician import TinyStatistician


class Ex05TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.tstat = TinyStatistician()
        self.numbers = [1, 42, 300, 10, 59]

    def test_mean(self):
        print('2.05.01: mean')
        print(f'  input: {self.numbers}')
        y = self.tstat.mean(self.numbers)
        print(f'  result = {y}')
        self.assertEqual(y, 82.4)

    def test_median(self):
        print('2.05.02: median')
        print(f'  input: {self.numbers}')
        y = self.tstat.median(self.numbers)
        print(f'  result = {y}')
        self.assertEqual(y, 42.0)

    def test_quartiles(self):
        print('2.05.03: quartiles')
        print(f'  input: {self.numbers}')
        y = self.tstat.quartiles(self.numbers)
        print(f'  result = {y}')
        self.assertEqual(y, [10.0, 59.0])

    def test_variance(self):
        print('2.05.04: variance')
        print(f'  input: {self.numbers}')
        y = self.tstat.var(self.numbers)
        print(f'  result = {y}')
        self.assertEqual(y, 12279.439999999999)

    def test_st(self):
        print('2.05.05: standard deviation')
        print(f'  input: {self.numbers}')
        y = self.tstat.std(self.numbers)
        print(f'  result = {y}')
        self.assertEqual(y, 110.81263465868862)


if __name__ == '__main__':
    unittest.main()
