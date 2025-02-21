import os

folder_path = './'

files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]

file_contents = []
for file_name in files:
    with open(os.path.join(folder_path, file_name), 'r') as file:
        content = file.read().strip()
        num_lines = len(content.split('\n'))
        file_contents.append((file_name, num_lines, content))

sorted_files = sorted(file_contents, key=lambda x: x[1])

with open('result.txt', 'w') as result_file:
    for file_name, num_lines, content in sorted_files:
        result_file.write(f'Имя файла: {file_name}\n')
        result_file.write(f'Количество строк: {num_lines}\n')
        result_file.write(content + '\n\n')

print("Файлы успешно объединены!")