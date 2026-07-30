"""Nearest-rank percentiles over collected samples. Standard library only."""


class Samples:
    def __init__(self):
        self._xs = []

    def add(self, x):
        self._xs.append(float(x))

    def percentile(self, p):
        if not self._xs:
            return 0.0
        xs = sorted(self._xs)
        k = max(0, min(len(xs) - 1, round(p / 100 * (len(xs) - 1))))
        return xs[k]
