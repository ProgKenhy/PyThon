# Vers. 1.0 (without csv library)
import json
import sys


def json_to_csv(input_json):
    with open(input_json, 'r') as input_json:
        data = json.load(input_json)
    root_key = list(data.keys())[0]  # Получаем название корневой записи JSON
    output_csv_name = root_key + '.csv'
    with open(output_csv_name, 'w') as output_csv:
        inner_keys = ''
        for key in data[root_key][0]:
            inner_keys += str(key)
            inner_keys += ','
        inner_keys = inner_keys[:-1]
        output_csv.write(inner_keys+'\n')
        result_values = ''
        for item in data[root_key]:
            for val in item.values():
                result_values += str(val)
                result_values += ','
            result_values = result_values[:-1]
            result_values += '\n'
        output_csv.write(result_values)
    return output_csv_name


if __name__ == '__main__':
    if len(sys.argv) == 2:
        json_file = sys.argv[1]

    else:
        print("Необходимо указать имя JSON файла (включая расширение):")
        # json_file = 'Sample-JSON-file-with-multiple-records.json'
        # json_file = 'Sample-employee-JSON-data.json'
        json_file = input()

    name_of_csv_file = json_to_csv(json_file)
    print(f"Файл {json_file} успешно преобразован в {name_of_csv_file}")

# # Vers. 2.0
# import json
# import csv
# import sys
#
#
# def json_to_csv(json_file):
#     with open(json_file, 'r') as file:
#         data = json.load(file)
#     root_key = list(data.keys())[0]  # Получаем название корневой записи JSON
#     output_file = root_key + '.csv'
#
#     with open(output_file, 'w', newline='') as file:
#         writer = csv.writer(file)
#
#         # Записываем заголовок CSV файла из ключей первого элемента в корневой записи
#         writer.writerow(data[root_key][0].keys())
#
#         for item in data[root_key]:
#             writer.writerow(item.values())
#
#
# if __name__ == '__main__':
#     if len(sys.argv) == 2:
#         json_file = sys.argv[1]
#
#     else:
#         print("Необходимо указать имя JSON файла (включая расширение):")
#         # json_file = 'Sample-JSON-file-with-multiple-records.json'
#         # json_file = 'Sample-employee-JSON-data.json'
#         json_file = input()
#
#     json_to_csv(json_file)
#     print("JSON файл успешно преобразован в CSV")
