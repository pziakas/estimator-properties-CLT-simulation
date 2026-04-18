import matplotlib.pyplot as plt
import numpy as np


def mean_estim(arr: np.ndarray) -> float:
    
    """
    This function accepts as an argument a Numpy array.

    It calculates the sample mean and returns its value.
    """

    if len(arr) == 0:
        raise ZeroDivisionError("Your sample has zero size! Check your array definitions!")
    
    elem_sum = np.sum(arr)
    
    return elem_sum/len(arr)

def variance_estim(arr: np.ndarray, bias: bool) -> float:

    """
    This function accepts as arguments a Numpy array and a boolean to choose the variance formula.

    It calculates the sample variance depending on the boolean inserted and returns its value.
    """

    if len(arr) == 0:
        raise ZeroDivisionError("Your sample has zero size! Check your array definitions!")

    mean = mean_estim(arr)
    
    if (not bias) and len(arr) == 1:
        raise ZeroDivisionError("You are going to divide with zero! Check your array definitions!")

    elem_sum = np.sum((arr - mean)**2)

    return elem_sum/(len(arr)) if bias else elem_sum/(len(arr)-1)

def get_rand(arr: np.ndarray, sample_size: int) -> np.ndarray:

    """
    This function accepts as an arguments a Numpy array and an interger for the sample size.

    It collects sample_size random numbers from the array and returns a new Numpy array that 
    contains them.
    """

    if sample_size <= 0:
        raise ValueError("The option you inserted for the sample size is invalid!")

    sample = np.random.choice(arr,size = sample_size)

    return sample

def plot(arr: np.ndarray, xtitle: str, title: str, nbins: int) -> None:

    """
    This function accepts as an arguments a Numpy array, an integer for the number of bins
    and two strings for the title and the X axis title.

    It plots the histogram according to the Numpy array that is inserted. It also prints the
    mean value and the standard deviation of the distribution.
    """

    if nbins <= 0:
        raise ValueError("The number of bins you have inserted is invalid!")
    
    plt.hist(arr,nbins,histtype='step')
    plt.xlabel(xtitle)
    plt.ylabel("Counts")
    plt.title(title)
    plt.show()

    print(f"The mean value of the distribution is: {np.mean(arr)}")
    print(f"The standard deviation of the distribution is: {np.std(arr)}")


def get_distr(arr: np.ndarray, sample_size: int, estim: str, n_iter: int) -> np.ndarray:

    """
    This function accepts as an arguments a Numpy array, an integer for the sample size and 
    and the number of iterations and one string for the name of the estimator.

    It gets n_iter samples of sample_size and calculates the value of the designated estimator
    for each sample. It returns the values of the estimaor as a Numpy array.
    """

    values = []

    print(f"Requested a sample of {sample_size} numbers!")

    if sample_size <= 0:
        raise ValueError("The option you inserted for the sample size is invalid!")

    if n_iter <= 0:
        raise ValueError("The number of iterations you have inserted is invalid!")
    
    print(f"Requested {n_iter} iterations!")

    str_to_func = {
        "mean": mean_estim,
        "var": lambda sample: variance_estim(sample,True),
        "star_var": lambda sample: variance_estim(sample,False)
    } 

    if estim not in str_to_func:
        raise ValueError(f"The estimator you have chosen is invalid!")

    for i in range(n_iter):
        sample = get_rand(arr,sample_size)
        val = str_to_func[estim](sample)
        values.append(val)
    
    estim_val = np.array(values)

    return estim_val

def get_full_plot(arr: np.ndarray, sample_size: int, estim: str, xtitle: str, title: str, nbins: int, n_iter: int) -> None:

    """
    This function accepts assembles all the previously defined functions together.

    It plots the distribution of the estimator, using n_iter samples of sample_size.
    """

    values = get_distr(arr,sample_size,estim,n_iter)

    plot(values,xtitle,title,nbins)
    