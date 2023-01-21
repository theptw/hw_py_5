def pack(file_orig, file_packed): # сжатие
    data_str = ''
    data = open(file_orig, 'r')
    for line in data:
        data_str += line
    data.close()
    print(data_str)

    final_str = ''
    count = 1
    for i in range(len(data_str) - 1):
        if data_str[i] == data_str[i+1]:
            count += 1
            if i+1 == len(data_str) - 1: #если последнии элементы равны
                final_str += str(count) + data_str[i]
        elif i+1 == len(data_str) - 1:   #если следующий элемент последний и не равен настоящему
            final_str += str(count) + data_str[i] + '1' + data_str[i+1]
        else:
            final_str += str(count) + data_str[i]
            count = 1

    data = open(file_packed, 'w')
    data.write(final_str)
    data.close()

    return final_str
    
def unpack(file_orig, file_packed):
    data_str = ''
    final_str = ''
    data = open(file_packed, 'r')
    for line in data:
        data_str += line
    data.close()
    print(data_str)
    
    for i in range(0,len(data_str),2):
        final_str += int(data_str[i]) * data_str[i+1]

    data = open(file_orig, 'w')
    data.write(final_str)
    data.close()

    return final_str

action = input('Для сжатия данных нажмите Enter, для восстановления любую другую клавишу: ')
if action == '':
    file_path = input('Введите путь файла, из которго необходимо взять данные(сжатие) или нажмите Enter для стандартного значения: ')
    if file_path == '':
        print(pack('hw_py_5\original.txt', 'hw_py_5\packed.txt'))# в packed из original
    else:
        print(pack(file_path, 'hw_py_5\packed.txt'))
else:
    file_path = input('Введите путь файла, из которго необходимо взять данные(восстановление) или нажмите Enter для стандартного значения: ')
    if file_path == '':
        print(unpack('hw_py_5\original.txt', 'hw_py_5\packed.txt'))# в original из packed
    else: 
        print(unpack('hw_py_5\original.txt', file_path))


    

