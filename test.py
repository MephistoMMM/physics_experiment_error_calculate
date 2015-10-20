


def f_x(u,x,y,z,a):
    return (y+z+a)*u
def f_y(u,x,y,z,a):
    return (x+z+a)*u
def f_z(u,x,y,z,a):
    return (y+x+a)*u
def f_a(u,x,y,z,a):
    return (y+z+x)*u
def FUNCTIONS(x, y, z, a):
    print(math.sqrt(x+y+z+a))
    return x+y+z+a

DIFFERENTIALS = (f_x, f_y, f_z, f_a)
