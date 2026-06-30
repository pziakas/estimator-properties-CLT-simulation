import matplotlib.pyplot as plt
import numpy as np


def mean_estim(arr: np.ndarray) -> float:
    
    """
    Calculates the sample mean estimator.

    Parameters
    ----------
    arr: np.ndarray
        The sample values array

    Returns
    -------
    float
        Sample mean estimator
    """

    if len(arr) == 0:
        raise ZeroDivisionError("Your sample has zero size! Check your array definitions!")
    
    return np.mean(arr)

def variance_estim(arr: np.ndarray, bias: bool) -> float:

    """
    Calculates the sample variance estimator for the biased and unbiased case.

    Parameters
    ----------
    arr: np.ndarray
        The sample values array
    
    bias: bool
        A boolean associated to the bias 

    Returns
    -------
    float
        Variance estimator based on bias
    """

    if len(arr) == 0:
        raise ZeroDivisionError("Your sample has zero size! Check your array definitions!")

    mean = np.mean(arr)
    
    if (not bias) and len(arr) == 1:
        raise ZeroDivisionError("You are going to divide with zero! Check your array definitions!")

    elem_sum = np.sum((arr - mean)**2)

    return elem_sum/(len(arr)) if bias else elem_sum/(len(arr)-1)

def get_rand(arr: np.ndarray, sample_size: int) -> np.ndarray:

    """
    Collects a random sample of defined size from an already defined sample.

    Parameters
    ----------
    arr: np.ndarray
        The sample values array
    
    sample_size: int
        The size of the drawn sample

    Returns
    -------
    np.ndarray
        Drawn sample of defined size
    """

    if sample_size <= 0:
        raise ValueError("The option you inserted for the sample size is invalid!")

    sample = np.random.choice(arr,size = sample_size)

    return sample

def print_mean_std(arr: np.ndarray) -> None:

    """
    Print the mean value and the standard deviation of the sample.

    Parameters
    ----------
    arr: np.ndarray
        The sample values array
    """

    print(f"The mean value of the distribution is: {np.mean(arr)}")
    print(f"The standard deviation of the distribution is: {np.std(arr)}")

def plot(arr: np.ndarray, xtitle: str, title: str, nbins: int) -> None:

    """
    Plots the distribution of the sample.

    Parameters
    ----------
    arr: np.ndarray
        The sample values array
    
    xtitle: str
        The X axis title
    
    title: str
        The figure title
    
    nbins: int
        The number of bins
    """

    if nbins <= 0:
        raise ValueError("The number of bins you have inserted is invalid!")
    

    _,ax = plt.subplots(figsize=(10,6))
    
    ax.hist(arr,nbins,histtype='step',color="darkred",linewidth=2,label="Distribution")
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlabel(xtitle)
    ax.set_ylabel("Counts")
    ax.set_title(title)
    
    plt.tight_layout()
    plt.show()


def get_distr(arr: np.ndarray, sample_size: int, estim: str, n_iter: int) -> np.ndarray:

    """
    Collects a number of random samples of defined size from an already defined sample and
    calculates the value of a given estimator for each one.

    Parameters
    ----------
    arr: np.ndarray
        The sample values array
    
    sample_size: int
        The size of the drawn sample

    est: str
        The estimator that will be calulated
    
    n_iter: int
        Number of random samples to be drawn
    
    Returns
    -------
    np.ndarray
        The array with the estimator values
    """

    values = []

    if sample_size <= 0:
        raise ValueError("The option you inserted for the sample size is invalid!")

    if n_iter <= 0:
        raise ValueError("The number of iterations you have inserted is invalid!")

    print(f"Requested a sample of {sample_size} numbers!")
    
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

    return np.array(values)

def get_full_plot(arr: np.ndarray, sample_size: int, estim: str, xtitle: str, title: str, nbins: int, n_iter: int) -> None:

    """
    Plots the distribution of a given estimaror using randomly drawn samples of defined size 
    from an already defined sample.

    Parameters
    ----------
    arr: np.ndarray
        The sample values array

    sample_size: int
        The size of the randomly drawn sample

    estim: str
        The estimator that will be plotted
    
    xtitle: str
        The X axis title
    
    title: str
        The figure title
    
    nbins: int
        The number of bins
    
    n_iter: int
        The number of random samples that will be drawn
    """

    values = get_distr(arr,sample_size,estim,n_iter)

    plot(values,xtitle,title,nbins)

    print_mean_std(values)
    