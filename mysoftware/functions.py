def square(x):
    return x*x

def coulomb(x):
    if x != 0:
        return 1/abs(x)
    else:
        raise Exception("Attempt to evaluate potential at zero")
    
def coulomb2(x):
    assert type(x) in [float,int], "Invalid argument"
    try:
        return 1/abs(x)
    except ZeroDivisionError:
        exit("Attempt to evaluate potential at zero")

def CentralDifference(f,x,h):
    return ((f(x+h) - f(x-h))/(2*h)

for i in range(2,8):
        h = 10**(-i)
        print(h,abs(CentralDifference(np.sin,0.0,h)-1.0))
