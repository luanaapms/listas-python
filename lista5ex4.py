lista_num = []


for number in range(18644, 33088):
    number_string = str(number)
    if number_string.count('2') != 0 and number_string.count('7') == 0:
        lista_num.append(number_string)

print(len(lista_num))