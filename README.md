#  Statistical Properties of Estimators & Central Limit Theorem - Monte Carlo Study

## Overview

This project investigates the behavior of common statistical estimators and demonstrates the Central Limit Theorem (CLT) using Monte Carlo simulations. The goal is to validate theoretical properties, explore estimator reliability, and connect these insights to applications in risk modeling and probabilistic forecasting.  The project combines theory, modular Python code, and visualizations in Jupyter notebooks to provide a complete workflow for reproducible analysis.

## Statistical Properties of Estimators

Qualities estimators should demonstrate to be considered as "good estimators" are briefly explained below:

- **Unbiasedness**: The expected value of the estimator equals the true parameter value.

- **Consistency**: The estimator converges in probability to the true parameter as sample size increases.

- **Efficiency**: Among unbiased estimators, it achieves the minimum possible variance.

The following estimators are analyzed:

- $\mu = \frac{1}{n} \sum_{i=1}^{n} X_{i}$ (Sample Mean)

- $s^2 = \frac{1}{n} \sum_{i=1}^{n} (X_{i}- \mu)^2$ (Sample Variance)

- $s^{*2} = \frac{1}{n-1} \sum_{i=1}^{n} (X_{i}- \mu)^2$ (Star Sample Variance)

## Central Limit Theorem study

This project also tests the validity of the Central Limit Theorem, which states:

*For sufficiently large sample sizes, the distribution of the sample mean converges to a Gaussian distribution, regardless of the underlying population.*

The CLT is tested in two cases:

- Single (pure) distribution 
- Mixture of distributions

Key points that are validated:

- The sampling distribution of the mean approaches a normal distribution as the sample size increases.

- The mean of the sampling distribution matches the population mean.

- The standard deviation of the sample mean distribution is called **Standard Error** and is given from the formula $\frac{\sigma_{population}}{\sqrt{n_{sample}}}$.

## Project Structure 

- **estimators.ipynb** - Estimator properties simulations, explanations and figures.
- **CLT.ipynb** - CLT simulations, explanations and figures.
- **stats_utils.py** - Module that contains modular, reusable functions for Monte Carlo experiments and plotting.

## Skills Demonstrated

- **Statistical Modeling**: Studying estimator properties according to statistical theory
- **Monte Carlo Simulation**: Handling datasets of randomly generated numbers
- **Software Engineering**: Modular, reproducible Python code
- **Visualization**: Clear presentation of statistical results
- **Quantitative Reasoning**: Linking theory to practical applications

## Technologies Used

- Python 3.13.9
- Numpy
- Matplotlib
- Jupyter Notebooks

## Usage

## Usage

To run this project, the user needs to clone the repository and install the required libraries using the following command:

```bash
pip install numpy matplotlib jupyter 
```

Then, they can run the `estimators.ipynb` and `CLT.ipynb` notebooks with the following command:

```bash
jupyter notebook estimators.ipynb
jupyter notebook CLT.ipynb
```

## Statistical Properties of Estimators - Key results

Monte Carlo simulations confirm theoretical expectations:

- The sample mean is unbiased and consistent.
- The variance estimator using $\frac{1}{n}$ is biased.
- The $\frac{1}{n-1}$ corrected variance estimator is unbiased.

## Central Limit Theorem - Key results

Monte Carlo simulations confirm theoretical expectations:

- When the sample size is large enough, both in the cases of a pure distribution and a mix of distributions, the sample mean tends to follow a Gaussian distribution
- The mean value of the sample mean is very close to the mean value of the initial distribution for both cases 
- The Standard Error formula holds for both cases