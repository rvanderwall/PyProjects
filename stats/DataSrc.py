import csv


class DataSource:
    def __init__(self):
        pass

    @staticmethod
    def get_csv(file_name, delim, converter):
        rows = []
        with open(file_name) as csvfile:
            reader = csv.reader(csvfile, delimiter=delim, quotechar='"')
            next(reader)    # Skip header
            for row in reader:
                data = converter(row)
                rows.append(data)
        return rows
