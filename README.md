# Statistical Properties of Estimators

## Overview

This project investigates the statistical properties of common estimators through theoretical analysis and Monte Carlo simulation. The goal is to empirically validate unbiasedness, consistency, and efficiency using reproducible, modular Python code. These qualities are briefly explained below:

- **Unbiasedness**: The expected value of the estimator equals the true parameter value.

- **Consistency**: The estimator converges in probability to the true parameter as sample size increases.

- **Efficiency**: Among unbiased estimators, it achieves the minimum possible variance.

The following estimators are analyzed:

- $\mu = \frac{1}{n} \sum_{i=1}^{n} X_{i}$ (Sample Mean)

- $s^2 = \frac{1}{n} \sum_{i=1}^{n} (X_{i}- \mu)^2$ (Sample Variance)

- $s^{*2} = \frac{1}{n-1} \sum_{i=1}^{n} (X_{i}- \mu)^2$ (Star Sample Variance)

The study evaluates whether each estimator satisfies these properties. The implementation follows a modular design with input validation and parameterized simulation experiments.

## Skills Demonstrated

- **Statistical Modeling**: Studying estimator properties according to statistical theory
- **Monte Carlo Simulation**: Handling datasets of randomly generated numbers
- **Software Engineering**: Modular, reproducible Python code
- **Visualization**: Clear presentation of statistical results
- **Results Communication**: Reasoning and explanation of the derived results

## Technologies Used

- Python 3.13.9
- Numpy
- Matplotlib

## Key Results

Monte Carlo simulations confirm theoretical expectations:

- The sample mean is unbiased and consistent.
- The variance estimator using 1/n is biased.
- The 1/(n-1) corrected variance estimator is unbiased.
- Empirical variance decreases with increasing sample size, illustrating consistency.