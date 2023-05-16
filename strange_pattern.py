import numpy as np

# implement the function strange pattern

def strange_pattern(n):
    # delete the NotImplementedError when you write your function.
    arr = np.zeros(n, dtype='bool')
    
    arr[::3, ::3] = True
    arr[1::3, 2::3] = True
    arr[2::3, 1::3] = True

    return arr


if __name__ == "__main__":
    # use this for your own testing!

    pass
