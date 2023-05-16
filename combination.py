import numpy as np 

# implement your function to combine two numpy arrays 

def combination(a1, a2, axis = 0):
    # delete the NotImplementedError when you write your function.
    a1 = a1.squeeze()
    a2 = a2.squeeze()
    combine = True
    a1_shape = a1.shape
    a2_shape = a2.shape

    if len(a1_shape) == len(a2_shape):
        for i in range(len(a2_shape)):
            if i != axis and a1_shape[i] != a2_shape[i]:
                combine = False
        if combine == True:
            combined_a = np.concatenate((a1, a2), axis)
            return combined_a
        else:
            raise ValueError("These arrays cannot be combined")
    else:
        raise ValueError("These arrays cannot be combined")


if __name__ == "__main__":
    # use this for your own testing!

    pass
