---
tags: [probability, statistics, gate-da, glossary, revision]
---

# Glossary - Probability & Statistics

> [!note] Alphabetical reference of all terminology for GATE DA 2027

---

## A

### Alternative Hypothesis ($H_1$ or $H_a$)
A hypothesis representing a departure from the null hypothesis. The hypothesis we typically want to find evidence for.

### Addition Theorem
$P(A \cup B) = P(A) + P(B) - P(A \cap B)$. For mutually exclusive events: $P(A \cup B) = P(A) + P(B)$.

### Almost Sure Convergence
A sequence of random variables $X_n$ converges almost surely to $X$ if $P(\lim_{n \to \infty} X_n = X) = 1$.

### ANOVA (Analysis of Variance)
A statistical method to compare means of three or more groups by analyzing variance components.

### Average / Mean
The sum of values divided by count. Sample mean $\bar{x} = \frac{1}{n}\sum x_i$. Population mean $\mu = E[X]$.

---

## B

### Bayes Theorem
$P(B|A) = \frac{P(A|B)P(B)}{P(A)}$. Updates prior probability to posterior using likelihood.

### Bernoulli Distribution
Discrete distribution with two outcomes (success/failure). $P(X=1)=p$, $P(X=0)=1-p$.

### Bias of an Estimator
$Bias(\hat{\theta}) = E[\hat{\theta}] - \theta$. Difference between expected estimate and true parameter.

### Binomial Distribution
Number of successes in $n$ independent Bernoulli trials. $P(X=k) = \binom{n}{k}p^k(1-p)^{n-k}$.

### Box Plot
Graphical representation of five-number summary: minimum, Q1, median, Q3, maximum.

### Central Limit Theorem (CLT)
Sample mean of i.i.d. variables approaches normal distribution regardless of population distribution as $n \to \infty$.

### Chi-Square Distribution
Distribution of sum of squared standard normals. Used for variance tests and goodness-of-fit.

### Coefficient of Variation (CV)
$CV = \frac{s}{\bar{x}} \times 100\%$. Relative measure of dispersion, unit-free.

### Combination
Selection of $r$ objects from $n$ without regard to order: $\binom{n}{r} = \frac{n!}{r!(n-r)!}$.

### Complement of an Event
$A^c = \Omega \setminus A$. $P(A^c) = 1 - P(A)$.

### Conditional Probability
$P(A|B) = \frac{P(A \cap B)}{P(B)}$, $P(B) > 0$. Probability of $A$ given $B$ occurred.

### Confidence Interval
An interval estimate of a parameter with a specified confidence level $(1-\alpha)$.

### Confidence Level
$1-\alpha$. Probability that the interval contains the true parameter in repeated sampling.

### Continuous Random Variable
Takes uncountably infinite values. Described by probability density function (PDF).

### Correlation Coefficient
$\rho = \frac{Cov(X,Y)}{\sigma_X \sigma_Y}$. Measures linear relationship strength, ranges $[-1, 1]$.

### Covariance
$Cov(X,Y) = E[XY] - E[X]E[Y]$. Measures joint variability direction.

### Critical Value
Threshold value of test statistic that separates rejection and non-rejection regions.

### Cumulative Distribution Function (CDF)
$F(x) = P(X \leq x)$. Gives probability that RV is $\leq x$.

---

## D

### Degrees of Freedom
Number of independent values in a calculation. For sample variance: $n-1$.

### Descriptive Statistics
Methods for summarizing and describing data: mean, median, mode, variance, etc.

### Discrete Random Variable
Takes countable number of distinct values. Described by probability mass function (PMF).

### Distribution
A mathematical function describing probabilities of all possible outcomes.

---

## E

### Empirical Rule (68-95-99.7 Rule)
For normal distribution: 68% within 1$\sigma$, 95% within 2$\sigma$, 99.7% within 3$\sigma$.

### Estimator
A rule/formula to estimate a parameter from sample data. A random variable.

### Estimate
The numerical value obtained by applying an estimator to a specific sample.

### Event
A subset of the sample space. Collection of outcomes to which probability is assigned.

### Expectation / Expected Value
$E[X] = \sum x_i p_i$ (discrete) or $\int x f(x) dx$ (continuous). Long-run average.

### Exponential Distribution
Continuous distribution modeling time between events in Poisson process. Memoryless property.

---

## F

### F-Distribution
Ratio of two independent chi-square variables divided by their degrees of freedom. Used in ANOVA and variance ratio tests.

### Factorial
$n! = n \times (n-1) \times ... \times 1$. $0! = 1$.

### Frequency Distribution
Table showing how often each value/range occurs in a dataset.

---

## G

### Geometric Distribution
Number of trials until first success. $P(X=k) = (1-p)^{k-1}p$. Memoryless property.

### Goodness of Fit Test
Tests whether observed frequencies match expected frequencies from a distribution.

---

## H

### Histogram
Bar chart representing frequency distribution of continuous data.

### Hypothesis
A statement about a population parameter to be tested.

### Hypothesis Testing
Formal procedure to make decisions about population parameters using sample data.

---

## I

### Independent Events
$P(A \cap B) = P(A)P(B)$. Occurrence of one doesn't affect probability of the other.

### Independent Random Variables
Joint distribution equals product of marginals: $f(x,y) = f_X(x)f_Y(y)$.

### Interquartile Range (IQR)
$IQR = Q_3 - Q_1$. Measure of spread resistant to outliers.

### Interval Estimation
Providing a range of plausible values for a parameter (confidence interval).

---

## J

### Joint Distribution
Probability distribution of two or more random variables simultaneously.

---

## K

### Kurtosis
Measure of tail heaviness. Normal distribution has excess kurtosis = 0.

---

## L

### Law of Large Numbers (LLN)
Sample mean converges to population mean as sample size increases.

### Level of Significance
$\alpha = P(\text{Type I Error})$. Maximum acceptable probability of rejecting true $H_0$.

### Likelihood Function
$L(\theta) = \prod f(x_i; \theta)$. Viewed as function of parameter given observed data.

### Log-Likelihood
$\ell(\theta) = \log L(\theta)$. Easier to differentiate for MLE.

---

## M

### Marginal Distribution
Distribution of a subset of variables obtained by summing/integrating over others.

### Maximum Likelihood Estimation (MLE)
Method finding parameter values that maximize the likelihood function.

### Mean
See Average.

### Mean Squared Error (MSE)
$MSE(\hat{\theta}) = E[(\hat{\theta} - \theta)^2] = Var(\hat{\theta}) + Bias^2$.

### Median
Middle value when data is ordered. 50th percentile.

### Memoryless Property
$P(X > s+t | X > s) = P(X > t)$. Only exponential (continuous) and geometric (discrete) have this.

### Method of Moments
Equating sample moments to population moments to estimate parameters.

### Mode
Most frequently occurring value.

### Moment Generating Function (MGF)
$M_X(t) = E[e^{tX}]$. Uniquely determines distribution. $k$-th derivative at 0 gives $k$-th moment.

### Mutually Exclusive Events
$A \cap B = \emptyset$. Cannot occur simultaneously. $P(A \cup B) = P(A) + P(B)$.

---

## N

### Normal Distribution
Bell-shaped continuous distribution. $f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$.

### Null Hypothesis ($H_0$)
Default assumption (no effect/no difference) tested against alternative.

---

## O

### Observed Value
Actual data point obtained from experiment/survey.

### One-Tailed Test
Alternative hypothesis specifies direction ($>$ or $<$). Rejection region in one tail.

---

## P

### Parameter
Numerical characteristic of a population (e.g., $\mu$, $\sigma^2$, $p$).

### Percentile
Value below which a given percentage of observations fall.

### Permutation
Arrangement of $r$ objects from $n$ where order matters: $^nP_r = \frac{n!}{(n-r)!}$.

### Poisson Distribution
Counts events in fixed interval. $P(X=k) = \frac{e^{-\lambda}\lambda^k}{k!}$. Mean = Variance = $\lambda$.

### Point Estimation
Providing a single value estimate of a parameter.

### Population
Complete set of all possible observations of interest.

### Population Variance
$\sigma^2 = \frac{1}{N}\sum_{i=1}^N (x_i - \mu)^2$.

### Power of a Test
$1 - \beta$. Probability of correctly rejecting false $H_0$.

### Probability
Measure of likelihood of an event. Axioms: non-negativity, normalization, additivity.

### Probability Density Function (PDF)
$f(x)$ for continuous RV. $P(a \leq X \leq b) = \int_a^b f(x)dx$.

### Probability Mass Function (PMF)
$P(X=x)$ for discrete RV. Gives probability for each possible value.

### p-Value
Smallest significance level at which $H_0$ would be rejected. $P(\text{test stat} \geq \text{observed} | H_0 \text{ true})$.

---

## Q

### Quantile
Cut point dividing distribution into equal probability intervals.

### Quartiles
$Q_1$ (25th percentile), $Q_2$ (median), $Q_3$ (75th percentile).

---

## R

### Random Variable
A function mapping outcomes to real numbers. Discrete or continuous.

### Random Sampling
Every sample of size $n$ has equal probability of selection.

### Range
$R = \max - \min$. Simplest measure of spread.

### Rejection Region
Set of test statistic values leading to rejection of $H_0$.

### Regression
Modeling relationship between dependent and independent variables.

---

## S

### Sample
Subset of population selected for observation.

### Sample Mean
$\bar{x} = \frac{1}{n}\sum_{i=1}^n x_i$.

### Sample Variance
$s^2 = \frac{1}{n-1}\sum_{i=1}^n (x_i - \bar{x})^2$. Unbiased estimator of $\sigma^2$.

### Sampling Distribution
Probability distribution of a statistic over all possible samples.

### Significance Level
$\alpha$. Threshold for p-value to reject $H_0$. Common: 0.05, 0.01.

### Skewness
Measure of asymmetry. Positive = right-skewed, Negative = left-skewed.

### Standard Deviation
$\sigma = \sqrt{Var(X)}$. Square root of variance. Same units as data.

### Standard Error
$SE = \frac{\sigma}{\sqrt{n}}$ (or $s/\sqrt{n}$). Standard deviation of sampling distribution of statistic.

### Standard Normal Distribution
$Z \sim N(0,1)$. Mean 0, variance 1.

### Statistic
A function of sample data. Used to estimate parameters.

### Sufficient Statistic
Statistic that captures all information about parameter from sample.

---

## T

### t-Distribution
Distribution of $\frac{\bar{X}-\mu}{s/\sqrt{n}}$ for normal population. Heavier tails than normal.

### Test Statistic
Standardized value computed from sample data to test $H_0$.

### Two-Tailed Test
Alternative hypothesis: parameter $\neq$ value. Rejection regions in both tails.

### Type I Error
Rejecting $H_0$ when it is true. Probability = $\alpha$.

### Type II Error
Failing to reject $H_0$ when it is false. Probability = $\beta$.

---

## U

### Unbiased Estimator
$E[\hat{\theta}] = \theta$. Expected value equals true parameter.

### Uniform Distribution
All outcomes equally likely. Continuous: $f(x) = \frac{1}{b-a}$ on $[a,b]$.

---

## V

### Variance
$Var(X) = E[(X-\mu)^2] = E[X^2] - \mu^2$. Average squared deviation from mean.

---

## Z

### Z-Score
$Z = \frac{X - \mu}{\sigma}$. Number of standard deviations from mean.

### Z-Test
Hypothesis test using standard normal distribution. Used when $\sigma$ known or $n$ large.

---

## Related Notes

- [[Formula Sheet]]
- [[GATE Numerical Tricks]]

---

#probability #statistics #gate-da #glossary #revision