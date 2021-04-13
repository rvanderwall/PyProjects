import random
from DataSrc import DataSource
from StatPack import StatPack

# https://retirementplans.vanguard.com/VGApp/pe/pubeducation/calculators/RetirementNestEggCalc.jsf

#
# In this simulation, we demonstrate that the average profit is not margin * average demand
# since we have a capacity limit.  We can always meet demand when it it less than average, but
# cannot meet demand when it exceeds capacity, this caps our profits and reduces the average.


class Factory:
    def __init__(self):
        self.AVE = 100_000  # Average Demand
        self.RANGE = 50_000  # 50-150
        self.CAPACITY = 130_000  # Capacity of facility
        self.PROFIT_MARGIN = 0.1  #
        self.sp_demand = StatPack('demand')
        self.sp_profit = StatPack('profit')

    def cycle(self):
        d = self._sample_demand()
        p = self._profit(d)
        self.sp_demand.add_val(d)
        self.sp_profit.add_val(p)
        return

    def show_results(self):
        self.sp_demand.show_stats()
        self.sp_profit.show_stats()

    def _sample_demand(self):
        r = random.randint(self.AVE - self.RANGE, self.AVE + self.RANGE)
        return r

    def _profit(self, demand):
        if demand > self.CAPACITY:
            demand = self.CAPACITY
        p = demand * self.PROFIT_MARGIN
        return p


def convert_stock_row_data(row):
    val = float(row[1].replace('%','')) / 100.0
    return val


class Stock:
    def __init__(self):
        self.START = 1_500_000
        self.withdraw = 150_000

        self.sp_years = StatPack('Years')
        self.sp_growth = StatPack('Growth')
        self.history = DataSource.get_csv('stock.csv','\t',convert_stock_row_data)
        self.GROWTH = 0.07      # Average 5%/yr
        self.VARIANCE = 0.10    # varies from -0.05 .. 0.15

    def cycle(self):
        yrs = self._run_until_out_of_money()
        print(f"Money will last {yrs} years")
        self.sp_years.add_val(yrs)

    def show_results(self):
        print(f"Withdrawing {self.withdraw:.2f} per year:")
        self.sp_growth.show_stats()
        self.sp_years.show_stats()
        self.sp_years.show_histo()

    def _run_until_out_of_money(self):
        current = self.START
        years = 0
        while current > 0 and years < 100:
            years += 1
            rate = self._cur_growth()
            self.sp_growth.add_val(rate)
            current = current + current * rate
            current = current - self.withdraw
            # print(f"Current={current:.2f}, rate={rate:.4f}")
        return years

    def _cur_growth(self):
        # r = random.uniform(self.GROWTH - self.VARIANCE, self.GROWTH + self.VARIANCE)
        r = random.choice(self.history)
        return r


def run(sim):
    N = 100  # Number of simulations to run
    for n in range(N):
        sim.cycle()
    sim.show_results()


print("Monte Carlo simulation")
if __name__ == "__main__":
    # sim = Factory()
    sim = Stock()
    run(sim)
