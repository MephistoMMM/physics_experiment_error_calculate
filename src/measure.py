"""
This file to calculate the direct measure!
This file to calculate the indirect measure!
@author mpsss
@email mephistommm@gmail.com
"""
from src.calculate_lib import float_err_zero
from src.input_lib import input_a_list
from src.input_lib import input_lists
from src.input_lib import read_file_list
from src.show_result import show_result_direct, show_result_indirect
from src.calculate_lib import average_and_u, average_and_u_for_indirect
import math, sys
from os import path

def direct(arguments):

    if arguments['--f-d']:
        source = read_file_list(path.abspath(arguments['--f-d']))
        error = source[-1][0]
        source = source[0]
    else:
        error = float_err_zero(arguments['-e']) if arguments['-e'] else 0
        source = input_a_list()

    print("source: {}\t\n error: {}".format(str(source), error))
    show_result_direct(*average_and_u(source, error))


def indirect(arguments):
    
    if arguments['--f-d']:
        sources = read_file_list(path.abspath(arguments['--f-d']))
    else:
        sources = input_lists()

    errors = sources[-1]
    sources.pop(-1)
    print("source: {}\t\n error: {}".format(
        '\n\t'.join([str(x) for x in sources]), errors))

    if(len(sources) != len(errors)):
        print("lack data group member!")
        sys.exit(1)

    results = []
    for source, error in zip(sources, errors):
        results.append(average_and_u(source, error))

    context = user_defined_func(arguments['<functions>'])
    show_result_indirect(results, *average_and_u_for_indirect(results, context))


def user_defined_func(func_path):
    context = {}
    context['math'] = math
    
    try:
        with open(path.abspath(func_path), 'r', encoding='utf8') as f:
            exec(f.read(), context)

        return context
    except FileNotFoundError as err:
        print(err)
        sys.exit(1)
