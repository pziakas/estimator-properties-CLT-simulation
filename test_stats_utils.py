import stats_utils as stats
import pytest
import numpy as np

# Test cases for testing the mean estimator function 

@pytest.mark.parametrize(
    "arr, expected",
    [
        (np.array([1, 2, 3]), 2.0),
        (np.array([1, 2, 3, 4]), 2.5),
        (np.array([-2, -4, -6]), -4),
        (np.array([0]), 0)
    ]
)

def test_mean_estim(arr: np.ndarray, expected: float) -> None:

    assert stats.mean_estim(arr) == pytest.approx(expected)


def test_mean_estim_empty() -> None:

    arr = np.array([])

    with pytest.raises(ZeroDivisionError):
        stats.mean_estim(arr)


# Test cases for the variance estimator function

@pytest.mark.parametrize(
    "arr, bias, expected",
    [
        (np.array([1, 2, 3]), True, 2 / 3),
        (np.array([1, 2, 3]), False, 1),
        (np.array([-1, -2, -3]), True, 2 / 3),
        (np.array([-1, -2, -3]), False, 1),
        (np.array([5]), True, 0)
    ]
)

def test_variance_estim(arr: np.ndarray, bias: bool, expected: float) -> None:

    assert stats.variance_estim(arr,bias) == pytest.approx(expected)

def test_variance_one_element_unbiased() -> None:

    arr = np.array([5])

    with pytest.raises(ZeroDivisionError):
        stats.variance_estim(arr,False)

@pytest.mark.parametrize("bias", [True,False])

def test_variance_empty(bias: bool) -> None:

    arr = np.array([])

    with pytest.raises(ZeroDivisionError):
        stats.variance_estim(arr,bias)


# Test cases for the get_rand function 

def test_get_rand_size() -> None:

    arr = np.array([1,2,3,4,5])

    result = stats.get_rand(arr,3)

    assert len(result) == 3

def test_get_rand_values_from_array() -> None:

    arr = np.array([1,2,3,4,5])

    result = stats.get_rand(arr, 10)

    assert np.all(np.isin(result, arr))


@pytest.mark.parametrize("size", [0, -1])


def test_get_rand_invalid_size(size: int) -> None:

    arr = np.array([1,2,3,4,5])

    with pytest.raises(ValueError):
        stats.get_rand(arr, size)


# Test cases for get_distr function

def test_get_distr_invalid_estim() -> None:

    arr = np.array([1,2,3,4,5])

    with pytest.raises(ValueError):
        stats.get_distr(arr,4,"rand_est",10)

@pytest.mark.parametrize("estim", ["mean", "var", "star_var"])


def test_get_distr_length(estim: str) -> None:

    arr = np.array([1,2,3,4,5])

    results = stats.get_distr(arr,3,estim,10)

    assert len(results) == 10

@pytest.mark.parametrize("sample_size", [0, -1])
@pytest.mark.parametrize("estim", ["mean", "var", "star_var"])

def test_get_distr_invalid_sample_size(sample_size: int, estim: str) -> None:

    arr = np.array([1,2,3,4,5])

    with pytest.raises(ValueError):
        stats.get_distr(arr,sample_size,estim,10)

@pytest.mark.parametrize("n_iter", [0, -10])
@pytest.mark.parametrize("estim", ["mean", "var", "star_var"])

def test_get_distr_invalid_n_iter(n_iter: int, estim: str) -> None:

    arr = np.array([1,2,3,4,5])

    with pytest.raises(ValueError):
        stats.get_distr(arr,4,estim,n_iter)


# Test cases for plot function

@pytest.mark.parametrize("nbins", [0, -10])

def test_plot_invalid_nbins(nbins: int) -> None:

    arr = np.array([1,2,3,4,5])

    with pytest.raises(ValueError):
        stats.plot(arr,"x_title","title",nbins)