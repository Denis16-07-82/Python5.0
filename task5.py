# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def encode(data):
    encoding = ''

    if not data:
        return ''
    ei = 0
    while ei < len(data):
        count = 1
        if ei + 1 < len(data):
            while ei + 1 < len(data) and (data[ei] == data[ei + 1]):
                count += 1
                if ei + 2 < len(data) :
                    ei += 1
                else: break
        encoding += str(count) + data[ei]
        ei+= 1

    return encoding


def decode(data = ''):
    decoding = ''
    count = ''
    if not data:
        return ''
    for el in data:
        if el.isdigit():
            count+= el
        else:
            decoding+= int(count) * el
            count = ''
        
    return decoding

    





data = "AAAaAbb"
data1 =(encode(data))
print(encode(data))
print(decode(data1))

