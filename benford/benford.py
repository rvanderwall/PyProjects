import csv
import math
import plotly.graph_objects as go
import numpy as np


class Benford:
    def __init__(self):
        self.count = 0
        self.count_map = {}

    def show_results(self):
        print(self.count)
        print(self.count_map)
        Ps = []
        actuals = []
        for digit in range(1, 10):
            P = 100.0 * math.log((digit + 1.0) / digit, 10)
            percent = 100.0 * self.count_map[digit] / self.count
            Ps.append(P)
            actuals.append(percent)
            print(f"{digit}:  {percent:.1f}%   --   {P:.1f}%")

        self.plot(Ps, actuals)
        return Ps, actuals

    def _first_digit(self, num):
        if num == 0:
            return 0
        if num < 1.0:
            return self._first_digit(num * 10)
        if num >= 10.0:
            return self._first_digit(num / 10.0)

        dig = int(num)
        return dig

    def process_csv(self, fname, row_index):
        with open(fname, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader)
            for row in reader:
                self._process_val(float(row[row_index]))

    def process_data(self, data):
        for row in data:
            value = row.deaths_new
            self._process_val(value)

    def _process_val(self, value):
        self.count += 1
        digit = self._first_digit(value)
        if digit in self.count_map:
            self.count_map[digit] += 1
        else:
            self.count_map[digit] = 1

    def plot(self, expected, actual):
        assert len(expected) == len(actual)
        x = np.arange(1, len(expected))
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=expected, name="Expected"))
        fig.add_trace(go.Scatter(x=x, y=actual, name="Actual"))
        fig.show()
