import binascii # Библиотека для декодирования
import codecs # Кодеки
import numpy as np # Скрипт для работы с матрицами

class Interl(object):

    def NormalInterl(self, message):
        string = message
        lenght = 10
        count = 0
        
        binary_string = bin(int.from_bytes(string.encode(), 'big')) # ПРЕДСТАВЛЯЕМ СТРОКУ В БИТАМИ

        while len(str(binary_string[2:len(str(binary_string))])) % lenght != 0: # Пока строку нельзя поделить на пакеты
            binary_string = str(binary_string) + '0' # Добиваем нулями
            count += 1 # Сколько нулей добавили
        # Узнаем количество строк путем деления на пакеты
        string_split_column = str('\n'.join(str(binary_string)[i:i+lenght] for i in range(2, len(str(binary_string)), lenght))).split('\n', -1)
        # Делаем из потока бит вектор 
        string_split = str(' '.join(binary_string[2:len(binary_string)])).split(' ', -1)
        # Делаем из вектора двумерный массив с 10 столбцами и N строками
        string_matrix = np.array([string_split]).reshape(len(string_split_column), 10)
        # Применяем перестановку [9,8,7,6,5,4,3,2,1,0] - т.е. "отзеркаливаем"
        string_matrix = np.flip(string_matrix, axis=1)
        # Транспонируем матрицу для считыванния
        string_transpon_matrix = string_matrix.T
        # Считываем и переделываем в строку
        inter_string = '0b' + ''.join(str(item) for interlist in string_transpon_matrix for item in interlist)
        # Возвращаем два значения кортежем - исходное сообщение и кол-во нулей, которое нужно будет удалить при деинтерливере
        return(inter_string, count)
    
    def NormalDeinterl(self, message, count):
        string = message
        lenght = 10
        # Узнаем количество строк путем деления на пакеты
        string_deint_split_column = str('\n'.join(str(string)[i:i+lenght] for i in range(2, len(str(string)), lenght))).split('\n', -1)
        # Делаем из потока бит вектор
        string_deint_split = str(' '.join(string[2:len(string)])).split(' ', -1)
        # Делаем из вектора двумерный массив с 10 строками и N строками
        string_deint_split = np.array([string_deint_split]).reshape(10, len(string_deint_split_column))
        # Транспонируем матрицу для считыванния и сразу же зеркалим([0,1,2,3,4,5,6,7,8,9])
        string_deint_trans = np.flip(string_deint_split.T, axis=1)
        # Считываем и переделываем в строку
        deinter_string = '0b' + ''.join(str(item) for interlist in string_deint_trans for item in interlist)
        # Удаляем нули
        deinter_result_string = deinter_string[0:(len(deinter_string)-count)]
        # Возвращаем
        return(deinter_result_string)
