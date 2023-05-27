import math


class TinyStatistician:
    def mean(self, x):
        if not isinstance(x, list) or not x:
            return None
        return sum(x) / len(x)

    def median(self, x: list):
        if not isinstance(x, list) or not x:
            return None
        return sorted(x)[len(x) // 2]


    def quartiles(self, x):
        if not isinstance(x, list) or not x:
            return None
        return [sorted(x)[len(x) // 4],sorted(x)[len(x) *3 // 4]]

    def var(self, x):
        if not isinstance(x, list) or not x:
            return None
        return sum(map(lambda n: pow(n - self.mean(x), 2), x)) / len(x)

    def std(self, x):
        if not isinstance(x, list) or not x:
            return None
        return math.sqrt(self.var(x))
