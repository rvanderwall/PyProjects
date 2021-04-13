import requests
from bs4 import BeautifulSoup
import csv


WIKI_URL='https://en.wikipedia.org/wiki'
COVID_DATA_URL=f"{WIKI_URL}/Template:COVID-19_pandemic_data/United_States_medical_cases"


class Row:
    def __init__(self):
        self.date = ""
        self.confirmed_new = 0
        self.confirmed_cum = 0
        self.deaths_new = 0
        self.deaths_cum = 0
        self.recovered_new = 0
        self.recovered_cum = 0
        self.active = 0

    def from_csv_row(self, row):
        self.date = row[0]
        self.confirmed_new = int(row[1])
        self.confirmed_cum = int(row[2])
        self.deaths_new = int(row[3])
        self.deaths_cum = int(row[4])
        self.recovered_new = int(row[5])
        self.recovered_cum = int(row[6])
        self.active = int(row[7])
        return self


class CovidData:
    def __init__(self):
        self.CSV_FILE = 'covid.csv'

    def create_csv(self):
        data = self._get_data()
        self._write_data(data)

    def read_csv(self):
        data_rows = []
        with open(self.CSV_FILE, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader)    # Skip header
            for row in reader:
                r = Row().from_csv_row(row)
                data_rows.append(r)
        data_rows = data_rows[:-1]    # Drop last row since it is 'today' and we don't have data for it.
        self._validate_data(data_rows)
        return data_rows

    def _get_int_data(self, data):
        if data is None:
            return 0
        d = data.text.strip()
        if d == "":
            return 0
        else:
            return int(d)

    def _get_data(self):
        page = requests.get(COVID_DATA_URL)
        soup = BeautifulSoup(page.content, 'html.parser')

        results = soup.find(class_='wikitable')
        table = results.find('tbody')
        rows = table.find_all('tr')

        data_rows = []
        for row in rows:
            td_cells = row.find_all('td')
            th_cells = row.find_all('th')
            if len(th_cells) != 9:
                # Skip header and state label rows
                continue

            row_date = th_cells[1].text.strip()
            if row_date == "Midwest":
                # Skip last rows with summary data
                continue

            r = Row()
            r.date = row_date
            offset = 2
            r.confirmed_new = self._get_int_data(th_cells[offset])
            offset += 1
            r.confirmed_cum = self._get_int_data(th_cells[offset])
            offset += 1
            r.deaths_new = self._get_int_data(th_cells[offset])
            offset += 1
            r.deaths_cum = self._get_int_data(th_cells[offset])
            offset += 1
            r.recovered_new = self._get_int_data(th_cells[offset])
            offset += 1
            r.recovered_cum = self._get_int_data(th_cells[offset])
            offset += 1
            r.active = self._get_int_data(th_cells[offset])
            data_rows.append(r)
            print(f"Row {r.date} added")

        return data_rows

    def _write_data(self, data_rows):
        with open(self.CSV_FILE, 'w', newline='') as csvfile:
            fieldnames = ['date', 'confirmed_new', 'confirmed_cum', 'deaths_new', 'deaths_cum', 'recovered_new', 'recovered_cum', 'active']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for row in data_rows:
                data = {'date': row.date}
                data['confirmed_new'] = row.confirmed_new
                data['confirmed_cum'] = row.confirmed_cum
                data['deaths_new'] = row.deaths_new
                data['deaths_cum'] = row.deaths_cum
                data['recovered_new'] = row.recovered_new
                data['recovered_cum'] = row.recovered_cum
                data['active'] = row.active
                writer.writerow(data)

    def _validate_data(self, data):
        old_confirmed = 0
        old_deaths = 0
        old_recovered = 0

        row_num = 0
        for row in data:
            row_num += 1
            expected_conf_cum = old_confirmed + row.confirmed_new
            if expected_conf_cum != row.confirmed_cum:
                print(f"ERROR: row {row_num} at date {row.date} has wrong confirmed counts")

            expected_death_cum = old_deaths + row.deaths_new
            if expected_death_cum != row.deaths_cum:
                print(f"ERROR: row {row_num} at date {row.date} has wrong deaths counts")

            expected_recovered_cum = old_recovered + row.recovered_new
            if expected_recovered_cum != row.recovered_cum:
                print(f"ERROR: row {row_num} at date {row.date} has wrong deaths counts")

            old_confirmed = expected_conf_cum
            old_deaths = expected_death_cum
            old_recovered = expected_recovered_cum

        print(f"Validated {row_num} rows")
