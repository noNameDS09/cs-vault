---
tags: [probability, statistics, gate-da, formula-sheet, revision]
---

# Formula Sheet - GATE DA 2027 Probability & Statistics

> [!important] **30-Minute Pre-Exam Revision** - All key formulas only, no explanations

---

## PROBABILITY BASICS

### Sample Space & Events
$$
P(\Omega) = 1, \quad 0 \leq P(A) \leq 1
$$
$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$
$$
P(A^c) = 1 - P(A)
$$
$$
P(A \setminus B) = P(A) - P(A \cap B)
$$

### Conditional Probability
$$
P(A|B) = \frac{P(A \cap B)}{P(B)}, \quad P(B) > 0
$$

### Multiplication Rule
$$
P(A \cap B) = P(A|B)P(B) = P(B|A)P(A)
$$

### Total Probability Theorem
If $B_1, ..., B_n$ partition $\Omega$:
$$
P(A) = \sum_{i=1}^n P(A|B_i)P(B_i)
$$

### Bayes Theorem
$$
P(B_i|A) = \frac{P(A|B_i)P(B_i)}{\sum_{j=1}^n P(A|B_j)P(B_j)}
$$

### Independence
$$
P(A \cap B) = P(A)P(B) \quad \Leftrightarrow \quad A \perp B
$$
$$
P(A|B) = P(A), \quad P(B|A) = P(B)
$$

---

## COUNTING

### Fundamental Principle
$$
\text{Total ways} = n_1 \times n_2 \times ... \times n_k
$$

### Permutations
$$
^nP_r = \frac{n!}{(n-r)!} \quad \text{(order matters)}
$$
$$
^nP_n = n! \quad \text{(arrange all)}
$$

### Circular Permutations
$$
\text{Distinct arrangements} = (n-1)! \quad \text{(clockwise $\neq$ anticlockwise)}
$$
$$
\text{If reflections same} = \frac{(n-1)!}{2}
$$

### Combinations
$$
^nC_r = \binom{n}{r} = \frac{n!}{r!(n-r)!} \quad \text{(order doesn't matter)}
$$
$$
^nC_r = ^nC_{n-r}
$$

### With Repetition
$$
\text{Multiset: } \binom{n+r-1}{r} \quad \text{(stars and bars)}
$$

### Complementary Counting
$$
\text{Wanted} = \text{Total} - \text{Unwanted}
$$

---

## RANDOM VARIABLES

### PMF (Discrete)
$$
P(X = x_i) = p_i, \quad \sum p_i = 1, \quad p_i \geq 0
$$

### PDF (Continuous)
$$
f(x) \geq 0, \quad \int_{-\infty}^{\infty} f(x) dx = 1
$$
$$
P(a \leq X \leq b) = \int_a^b f(x) dx
$$

### CDF (Both)
$$
F(x) = P(X \leq x)
$$
Discrete: $F(x) = \sum_{x_i \leq x} p_i$
Continuous: $F(x) = \int_{-\infty}^x f(t) dt$

Properties: $F(-\infty)=0$, $F(\infty)=1$, non-decreasing, right-continuous

---

## EXPECTATION & VARIANCE

### Expectation
$$
E[X] = \sum x_i p_i \quad \text{(discrete)}
$$
$$
E[X] = \int_{-\infty}^{\infty} x f(x) dx \quad \text{(continuous)}
$$
Linearity: $E[aX + bY + c] = aE[X] + bE[Y] + c$

### Function of RV
$$
E[g(X)] = \sum g(x_i) p_i \quad \text{or} \quad \int g(x) f(x) dx
$$

### Variance
$$
Var(X) = E[(X - \mu)^2] = E[X^2] - (E[X])^2
$$
$$
Var(aX + b) = a^2 Var(X)
$$
$$
Var(X) = E[X^2] - \mu^2
$$

### Standard Deviation
$$
\sigma_X = \sqrt{Var(X)}
$$

### Covariance
$$
Cov(X, Y) = E[XY] - E[X]E[Y]
$$
$$
Cov(aX + b, cY + d) = ac \cdot Cov(X, Y)
$$

### Correlation
$$
\rho_{XY} = \frac{Cov(X, Y)}{\sigma_X \sigma_Y}, \quad -1 \leq \rho \leq 1
$$

### Variance of Sum
$$
Var(X + Y) = Var(X) + Var(Y) + 2Cov(X, Y)
$$
If independent: $Var(X+Y) = Var(X) + Var(Y)$

### Variance of Linear Combination
$$
Var\left(\sum_{i=1}^n a_i X_i\right) = \sum_{i=1}^n a_i^2 Var(X_i) + 2\sum_{i<j} a_i a_j Cov(X_i, X_j)
$$

---

## MOMENTS

### Raw Moments
$$
\mu_k' = E[X^k]
$$

### Central Moments
$$
\mu_k = E[(X - \mu)^k]
$$
$\mu_1 = 0$, $\mu_2 = \sigma^2$, $\mu_3$ = skewness, $\mu_4$ = kurtosis

### Skewness
$$
\gamma_1 = \frac{E[(X-\mu)^3]}{\sigma^3}
$$

### Kurtosis
$$
\gamma_2 = \frac{E[(X-\mu)^4]}{\sigma^4} - 3 \quad \text{(excess kurtosis)}
$$

### MGF (Moment Generating Function)
$$
M_X(t) = E[e^{tX}]
$$
$$
E[X^k] = \frac{d^k}{dt^k} M_X(t) \bigg|_{t=0}
$$

---

## DISCRETE DISTRIBUTIONS

### Bernoulli($p$)
$$
P(X=x) = p^x (1-p)^{1-x}, \quad x \in \{0,1\}
$$
$$
E[X] = p, \quad Var(X) = p(1-p) = pq
$$

### Binomial($n, p$)
$$
P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad k = 0,1,...,n
$$
$$
E[X] = np, \quad Var(X) = np(1-p) = npq
$$
Sum of $n$ i.i.d. Bernoulli($p$)

### Geometric($p$) - Number of trials until first success
$$
P(X=k) = (1-p)^{k-1} p, \quad k = 1,2,...
$$
$$
E[X] = \frac{1}{p}, \quad Var(X) = \frac{1-p}{p^2}
$$
Memoryless: $P(X > m+n | X > m) = P(X > n)$

### Poisson($\lambda$)
$$
P(X=k) = \frac{e^{-\lambda} \lambda^k}{k!}, \quad k = 0,1,2,...
$$
$$
E[X] = \lambda, \quad Var(X) = \lambda
$$
Sum of independent Poissons: $X+Y \sim Poisson(\lambda_1 + \lambda_2)$
Binomial approx: if $n$ large, $p$ small, $np = \lambda$

---

## CONTINUOUS DISTRIBUTIONS

### Uniform($a, b$)
$$
f(x) = \frac{1}{b-a}, \quad a \leq x \leq b
$$
$$
E[X] = \frac{a+b}{2}, \quad Var(X) = \frac{(b-a)^2}{12}
$$

### Exponential($\lambda$)
$$
f(x) = \lambda e^{-\lambda x}, \quad x \geq 0
$$
$$
F(x) = 1 - e^{-\lambda x}
$$
$$
E[X] = \frac{1}{\lambda}, \quad Var(X) = \frac{1}{\lambda^2}
$$
Memoryless: $P(X > s+t | X > s) = P(X > t)$
Related to Poisson process

### Normal($\mu, \sigma^2$)
$$
f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}
$$
$$
E[X] = \mu, \quad Var(X) = \sigma^2
$$

### Standard Normal $Z \sim N(0,1)$
$$
\phi(z) = \frac{1}{\sqrt{2\pi}} e^{-z^2/2}
$$
$$
\Phi(z) = P(Z \leq z)
$$
Standardization: $Z = \frac{X - \mu}{\sigma}$

Key Values:
$$
P(-1 < Z < 1) \approx 0.6827 \quad (68\%)
$$
$$
P(-2 < Z < 2) \approx 0.9545 \quad (95\%)
$$
$$
P(-3 < Z < 3) \approx 0.9973 \quad (99.7\%)
$$
$$
z_{0.025} = 1.96, \quad z_{0.05} = 1.645, \quad z_{0.005} = 2.576
$$

---

## LAW OF LARGE NUMBERS & CLT

### Weak LLN
For i.i.d. $X_1, ..., X_n$ with mean $\mu$:
$$
\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i \xrightarrow{P} \mu
$$

### Central Limit Theorem
For i.i.d. $X_i$ with mean $\mu$, variance $\sigma^2$:
$$
\frac{\bar{X}_n - \mu}{\sigma/\sqrt{n}} \xrightarrow{d} N(0,1)
$$
Equivalent: $\bar{X}_n \approx N\left(\mu, \frac{\sigma^2}{n}\right)$ for large $n$

Standard Error:
$$
SE(\bar{X}) = \frac{\sigma}{\sqrt{n}}
$$

---

## DESCRIPTIVE STATISTICS

### Mean
$$
\bar{x} = \frac{1}{n}\sum_{i=1}^n x_i
$$
Weighted: $\bar{x} = \frac{\sum w_i x_i}{\sum w_i}$

### Median
Middle value (or average of two middle values)

### Mode
Most frequent value

### Range
$$
R = x_{max} - x_{min}
$$

### Variance
Population: $\sigma^2 = \frac{1}{N}\sum (x_i - \mu)^2$
Sample: $s^2 = \frac{1}{n-1}\sum (x_i - \bar{x})^2$

### Standard Deviation
$\sigma = \sqrt{\sigma^2}$, $s = \sqrt{s^2}$

### Quartiles
$Q_1$ = 25th percentile, $Q_2$ = median, $Q_3$ = 75th percentile
$IQR = Q_3 - Q_1$

### Coefficient of Variation
$$
CV = \frac{s}{\bar{x}} \times 100\%
$$

### Skewness (Sample)
$$
g_1 = \frac{n}{(n-1)(n-2)} \sum \left(\frac{x_i - \bar{x}}{s}\right)^3
$$

### Kurtosis (Sample)
$$
g_2 = \frac{n(n+1)}{(n-1)(n-2)(n-3)} \sum \left(\frac{x_i - \bar{x}}{s}\right)^4 - \frac{3(n-1)^2}{(n-2)(n-3)}
$$

### Pearson Correlation
$$
r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2 \sum (y_i - \bar{y})^2}}
$$

---

## SAMPLING DISTRIBUTIONS

### Sample Mean
If $X_i \sim N(\mu, \sigma^2)$: $\bar{X} \sim N\left(\mu, \frac{\sigma^2}{n}\right)$
If population not normal but $n \geq 30$: $\bar{X} \approx N\left(\mu, \frac{\sigma^2}{n}\right)$

### Sample Variance
If $X_i \sim N(\mu, \sigma^2)$:
$$
\frac{(n-1)s^2}{\sigma^2} \sim \chi^2_{n-1}
$$

---

## ESTIMATION

### MLE Procedure
1. Write likelihood: $L(\theta) = \prod f(x_i; \theta)$
2. Take log: $\ell(\theta) = \sum \log f(x_i; \theta)$
3. Differentiate: $\frac{d\ell}{d\theta} = 0$
4. Solve for $\hat{\theta}$
5. Check second derivative < 0 or boundary

### Common MLEs
- Bernoulli: $\hat{p} = \bar{x}$
- Binomial: $\hat{p} = \bar{x}/n$
- Poisson: $\hat{\lambda} = \bar{x}$
- Normal: $\hat{\mu} = \bar{x}$, $\hat{\sigma}^2 = \frac{1}{n}\sum(x_i-\bar{x})^2$
- Exponential: $\hat{\lambda} = 1/\bar{x}$

### Method of Moments
Equate sample moments to population moments:
$$
m_k = \frac{1}{n}\sum x_i^k = \mu_k'(\theta)
$$
Solve for parameters.

### Bias, MSE
$$
Bias(\hat{\theta}) = E[\hat{\theta}] - \theta
$$
$$
MSE(\hat{\theta}) = Var(\hat{\theta}) + Bias(\hat{\theta})^2
$$

---

## CONFIDENCE INTERVALS

### Mean ($\sigma$ known)
$$
\bar{x} \pm z_{\alpha/2} \frac{\sigma}{\sqrt{n}}
$$

### Mean ($\sigma$ unknown, $n$ large)
$$
\bar{x} \pm z_{\alpha/2} \frac{s}{\sqrt{n}}
$$

### Mean ($\sigma$ unknown, $n$ small, normal pop.)
$$
\bar{x} \pm t_{\alpha/2, n-1} \frac{s}{\sqrt{n}}
$$

### Difference of Means ($\sigma_1, \sigma_2$ known)
$$
(\bar{x}_1 - \bar{x}_2) \pm z_{\alpha/2} \sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}
$$

### Difference of Means (unknown, equal variances)
$$
(\bar{x}_1 - \bar{x}_2) \pm t_{\alpha/2, n_1+n_2-2} s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}
$$
where $s_p^2 = \frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1+n_2-2}$

### Proportion
$$
\hat{p} \pm z_{\alpha/2} \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}
$$

### Variance
$$
\left(\frac{(n-1)s^2}{\chi^2_{\alpha/2, n-1}}, \frac{(n-1)s^2}{\chi^2_{1-\alpha/2, n-1}}\right)
$$

---

## HYPOTHESIS TESTING

### Test Statistics

| Test | Statistic | Distribution |
|------|-----------|--------------|
| z-test (mean, $\sigma$ known) | $z = \frac{\bar{x} - \mu_0}{\sigma/\sqrt{n}}$ | $N(0,1)$ |
| z-test (proportion) | $z = \frac{\hat{p} - p_0}{\sqrt{p_0(1-p_0)/n}}$ | $N(0,1)$ |
| t-test (mean, $\sigma$ unknown) | $t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}}$ | $t_{n-1}$ |
| Two-sample t (equal var) | $t = \frac{\bar{x}_1 - \bar{x}_2}{s_p\sqrt{1/n_1+1/n_2}}$ | $t_{n_1+n_2-2}$ |
| Chi-square (variance) | $\chi^2 = \frac{(n-1)s^2}{\sigma_0^2}$ | $\chi^2_{n-1}$ |
| Chi-square (goodness of fit) | $\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}$ | $\chi^2_{k-1}$ |
| F-test (variance ratio) | $F = \frac{s_1^2}{s_2^2}$ | $F_{n_1-1, n_2-1}$ |

### Decision Rule
Reject $H_0$ if: $|test stat| > critical value$ OR $p\text{-value} < \alpha$

### Types of Errors
- Type I: Reject $H_0$ when true $\rightarrow$ $\alpha = P(\text{Type I})$
- Type II: Fail to reject $H_0$ when false $\rightarrow$ $\beta = P(\text{Type II})$
- Power = $1 - \beta$

---

## ANOVA (One-Way)

| Source | SS | df | MS | F |
|--------|-----|-----|-----|-----|
| Between | $SS_B = \sum n_i(\bar{x}_i - \bar{\bar{x}})^2$ | $k-1$ | $MS_B = SS_B/(k-1)$ | $MS_B/MS_W$ |
| Within | $SS_W = \sum (n_i-1)s_i^2$ | $N-k$ | $MS_W = SS_W/(N-k)$ | |
| Total | $SS_T = SS_B + SS_W$ | $N-1$ | | |

---

## PROBABILITY INEQUALITIES

### Markov
For $X \geq 0$, $a > 0$:
$$
P(X \geq a) \leq \frac{E[X]}{a}
$$

### Chebyshev
For any $X$ with finite $\mu, \sigma^2$:
$$
P(|X - \mu| \geq k\sigma) \leq \frac{1}{k^2}, \quad k > 0
$$
Equivalently:
$$
P(|X - \mu| < k\sigma) \geq 1 - \frac{1}{k^2}
$$

---

## TRANSFORMATIONS

### Monotonic $Y = g(X)$ (strictly increasing/decreasing)
$$
f_Y(y) = f_X(g^{-1}(y)) \left| \frac{d}{dy} g^{-1}(y) \right|
$$

### Linear $Y = aX + b$
$$
f_Y(y) = \frac{1}{|a|} f_X\left(\frac{y-b}{a}\right)
$$
$$
E[Y] = aE[X] + b, \quad Var(Y) = a^2 Var(X)
$$

---

## REGRESSION (Simple Linear)

### Model
$y = \beta_0 + \beta_1 x + \epsilon$, $\epsilon \sim N(0, \sigma^2)$

### Estimates
$$
\hat{\beta}_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} = \frac{S_{xy}}{S_{xx}}
$$
$$
\hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x}
$$

### $R^2$
$$
R^2 = \frac{SS_{reg}}{SS_{tot}} = 1 - \frac{SS_{res}}{SS_{tot}} = r^2
$$

### Standard Error
$$
s = \sqrt{\frac{SS_{res}}{n-2}} = \sqrt{MSE}
$$
$$
SE(\hat{\beta}_1) = \frac{s}{\sqrt{S_{xx}}}
$$

---

## Related Notes

- [[Glossary]]
- [[GATE Numerical Tricks]]

---

#probability #statistics #gate-da #formula-sheet #revision