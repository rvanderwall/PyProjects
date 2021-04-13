from benford import Benford
from covid import CovidData

b = Benford()
b.process_csv('ibm.csv', 6)
b.show_results()

b = Benford()
c = CovidData()
data = c.read_csv()
b.process_data(data)
b.show_results()

