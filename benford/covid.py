import math
import requests
from bs4 import BeautifulSoup
import csv
import plotly.graph_objects as go
import numpy as np


WIKI_URL='https://en.wikipedia.org/wiki'
COVID_DATA_URL=f"{WIKI_URL}/Template:COVID-19_pandemic_data/United_States_medical_cases"


class Row:
    date = ""
    confirmed_new = 0
    confirmed_cum = 0
    deaths_new = 0
    deaths_cum = 0
    recovered_new = 0
    recovered_cum = 0
    active = 0


def get_int_data(data):
    if data is None:
        return 0
    d = data.text.strip()
    if d == "":
        return 0
    else:
        return int(d)

def get_data():
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
        r.confirmed_new = get_int_data(th_cells[offset])
        offset += 1
        r.confirmed_cum = get_int_data(th_cells[offset])
        offset += 1
        r.deaths_new = get_int_data(th_cells[offset])
        offset += 1
        r.deaths_cum = get_int_data(th_cells[offset])
        offset += 1
        r.recovered_new = get_int_data(th_cells[offset])
        offset += 1
        r.recovered_cum = get_int_data(th_cells[offset])
        offset += 1
        r.active = get_int_data(th_cells[offset])
        data_rows.append(r)
        print(f"Row {r.date} added")

    return data_rows


def write_data(data_rows):
    with open('covid.csv', 'w', newline='') as csvfile:
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

def read_data():
    data_rows = []
    with open('covid.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)    # Skip header
        for row in reader:
            r = Row()
            r.date = row[0]
            r.confirmed_new = int(row[1])
            r.confirmed_cum = int(row[2])
            r.deaths_new = int(row[3])
            r.deaths_cum = int(row[4])
            r.recovered_new = int(row[5])
            r.recovered_cum = int(row[6])
            r.active = int(row[7])
            data_rows.append(r)
    return data_rows

def validate_data(data):
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


def first_digit(num):
    if num == 0:
        return 0
    if num < 1.0:
        return first_digit(num * 10)
    if num >= 10.0:
        return first_digit(num / 10.0)

    dig = int(num)
    return dig


def process():
    data = read_data()
    data = data[:-1]    # Drop last row since it is 'today' and we don't have data for it.
    validate_data(data)
    counts_map = {}
    count = 0
    for row in data:
        value = row.deaths_new
        count += 1
        digit = first_digit(value)
        if digit in counts_map:
            counts_map[digit] += 1
        else:
            counts_map[digit] = 1

    print(count)
    print(counts_map)
    Ps = []
    actuals = []
    for digit in range(1, 10):
        P = 100.0 * math.log((digit + 1.0) / digit, 10)
        percent = 100.0 * counts_map[digit] / count
        Ps.append(P)
        actuals.append(percent)
        print(f"{digit}:  {percent:.1f}%   --   {P:.1f}%")

    return Ps, actuals


def plot(expected, actual):
    assert len(expected) == len(actual)
    x = np.arange(1, len(expected))
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=expected, name="Expected"))
    fig.add_trace(go.Scatter(x=x, y=actual, name="Actual"))
    fig.show()


# data = get_data()
# write_data(data)
Ps, counts = process()
plot(Ps, counts)
