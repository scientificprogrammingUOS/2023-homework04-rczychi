import numpy as np

# implement the function gaussian_analysis

def gaussian_analysis(loc, scale, lower, upper):
    if isinstance(loc, (int, float)) == True and isinstance(scale, (int, float)) == True and isinstance(lower, (int, float)) == True and isinstance(upper, (int, float)) == True:        
        if lower < upper:
            gauss = np.random.normal(loc, scale, 100)

            up_bound = gauss < upper
            gauss = gauss[up_bound]
            low_bound = gauss > lower
            gauss = gauss[low_bound]
            print(gauss)

            mean = np.mean(gauss)
            std = np.std(gauss)
            x = tuple((mean, std))
            print(f"The mean (first value) and the standard deviation (second value) are: {x}")
            
            return x
        else:
            print("The lower bound must be smaller than the upper bound")
    else:
        print("The values have to be either integers or floats")


if __name__ == "__main__":
    # use this for your own testing!

    pass
