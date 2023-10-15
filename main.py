
import os
import glob
#Находим пути к файлам
def files_path():
    file_path = f"{os.getcwd()}/"
    files_paths = glob.glob(file_path + '*.txt')
    return files_paths

def reading_and_writing_files():
    # чтение файлов, создание списка длин файлов, названия файлов, содержимого файлов
    files_paths = files_path()
    files =[]
    for file in files_paths:
        name_of_files = file.split('/')[-1]
        with open(file,'r', encoding='utf-8') as f:
            line = f.readlines()
            files.append([len(line), name_of_files, line])
            #Сортировка по длине строк файлов
    files.sort()
    # Запись в новый файл 4.txt объединенных файлов 1,2,3
    with open('4.txt', 'w', encoding='utf-8') as f:
        for line_file in files:
            f.write(f"{line_file[0]}\n{line_file[1]}\n {''.join(line_file[2])}\n")
    return files
print(reading_and_writing_files())


