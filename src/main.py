"""
Main file to exculate
@author mpsss
@email mephistommm@gmail.com
"""
from docopt import docopt
from src.measure import direct
from src.measure import indirect


def main():
    """
    Usage: 
      physics-exp [options] direct  
      physics-exp [options] indirect <functions>

    Options:
      -e ERROR        a file define error to calculate[default:0],also can be list,
                      (this parament only used in direct)
      --f-d DFILE     a file define data list for calculate
                      (the last line mast be ERROR)

    Message:
        <functions>     define calculate function and differential, DIFFERENTIALS is a function list
                        FUNCTIONS is a function
        input format    input format and file format need like these:
                                x 12.2 12 23.4 32
                                y 23.3 3  32    6.6
                                e 223 3223 2322 3232
        error line      error line must be the last line in file and in input line
                        if your specify the --f-d , you should use -e
    lovely by mpsss.
    """
    arguments = docopt(main.__doc__, version="α")
    print(arguments)

    if arguments['direct']:
        direct(arguments)
    else:
        indirect(arguments)




