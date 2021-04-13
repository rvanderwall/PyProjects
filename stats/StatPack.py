class StatPack:
    def __init__(self, name):
        self.name = name
        self.min = 9999999
        self.max = 0
        self.tot = 0
        self.count = 0
        self.histo = {}

    def add_val(self, new_val):
        if new_val in self.histo:
            self.histo[new_val] += 1
        else:
            self.histo[new_val] = 1

        self.tot += new_val
        self.count += 1
        if new_val < self.min:
            self.min = new_val
        if new_val > self.max:
            self.max = new_val

    def show_stats(self):
        ave = self.tot / self.count
        print(f"{self.name}:  Ave = {ave}")
        print(f"    Min: {self.min}  Max:{self.max}")
        print(self.histo)

    def show_histo(self):
        import numpy as np
        import matplotlib.pyplot as plt

        pos = np.arange(len(self.histo.keys()))
        width = 1.0  # gives histogram aspect to the bar diagram

        ax = plt.axes()
        ax.set_xticks(pos + (width / 2))
        ax.set_xticklabels(self.histo.keys())
        plt.bar(list(self.histo.keys()), self.histo.values(), color='g')
        plt.show()