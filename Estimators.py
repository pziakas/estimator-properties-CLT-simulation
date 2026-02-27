import matplotlib.pyplot as plt
import numpy as np


def mean_estim(arr):
    
    """
    This function accepts as an argument a Numpy array.

    It calculates the sample mean and returns its value.
    """

    if len(arr) == 0:
        raise ZeroDivisionError("Your sample has zero size! Check your array definitions!")
    
    sum = np.sum(arr)
    
    return sum/len(arr)

def variance_estim(arr, mode):

    """
    This function accepts as an arguments a Numpy array and an interger for the mode.

    It calculates the sample variance depnding on the mode inserted and returns its value.
    """

    mean = mean_estim(arr)
    sum = 0.0

    if len(arr) == 0:
        raise ZeroDivisionError("Your sample has zero size! Check your array definitions!")
    
    if mode == 2 and len(arr) == 1:
        raise ZeroDivisionError("You are going to divide with zero! Check your array definitions!")

    for i in range(len(arr)):
        sum += (arr[i] - mean)**2

    mode_to_val = {
        1: sum/(len(arr)),
        2: sum/(len(arr)-1)
    }
    
    if mode not in mode_to_val:
        raise ValueError("The mode you have inserted is invalid!")

    return mode_to_val[mode]

def get_rand(arr,sample_size):

    """
    This function accepts as an arguments a Numpy array and an interger for the sample size.

    It collects random numbers from the array, as many as the inserted sample size and returns
    a new Numpy array that contains them.
    """

    if sample_size <= 0:
        raise ValueError("The option you inserted for the sample size is invalid!")

    sample = np.random.choice(arr,size = sample_size)

    return sample

def plot(arr,xtitle,title,nbins):

    """
    This function accepts as an arguments a Numpy array, an integer for the number of bins
    and two strings for the title and the X axis title.

    It plots the histogram according to the Numpy array that is inserted. It also print the
    mean value and the standard deviation of the histogram.
    """

    if nbins <= 0:
        raise ValueError("The number of bins you have inserted is invalid!")
    
    plt.hist(arr,nbins,histtype='step')
    plt.xlabel(xtitle)
    plt.ylabel("Counts")
    plt.title(title)

    print(f"The mean value of the distribution is: {np.mean(arr)}")
    print(f"The standard deviation of the distribution is: {np.std(arr)}")


def get_distr(arr,sample_size,estim,n_iter):

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
        "var": lambda sample: variance_estim(sample,1),
        "star_var": lambda sample: variance_estim(sample,2)
    } 

    if estim not in str_to_func:
        raise ValueError(f"The estimator you have chosen is invalid!")

    for i in range(n_iter):
        sample = get_rand(arr,sample_size)
        val = str_to_func[estim](sample)
        values.append(val)
    
    estim_val = np.array(values)

    return estim_val

def get_full_plot(arr,sample_size,estim,xtitle,title,nbins,n_iter):

    """
    This function accepts assembles all the previously defined functions together.

    It plots the distribution of the estimator, using n_iter samples of sample_size.
    """

    try:
        values = get_distr(arr,sample_size,estim,n_iter)

        plot(values,xtitle,title,nbins)
    
    except (ValueError,ZeroDivisionError) as e:
        print(f"ERROR: {e}")