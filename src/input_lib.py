"""
this file define function to get data source 

input and read file
"""
from src.calculate_lib import float_err_zero

def input_lists():
    source_lists = []
    print('please a seris of lists of data: \n'
          '(input an \'enter\' to end,and the last line must be error linei)')

    while(True):
        source_list = input('please input a list of data:')
    
        if(len(source_list.strip()) <= 0): 
            break
        else:
            source_lists.append(get_number_from_str(source_list))

    return source_lists



def input_a_list():
    source_str = input('please input a list of data:')
    return get_number_from_str(source_str)


def read_file_list(path):
    """
    file format need like these:
        x 1.32 32.4 32.3 
        Y 3.21 23 32  23 
    """
    with open(path, 'r', encoding='utf8') as f:
        data = f.read()

        source_lines = tuple(
                filter(lambda x: len(x) >0,
                    map(lambda x: x.strip(), data.split('\n'))))

        source_lists = []
        for line in source_lines:
            source_lists.append(get_number_from_str(line))

    return source_lists


def get_number_from_str(source_str):
    source_list = tuple(
            map(lambda x: float_err_zero(x),
                filter(lambda x: len(x) >0,
                    map(lambda x: x.strip(), source_str.split(' ')))))
    return source_list[1:]
