import csv

print("Hello")

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
    counts = {}
    count = 0
    with open('ibm.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        for row in reader:
            value = float(row[6])
            count += 1
            digit = first_digit(value)
            if digit in counts:
                counts[digit] += 1
            else:
                counts[digit] = 1

    print(count)
    print(counts)
    for digit in range(1, 10):
        percent = 100.0 * counts[digit] / count
        print(f"{digit}:  {percent}%")

process()


