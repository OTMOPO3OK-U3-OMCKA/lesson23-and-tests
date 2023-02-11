# У вас есть список улиц streets. 
# Нужно написать функцию get_tuples, 
# которая вернет список пар (<название улицы>, <индекс в исходном массиве>), 
# индекс должен начинаться с единицы. 
# В качестве аргумента функция принимает список улиц - список 
# строк, в результате должна вывести список кортежей. 


streets = ['ленина', 'советская', 'краснооктябрьская', 'первомайская']


def get_tuples(input_arr):
    # TODO напишите Ваш код здесь
    return [(y, x) for x, y in enumerate(input_arr, 1)]


if __name__ == "__main__":
    print(get_tuples(streets))
