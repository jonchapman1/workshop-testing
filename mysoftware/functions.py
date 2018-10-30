
def square(x):
    return x*x

def coulomb(x):
    if x != 0:
        return 1/abs(x)
    else:
        raise Exception("Attempt to evaluate potential at zero")
 
def CentralDifference(f,x,h):
    return (f(x+h) - f(x-h))/(2*h)
       
