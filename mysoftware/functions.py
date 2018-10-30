
def square(x):
    """
    Takes a number x and squares it.

    Parameters:
    -----------
    x, float or int:
        Number which is to be squared.

    Returns:
    --------
    float:
        Square of x.

    Examples:
    ---------
    >>> square(2)
    4

    >>> square(-1)
    1

    """
    return x*x

def coulomb(x):
    if x != 0:
        return 1/abs(x)
    else:
        raise Exception("Attempt to evaluate potential at zero")
 
def CentralDifference(f,x,h):
    return (f(x+h) - f(x-h))/(2*h)
       
