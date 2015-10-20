"""
this file to show_result 
@author mpsss
@mephistommm@gmail.com
"""
R_AVERAGE = 0
R_U = 1
R_E = 2

def show_result_direct(average, u, E):
    print("{:-^40}".format(''))
    print("result:\n" +
          "\taverage: {:>.6f}".format(average) +
          "\tu: {:>.6f}".format(u) +
          "\tE: {:>.6f}%".format(E))
    print("{:-^40}".format(''))



def show_result_indirect(results,average, u, E):

    print("{:-^40}".format(''))
    for i in range(len(results)):
        print("args({}):\t".format(i) +
              "\taverage: {:>.6f}".format(results[i][R_AVERAGE]) +
              "\tu: {:>.6f}".format(results[i][R_U]) +
              "\tE: {:>.6f}%".format(results[i][R_E]))

    print("\nresult:\n" +
          "\taverage: {:>.6f}".format(average) +
          "\tu: {:>.6f}".format(u) +
          "\tE: {:>.6f}%".format(E))
    print("{:-^40}".format(''))
