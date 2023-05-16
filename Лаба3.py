import csv

def read_csv_file(file_name):
    #Чтение данных из CSV-файла
    with open(file_name, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        data = []
        for row in reader:
            data.append(row)
        return data

def write_csv_file(file_name, data):
    #Запись данных в CSV-файл
    with open(file_name, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def sort_data_by_field(data, field_name):
   # Сортировка данных по указанному полю
    sorted_data = sorted(data, key=lambda x :x[field_name])
    return sorted_data

def filter_data_by_criteria(data, field_name, criteria_value):
    #Фильтрация данных по заданному критерию
    filtered_data = [row for row in data if int(row[field_name]) > criteria_value]
    return filtered_data

def count_files_in_directory(directory_path):
    #Подсчет количества файлов в директории
    import os
    count = len([name for name in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, name))])
    return count

# Чтение данных из файла
data = read_csv_file('data.csv')

# Сортировка данных по строковому полю
sorted_data_by_name = sort_data_by_field(data, 'ФИО')
print('Данные, отсортированные по ФИО')
for row in sorted_data_by_name:
    print(row)

# Сортировка данных по числовому полю
sorted_data_by_group = sort_data_by_field(data, 'группа')
print('Данные, отсортированные по группе')
for row in sorted_data_by_group:
    print(row)

# Фильтрация данных по критерию
criteria = 3
filtered_data_by_age = filter_data_by_criteria(data, '№', criteria)
print(f'Данные, у которых номер больше {criteria}')
for row in filtered_data_by_age:
    print(row)

# Подсчет количества файлов в директории
directory_path = 'my_folder'
file_count = count_files_in_directory(directory_path)
print(f'Количество файлов в директории {directory_path} {file_count}')

def add_new_data(data):
    #Добавление новых данных
    new_data = {}
    for key in data[0].keys():
        new_data[key] = input(f'Введите {key} ')
    data.append(new_data)
    return data

# Чтение данных из файла
data = read_csv_file('data.csv')

# Добавление новых данных
data = add_new_data(data)

# Сохранение данных в файл
write_csv_file('data.csv', data)