import csv
import random
import os
from ast import literal_eval


def load_csv_file(file_path):
    with open(file_path) as file:
        reader = csv.reader(file)
        data = list(reader)
    return data


def Show(data, show_type='top', lines=5, separator=' | '):
    if lines > len(data):
        print("Недостаточно строк в файле")
        lines = len(data)

    if show_type == 'top':
        data_to_show = data[:lines]
    elif show_type == "bottom":
        data_to_show = data[lines:]
    elif show_type == 'random':
        data_to_show = random.sample(data, lines)
    else:
        print("ERROR of show_type")
        exit()

    for row in data_to_show:
        print(separator.join(row))


def Info(data):
    headers = data[0]
    data = data[1:]

    num_rows = len(data)
    num_columns = len(headers)

    print(f"Number of rows x columns: {num_rows}x{num_columns}")

    for i, header in enumerate(headers):
        col_data = [row[i] for row in data]
        num_filled = 0

        for value in col_data:
            if value:
                num_filled += 1

        not_empty_row = 0
        while not col_data[not_empty_row]:
            not_empty_row += 1
        try:
            data_type = type(literal_eval(col_data[not_empty_row])).__name__
        except:
            data_type = type(col_data[not_empty_row]).__name__

        print(f"{header} {num_filled} {data_type}")


def DelNaN(data):
    data = [row for row in data if all(row)]
    return data


def MakeDS(data):
    random.shuffle(data)
    split_index = int(len(data) * 0.7)

    learning_data = data[:split_index]
    testing_data = data[split_index:]

    os.makedirs("workdata/Learning", exist_ok=True)
    os.makedirs("workdata/Testing", exist_ok=True)

    with open("workdata/Learning/train.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(learning_data)

    with open("workdata/Testing/test.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(testing_data)


file_data = load_csv_file("Titanic.csv")

file_data = DelNaN(file_data)
Show(file_data, lines=30)
Info(file_data)
MakeDS(file_data)
