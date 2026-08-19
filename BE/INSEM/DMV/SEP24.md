# SPPU AIDS BE SEM VII - Data Modeling & Visualization (DMV) In-Sem Exam Answers (SEP 2024)

> **Course**: Data Modeling & Visualization | **Semester**: VII | **Branch**: AIDS
> **Exam**: In-Semester Examination | **Date**: September 2024
> **Total Marks**: 50

---

## Question 1

### Q1(a) Explain Covariance and Central Limit Theorem. [5]

---

#### Covariance

**Definition**: Covariance measures the **direction** of the linear relationship between two random variables $X$ and $Y$.

$$\text{Cov}(X, Y) = \mathbb{E}[(X - \mu_X)(Y - \mu_Y)] = \frac{1}{n-1} \sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y}) \quad \text{(sample)}$$

---

##### Types of Covariance

| Type | Condition | Interpretation | Graph Pattern |
|------|-----------|----------------|---------------|
| **Positive** | $\text{Cov}(X,Y) > 0$ | $X \uparrow \Rightarrow Y \uparrow$ | Upward slope ↗ |
| **Negative** | $\text{Cov}(X,Y) < 0$ | $X \uparrow \Rightarrow Y \downarrow$ | Downward slope ↘ |
| **Zero** | $\text{Cov}(X,Y) = 0$ | No linear relationship | Random cloud / symmetric curve |

---

##### Graphs

**Positive Covariance**:
```
Y ↑
  │             ●
  │           ●
  │         ●
  │       ●
  │     ●
  │   ●
  │ ●
  └──────────────────→ X
       Positive Covariance
       (Upward trend)
```

**Negative Covariance**:
```
Y ↑ ●
  │    ●
  │      ●
  │        ●
  │          ●
  │            ●
  │              ●
  │                ●
  └──────────────────→ X
```

**Zero Covariance**:
```
Y ↑   ●   ●   ●
  │  ●   ●   ●   ●
  │  ●               ●
  └────────────────────→ X
```

---

##### Relationship with Correlation

$$\rho_{XY} = \frac{\text{Cov}(X,Y)}{\sigma_X \sigma_Y} \in [-1, 1]$$

- **Correlation** = Standardized covariance (scale-invariant)
- Same sign as covariance
- $\rho = \pm 1$: Perfect linear relationship

---

#### Central Limit Theorem (CLT)

**Statement**: Let $X_1, X_2, \dots, X_n$ be **i.i.d.** random variables with mean $\mu$ and finite variance $\sigma^2$. The **sample mean** $\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i$ satisfies:

$$\frac{\bar{X}_n - \mu}{\sigma/\sqrt{n}} \xrightarrow{d} \mathcal{N}(0, 1) \quad \text{as } n \to \infty$$

Equivalently: $\bar{X}_n \xrightarrow{d} \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right)$

---

##### Key Points

| Property | Description |
|----------|-------------|
| **Distribution-free** | Works for ANY distribution with finite $\mu, \sigma^2$ |
| **Sample size** | $n \geq 30$ typically sufficient |
| **Sum version** | $\sum X_i \sim \mathcal{N}(n\mu, n\sigma^2)$ |
| **Standardized** | $Z = \frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \sim \mathcal{N}(0,1)$ |

---

##### Example: Rolling a Die

| $n$ | Distribution of $\bar{X}$ | Shape |
|-----|---------------------------|-------|
| 1 | Uniform $\{1,\dots,6\}$ | Flat |
| 2 | Triangular (2-12) | ▲ |
| 5 | Bell-shaped | ∼ Normal |
| 30 | Very close to Normal | $\mathcal{N}(3.5, 2.917/30)$ |

---

### Q1(b) Differentiate between Discrete and Continuous random variables with the help of an example. [5]

---

#### Discrete Random Variable

**Definition**: Takes **countable** number of distinct values (finite or countably infinite).

**PMF**: $P(X = x) = p(x)$ where $\sum_x p(x) = 1$

**CDF**: $F(x) = P(X \leq x) = \sum_{k \leq x} p(k)$ (step function)

**Graph**:
```
P(X=x) ↑
  0.4 ┤       ┌───┐
  0.3 ┤       │   │
  0.2 ┤   ┌───┘   └───┐
  0.1 ┤   │           │
  0.0 ┼───┼───┼───┼───┼──→ X
      0   1   2   3   4
```

---

#### Continuous Random Variable

**Definition**: Takes **uncountably infinite** values in an interval (real numbers).

**PDF**: $f(x) \geq 0$, $\int_{-\infty}^{\infty} f(x) dx = 1$

**Probability**: $P(a \leq X \leq b) = \int_a^b f(x) dx$ (area under curve)

**CDF**: $F(x) = \int_{-\infty}^x f(t) dt$ (continuous, non-decreasing)

**Graph**:
```
f(x) ↑
     │        ╭─────────╮
     │       ╱           ╲
     │      ╱             ╲
     │     ╱               ╲
     │    ╱                 ╲
     └─────────────────────────→ X
```

---

#### Key Differences

| Aspect | Discrete RV | Continuous RV |
|--------|-------------|---------------|
| **Values** | Countable set $\{x_1, x_2, \dots\}$ | Uncountable interval $[a,b]$ or $\mathbb{R}$ |
| **Probability Function** | PMF: $P(X=x)$ | PDF: $f(x)$ (density, not probability) |
| **$P(X=x)$** | $> 0$ possible | **Always 0** |
| **Probability Calculation** | Summation $\sum p(x)$ | Integration $\int f(x) dx$ |
| **CDF** | Step function (jumps) | Continuous, differentiable |
| **Expected Value** | $\sum x \cdot p(x)$ | $\int x f(x) dx$ |
| **Variance** | $\sum (x-\mu)^2 p(x)$ | $\int (x-\mu)^2 f(x) dx$ |

---

#### Examples

| Type | Example | Distribution |
|------|---------|--------------|
| **Discrete** | Number of heads in 10 coin tosses | Binomial(10, 0.5) |
| **Discrete** | Number of customers arriving per hour | Poisson($\lambda$) |
| **Discrete** | Roll of a die (1-6) | Uniform{1,2,3,4,5,6} |
| **Continuous** | Height of adult males | Normal($\mu, \sigma^2$) |
| **Continuous** | Time between bus arrivals | Exponential($\lambda$) |
| **Continuous** | Stock price returns | Log-normal |

---

### Q1(c) Define Independent Variable and explain types of Independent Variables with Example. [5]

---

#### Independent Variable

**Definition**: An **independent variable** (also called **predictor**, **feature**, **explanatory variable**, or **input variable**) is a variable that is **manipulated** or **observed** to determine its effect on the **dependent variable** (target/response).

In modeling: $Y = f(X_1, X_2, \dots, X_p) + \epsilon$

- $Y$ = Dependent variable (outcome)
- $X_1, \dots, X_p$ = Independent variables (predictors)

---

#### Types of Independent Variables

| Type | Description | Example |
|------|-------------|---------|
| **Quantitative (Continuous)** | Numeric, measurable on continuous scale | Age, Temperature, Income, Blood Pressure |
| **Quantitative (Discrete)** | Numeric, countable values | Number of children, Number of defects, Count of visits |
| **Qualitative (Categorical - Nominal)** | Categories with no natural order | Gender, Color, City, Brand |
| **Qualitative (Categorical - Ordinal)** | Categories with natural order | Education Level (HS < BS < MS < PhD), Satisfaction (Low < Med < High) |
| **Binary/Dichotomous** | Special case: only 2 categories | Yes/No, Pass/Fail, Male/Female, Treatment/Control |
| **Time/Date** | Temporal variables | Date of birth, Timestamp, Hour of day |

---

#### Detailed Classification

```
INDEPENDENT VARIABLES
         │
         ├── QUANTITATIVE (Numerical)
         │       │
         │       ├── CONTINUOUS (Infinite values in range)
         │       │     Examples: Height, Weight, Temperature, Salary, Time
         │       │
         │       └── DISCRETE (Countable values)
         │             Examples: #Children, #Products, #Errors, Count data
         │
         └── QUALITATIVE (Categorical)
                 │
                 ├── NOMINAL (No order)
                 │     Examples: Gender, Blood Type, Zip Code, Color
                 │
                 ├── ORDINAL (Natural order)
                 │     Examples: Education Level, Rating (1-5), Size (S/M/L)
                 │
                 └── BINARY (Two categories)
                       Examples: Smoker (Y/N), Disease (Y/N), Treatment (A/B)
```

---

#### Handling in Statistical Models

| Variable Type | Encoding Method | Example |
|---------------|-----------------|---------|
| **Continuous** | Use directly (maybe scale) | Age → 25, 30, 45 |
| **Discrete Count** | Use directly or as categorical | #Children → 0, 1, 2, 3+ |
| **Binary** | 0/1 encoding | Male=1, Female=0 |
| **Nominal (k categories)** | One-Hot / Dummy (k-1 columns) | Color: Red=[1,0], Blue=[0,1], Green=[0,0] |
| **Ordinal** | Integer encoding (preserves order) | Low=1, Medium=2, High=3 |
| **Date/Time** | Extract features | Year, Month, Day, Weekday, IsWeekend |

---

#### Example: House Price Prediction

| Variable | Type | Role |
|----------|------|------|
| **Price** | Continuous (Dependent) | Target $Y$ |
| **Area (sq ft)** | Continuous (Independent) | $X_1$ |
| **Bedrooms** | Discrete (Independent) | $X_2$ |
| **Location** | Nominal (Independent) | $X_3$ (Downtown/Suburb/Rural) |
| **House Age** | Continuous (Independent) | $X_4$ |
| **Garage** | Binary (Independent) | $X_5$ (Yes/No) |
| **Condition** | Ordinal (Independent) | $X_6$ (Poor/Fair/Good/Excellent) |

**Model**: $\text{Price} = \beta_0 + \beta_1\text{Area} + \beta_2\text{Bedrooms} + \beta_3\text{Location} + \dots + \epsilon$

---

## Question 2

### Q2(a) Explain Data Modelling Concepts with Example. [5]

---

#### Data Modeling Concepts

**Definition**: Data modeling is the process of creating a **conceptual representation** of data objects, their relationships, and rules for a specific domain.

---

#### Three Levels (ANSI/SPARC Architecture)

| Level | Name | Audience | Focus | Artifact |
|-------|------|----------|-------|----------|
| **1** | **Conceptual** | Business users | *What* data & relationships | ER Diagram |
| **2** | **Logical** | Data architects | *How* data structured | Normalized schema |
| **3** | **Physical** | DBAs, Developers | *Where/How* stored | DDL, Indexes |

---

#### Key Concepts

| Concept | Description |
|---------|-------------|
| **Entity** | Real-world object (Customer, Order, Product) |
| **Attribute** | Property of entity (Customer.Name, Order.Date) |
| **Relationship** | Association between entities (Customer *places* Order) |
| **Cardinality** | 1:1, 1:N, M:N (how many instances relate) |
| **Primary Key (PK)** | Unique identifier for entity instance |
| **Foreign Key (FK)** | Reference to PK of another table |
| **Normalization** | Eliminate redundancy (1NF, 2NF, 3NF, BCNF) |

---

#### Example: University Course Registration

**Conceptual (ER Diagram)**:
```
┌──────────┐        enrolls        ┌─────────┐
│ Student  │ ◄────────────────────► │ Course  │
└────┬─────┘        M:N             └────┬────┘
     │                                     │
     │ has                                 │ has
     ▼                                     ▼
┌──────────┐                         ┌──────────┐
│  Dept    │                         │Instructor│
└──────────┘                         └──────────┘
```

**Logical (Normalized Tables)**:
```sql
Student     (StudentID PK, Name, Email, DeptID FK, DOB)
Department  (DeptID PK, Name, Building, Budget)
Course      (CourseID PK, Title, Credits, DeptID FK, InstructorID FK)
Instructor  (InstructorID PK, Name, Email, DeptID FK)
Enrollment  (StudentID FK, CourseID FK, Semester, Grade, PK: StudentID+CourseID+Semester)
```

**Normalization Check**:
- **1NF**: Atomic values ✓
- **2NF**: No partial dependencies ✓ (Enrollment PK is composite)
- **3NF**: No transitive dependencies ✓ (Dept info in Department table)
- **BCNF**: Every determinant is candidate key ✓

---

### Q2(b) Explain Chebyshev inequality with the help of an example. [5]

---

#### Chebyshev's Inequality

**Theorem**: For any random variable $X$ with finite mean $\mu$ and finite variance $\sigma^2$, and for any $k > 0$:

$$P(|X - \mu| \geq k\sigma) \leq \frac{1}{k^2}$$

Equivalently:
$$P(|X - \mu| < k\sigma) \geq 1 - \frac{1}{k^2}$$

---

#### Key Features

| Feature | Description |
|---------|-------------|
| **Distribution-free** | No assumption on distribution shape (only needs $\mu, \sigma^2$) |
| **Conservative** | Bound is often loose (especially for normal distributions) |
| **Universal** | Applies to ANY distribution with finite variance |
| **Two-sided** | Bounds both tails simultaneously |

---

#### Probability Bounds Table

| $k$ | Minimum % within $k\sigma$ | Maximum % outside $k\sigma$ |
|-----|----------------------------|-----------------------------|
| 2 | 75% | 25% |
| 3 | 88.9% | 11.1% |
| 4 | 93.75% | 6.25% |
| 5 | 96% | 4% |

---

#### Comparison with Normal Distribution

| $k$ | Chebyshev (Any Distribution) | Normal Distribution |
|-----|------------------------------|---------------------|
| 1 | ≥ 0% (trivial) | 68.27% |
| 2 | ≥ 75% | 95.45% |
| 3 | ≥ 88.9% | 99.73% |

---

#### Example 1: Bolt Manufacturing

**Problem**: A factory produces bolts with mean length $\mu = 10$ cm and standard deviation $\sigma = 0.2$ cm. The distribution shape is **unknown**. What percentage of bolts have length between 9.6 cm and 10.4 cm?

**Solution**:
- Interval: $[9.6, 10.4] = [10 - 0.4, 10 + 0.4] = [\mu - 2\sigma, \mu + 2\sigma]$
- Here $k = 2$
- By Chebyshev: $P(|X - 10| < 0.4) \geq 1 - \frac{1}{2^2} = 0.75$

**Answer**: **At least 75%** of bolts lie in [9.6, 10.4] cm.

---

#### Example 2: Exam Scores

**Given**: Mean score = 70, Std dev = 10. Distribution unknown.

**Question**: What fraction scored between 50 and 90?

- $50 = 70 - 20 = \mu - 2\sigma$
- $90 = 70 + 20 = \mu + 2\sigma$
- $k = 2$

**Chebyshev says**: At least $1 - 1/4 = 75\%$ of students scored in [50, 90].

---

#### One-Sided Chebyshev (Cantelli's Inequality)

$$P(X - \mu \geq k\sigma) \leq \frac{1}{1 + k^2}$$

Useful when only upper/lower tail matters.

---

### Q2(c) Define Descriptive Statistics and Graphical Statistics. Explain different Estimation Methods. [5]

---

#### Descriptive Statistics

**Definition**: Quantitative methods for **summarizing** data using numerical measures.

**Categories**:

| Category | Measures | Purpose |
|----------|----------|---------|
| **Central Tendency** | Mean, Median, Mode | "Where is the center?" |
| **Dispersion** | Variance, Std Dev, Range, IQR, MAD | "How spread out?" |
| **Shape** | Skewness, Kurtosis | "What's the shape?" |
| **Relative Standing** | Percentiles, Quartiles, Z-scores | "Where does a value stand?" |
| **Association** | Covariance, Correlation | "How do variables relate?" |

---

#### Graphical Statistics

**Definition**: Visual methods for **exploring**, **summarizing**, and **communicating** data patterns.

**Common Types**:

| Plot Type | Purpose | Best For |
|-----------|---------|----------|
| **Histogram** | Distribution of 1 continuous var | Shape, modality, outliers |
| **Box Plot** | 5-number summary, outliers | Comparison across groups |
| **Scatter Plot** | Relationship between 2 continuous vars | Correlation, trends, clusters |
| **Bar Chart** | Categorical frequencies | Counts/proportions per category |
| **Density Plot** | Smoothed distribution | Continuous distribution shape |
| **Q-Q Plot** | Normality assessment | Theoretical vs sample quantiles |
| **Heatmap** | Correlation matrix / 2D density | Multi-variable patterns |
| **Violin Plot** | Distribution + density | Group comparison with shape |
| **Pair Plot** | All pairwise scatter plots | Multivariate exploration |
| **Time Series Plot** | Trends over time | Temporal patterns |

---

#### Estimation Methods

**Estimation**: Using sample data to infer population parameters.

---

##### 1. Point Estimation

**Single value** estimate of parameter $\theta$.

| Method | Principle | Example |
|--------|-----------|---------|
| **Method of Moments (MoM)** | Equate sample moments to population moments | $\hat{\mu} = \bar{x}$, $\hat{\sigma}^2 = \frac{1}{n}\sum(x_i-\bar{x})^2$ |
| **Maximum Likelihood (MLE)** | Maximize likelihood function | $\hat{\mu} = \bar{x}$, $\hat{\sigma}^2_{\text{MLE}} = \frac{1}{n}\sum(x_i-\bar{x})^2$ |
| **Bayesian Estimation** | Posterior mean/median/mode | $\hat{\theta}_{\text{Bayes}} = \mathbb{E}[\theta \mid X]$ |
| **Least Squares** | Minimize sum of squared residuals | Linear regression coefficients |

**Properties of Good Estimators**:
- **Unbiased**: $\mathbb{E}[\hat{\theta}] = \theta$
- **Consistent**: $\hat{\theta}_n \xrightarrow{p} \theta$
- **Efficient**: Minimum variance among unbiased estimators
- **Sufficient**: Uses all information in sample

---

##### 2. Interval Estimation (Confidence Intervals)

**Range of plausible values** with confidence level $1-\alpha$.

**General Form**: $\text{Estimate} \pm \text{Critical Value} \times \text{Standard Error}$

**Common CIs**:

| Parameter | Distribution | CI Formula |
|-----------|--------------|------------|
| Mean ($\sigma$ known) | Normal | $\bar{x} \pm z_{\alpha/2} \frac{\sigma}{\sqrt{n}}$ |
| Mean ($\sigma$ unknown) | t | $\bar{x} \pm t_{\alpha/2, n-1} \frac{s}{\sqrt{n}}$ |
| Proportion | Normal approx | $\hat{p} \pm z_{\alpha/2} \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$ |
| Variance | $\chi^2$ | $\left[\frac{(n-1)s^2}{\chi^2_{\alpha/2}}, \frac{(n-1)s^2}{\chi^2_{1-\alpha/2}}\right]$ |

---

##### 3. Bootstrap Estimation (Resampling)

Non-parametric method when theoretical distribution unknown.

**Algorithm**:
1. Resample $n$ observations **with replacement** from original sample
2. Compute statistic $\hat{\theta}^*$ on bootstrap sample
3. Repeat $B$ times (e.g., $B=1000$)
4. Use bootstrap distribution for CI: percentile, BCa, or basic

---

##### Comparison of Estimation Methods

| Method | Assumptions | Output | Best For |
|--------|-------------|--------|----------|
| **MoM** | Low (moments exist) | Point | Simple distributions, starting values |
| **MLE** | Parametric form known | Point + CI (asymptotic) | Most parametric models |
| **Bayesian** | Prior + likelihood | Full posterior | Small data, uncertainty quant, prior info |
| **Bootstrap** | i.i.d. samples | Point + CI (non-parametric) | Complex statistics, no theory |
| **Least Squares** | Linear model | Point + CI | Regression |

---

## Question 3

### Q3(a) Explain Stochastic Processes with the help of an Example. [5]

---

#### Stochastic Process

**Definition**: A **stochastic process** (or random process) is a **collection of random variables** $\{X(t), t \in T\}$ indexed by a parameter $t$ (usually time).

- **State Space**: Set of possible values $S$ (discrete or continuous)
- **Index Set**: $T$ (discrete time $t=0,1,2,\dots$ or continuous $t \geq 0$)

---

#### Classification

| Classification | Discrete Time | Continuous Time |
|----------------|---------------|-----------------|
| **Discrete State** | Markov Chain, Random Walk | Poisson Process, Birth-Death Process |
| **Continuous State** | ARMA, ARIMA | Brownian Motion, Wiener Process |

---

#### Key Properties

| Property | Description |
|----------|-------------|
| **Stationarity** | Statistical properties don't change over time |
| **Markov Property** | Future depends only on present, not past |
| **Independent Increments** | Non-overlapping increments are independent |
| **Stationary Increments** | Distribution of increment depends only on length |

---

#### Example: Simple Random Walk (Discrete Time, Discrete State)

**Definition**: $X_0 = 0$, and for $n \geq 1$:
$$X_n = X_{n-1} + Z_n$$

where $Z_n \stackrel{\text{i.i.d.}}{\sim} \begin{cases} +1 & \text{with prob } p \\ -1 & \text{with prob } q=1-p \end{cases}$

**Interpretation**: Particle moves on integer line; at each step moves right (+1) with prob $p$, left (-1) with prob $q$.

**Properties**:
- $X_n \sim \text{Binomial}(n, p)$ shifted: $P(X_n = k) = \binom{n}{(n+k)/2} p^{(n+k)/2} q^{(n-k)/2}$
- $\mathbb{E}[X_n] = n(2p-1)$
- $\text{Var}(X_n) = 4npq$
- **Markov Property**: $P(X_{n+1} \mid X_n, X_{n-1}, \dots) = P(X_{n+1} \mid X_n)$

**Sample Path**:
```
n:    0  1  2  3  4  5  6  7  8  9  10
X_n:  0  1  2  1  2  3  2  1  0 -1  0
       ↗ ↗ ↘ ↗ ↗ ↘ ↘ ↘ ↘ ↗
```

---

#### Example: Poisson Process (Continuous Time, Discrete State)

**Definition**: Counting process $\{N(t), t \geq 0\}$ where:
- $N(0) = 0$
- Independent increments
- $N(t+s) - N(s) \sim \text{Poisson}(\lambda t)$

**Inter-arrival times**: $T_i \sim \text{Exponential}(\lambda)$

---

#### Example: Brownian Motion (Continuous Time, Continuous State)

**Definition**: $\{B(t), t \geq 0\}$ where:
- $B(0) = 0$
- Independent increments
- $B(t) - B(s) \sim \mathcal{N}(0, t-s)$ for $t > s$
- Continuous paths

**Application**: Stock prices (Geometric Brownian Motion), particle diffusion

---

### Q3(b) Calculate Pi Using Monte Carlo method. [5]

---

#### Monte Carlo Method for π

**Principle**: Use **random sampling** to estimate numerical results via geometric probability.

---

#### Geometric Setup

- Square of side 2: $x \in [-1, 1], y \in [-1, 1]$, Area = $4$
- Inscribed circle radius 1: $x^2 + y^2 \leq 1$, Area = $\pi$
- **Ratio**: $\frac{\text{Circle Area}}{\text{Square Area}} = \frac{\pi}{4}$

---

#### Algorithm

```
1. Generate N random points (x_i, y_i) uniformly in [-1, 1] × [-1, 1]
2. Count M = number of points with x_i² + y_i² ≤ 1 (inside circle)
3. Estimate: π ≈ 4 × (M / N)
4. Error decreases as O(1/√N)
```

---

#### Mathematical Derivation

Let $I_i = \mathbb{1}(X_i^2 + Y_i^2 \leq 1)$ be indicator for point $i$ inside circle.

$\mathbb{E}[I_i] = P(\text{inside}) = \frac{\pi}{4}$

By Law of Large Numbers: $\frac{1}{N}\sum_{i=1}^N I_i \xrightarrow{p} \frac{\pi}{4}$

Thus: $\hat{\pi} = 4 \times \frac{1}{N}\sum_{i=1}^N I_i$

---

#### Python Implementation

```python
import numpy as np

def estimate_pi_monte_carlo(N=1_000_000, seed=42):
    np.random.seed(seed)
    # Generate N random points in [-1, 1] x [-1, 1]
    x = np.random.uniform(-1, 1, N)
    y = np.random.uniform(-1, 1, N)
    
    # Check which points fall inside unit circle
    inside = (x**2 + y**2) <= 1
    M = np.sum(inside)
    
    # Estimate pi
    pi_estimate = 4 * M / N
    
    # Standard error
    p_hat = M / N
    se = 4 * np.sqrt(p_hat * (1 - p_hat) / N)
    
    return pi_estimate, se, M

# Run
pi_est, se, M = estimate_pi_monte_carlo(1_000_000)
print(f"N = 1,000,000, M = {M}")
print(f"π estimate = {pi_est:.6f}")
print(f"True π = {np.pi:.6f}")
print(f"Error = {abs(pi_est - np.pi):.6f}")
print(f"Std Error ≈ {se:.6f}")
print(f"95% CI: [{pi_est - 1.96*se:.6f}, {pi_est + 1.96*se:.6f}]")
```

**Typical Output**:
```
N = 1,000,000, M = 785398
π estimate = 3.141592
True π = 3.141593
Error = 0.000001
Std Error ≈ 0.001728
95% CI: [3.138204, 3.144980]
```

---

#### Convergence

```
Error = |π_est - π|
       │
  0.1 ┤ *
       │  *
  0.01 ┤   *
       │     *
  0.001 ┤       *
       │         *
       └─────────────→ N (log scale)
        100  1000  10000  100000
        Error ~ 1/√N
```

---

#### Variance Reduction Techniques

| Technique | Idea | Effect |
|-----------|------|--------|
| **Antithetic Variates** | Use $(x,y)$ and $(-x,-y)$ pairs | Reduces variance by ~2x |
| **Stratified Sampling** | Divide square into grid, sample each | More uniform coverage |
| **Quasi-Monte Carlo** | Low-discrepancy sequences (Sobol) | $O(1/N)$ vs $O(1/\sqrt{N})$ |

---

### Q3(c) Discuss type 1 and type 2 errors with an example. [5]

---

#### Hypothesis Testing Errors

| Decision \ Reality | $H_0$ True | $H_1$ True |
|--------------------|------------|------------|
| **Reject $H_0$** | **Type I Error** (False Positive) | **Correct** (Power) |
| **Fail to Reject $H_0$** | **Correct** | **Type II Error** (False Negative) |

---

#### Type I Error (α)

- **Definition**: Rejecting $H_0$ when $H_0$ is actually true
- **Symbol**: $\alpha$ (significance level)
- **Probability**: $P(\text{Reject } H_0 \mid H_0 \text{ true}) = \alpha$
- **Typical values**: 0.05, 0.01, 0.10
- **Also called**: False positive, Producer's risk

---

#### Type II Error (β)

- **Definition**: Failing to reject $H_0$ when $H_1$ is actually true
- **Symbol**: $\beta$
- **Probability**: $P(\text{Fail to reject } H_0 \mid H_1 \text{ true}) = \beta$
- **Power**: $1 - \beta = P(\text{Reject } H_0 \mid H_1 \text{ true})$
- **Also called**: False negative, Consumer's risk

---

#### Trade-off

- **Decreasing $\alpha$** → Increases $\beta$ (harder to reject, more false negatives)
- **Increasing $\alpha$** → Decreases $\beta$ (easier to reject, more false positives)
- **Increasing sample size $n$** → Decreases both $\alpha$ and $\beta$

---

#### Example: Medical Disease Testing

**Scenario**: Test for a disease.
- $H_0$: Patient is **healthy** (no disease)
- $H_1$: Patient **has disease**

| Test Result \ Truth | Healthy ($H_0$) | Diseased ($H_1$) |
|---------------------|-----------------|------------------|
| **Positive** (Reject $H_0$) | **Type I Error** (False Alarm) | **Correct** (True Positive) |
| **Negative** (Fail to Reject $H_0$) | **Correct** (True Negative) | **Type II Error** (Missed Disease) |

**Consequences**:
- **Type I (α)**: Healthy patient told they're sick → Anxiety, unnecessary treatment, cost
- **Type II (β)**: Sick patient told they're healthy → Disease progresses, potential death

**Which is worse?**
- For **serious diseases** (cancer, HIV): **Type II much worse** → Want high sensitivity (low β), accept higher α
- For **minor conditions** or **screening**: Balance both

---

#### Numerical Example

**Given**: Disease prevalence = 1%, Test sensitivity = 95%, Specificity = 90%

| | |
|---|---|
| **Sensitivity** = $P(\text{Positive} \mid \text{Diseased})$ = $1 - \beta$ = 0.95 |
| **Specificity** = $P(\text{Negative} \mid \text{Healthy})$ = $1 - \alpha$ = 0.90 |
| **Type I (α)** = 1 - Specificity = 0.10 |
| **Type II (β)** = 1 - Sensitivity = 0.05 |

**For 10,000 people**:
- Diseased: 100 (1%)
- Healthy: 9,900 (99%)

| Outcome | Count | Rate |
|---------|-------|------|
| True Positive | $100 \times 0.95 = 95$ | |
| False Negative (Type II) | $100 \times 0.05 = 5$ | β = 5% |
| True Negative | $9900 \times 0.90 = 8,910$ | |
| False Positive (Type I) | $9900 \times 0.10 = 990$ | α = 10% |

**PPV** = $\frac{95}{95+990} = 8.7\%$ (Low due to low prevalence!)

---

## Question 4

### Q4(a) Explain the steps of Hypothesis Testing. [5]

---

#### Hypothesis Testing Framework

**Goal**: Make decision about population parameter $\theta$ based on sample data.

---

#### Step-by-Step Procedure

```
┌─────────────────────────────────────────────────────────────┐
│ 1. STATE HYPOTHESES                                         │
│    H₀ (Null):    θ = θ₀        (status quo, no effect)      │
│    H₁ (Alternative): θ ≠ θ₀ / θ > θ₀ / θ < θ₀              │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. CHOOSE SIGNIFICANCE LEVEL α                              │
│    Common: 0.05, 0.01, 0.10                                 │
│    α = P(Type I Error) = P(Reject H₀ | H₀ true)             │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. SELECT TEST STATISTIC & SAMPLING DISTRIBUTION            │
│    Z-test (σ known, n large)  → N(0,1)                      │
│    t-test (σ unknown)         → t(n-1)                      │
│    χ²-test (variance)         → χ²(n-1)                     │
│    F-test (variances)         → F(df1, df2)                 │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│ 4. DETERMINE CRITICAL REGION / REJECTION REGION             │
│    Based on α and H₁ (one-tailed or two-tailed)             │
│    Critical value(s): z_α, t_α, χ²_α, etc.                  │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│ 5. COMPUTE TEST STATISTIC FROM SAMPLE DATA                  │
│    e.g., z = (x̄ - μ₀) / (σ/√n)                              │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│ 6. MAKE DECISION                                            │
│    If test stat in rejection region → REJECT H₀             │
│    Else → FAIL TO REJECT H₀                                 │
│    (Never "accept H₀" — insufficient evidence against)      │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│ 7. INTERPRET RESULT IN CONTEXT                              │
│    "There is sufficient evidence at α=0.05 to conclude..."  │
│    Report p-value if possible                               │
└─────────────────────────────────────────────────────────────┘
```

---

#### Detailed Steps

| Step                    | Action                                               | Detail                                                   |
| ----------------------- | ---------------------------------------------------- | -------------------------------------------------------- |
| **1. Hypotheses**       | $H_0$: Null (equality), $H_1$: Alternative (≠, >, <) | $H_0$ always has =; $H_1$ is research hypothesis         |
| **2. α Level**          | Probability of Type I error                          | Typically 0.05; lower for serious consequences           |
| **3. Test Statistic**   | Standardized measure                                 | $Z$, $t$, $\chi^2$, $F$ based on parameter & assumptions |
| **4. Rejection Region** | Values leading to $H_0$ rejection                    | Critical values from tables/software                     |
| **5. Compute**          | Plug in sample data                                  | $z = \frac{\bar{x} - \mu_0}{\sigma/\sqrt{n}}$            |
| **6. Decision**         | Compare to critical value                            | Reject $H_0$ if $z> z_{\alpha/2}$ (two-tailed)           |
| **7. Conclusion**       | State in problem context                             | Include practical significance, not just statistical     |

---

#### p-Value Approach (Alternative to Step 4-6)

**p-value** = $P(\text{Test Stat} \geq \text{observed} \mid H_0 \text{ true})$

- **Decision**: Reject $H_0$ if $p\text{-value} < \alpha$
- **Advantage**: Gives strength of evidence, not just binary decision

---

#### Types of Errors

| Error | Symbol | Definition | Control |
|-------|--------|------------|---------|
| **Type I** | $\alpha$ | Reject $H_0$ when $H_0$ true | Set $\alpha$ |
| **Type II** | $\beta$ | Fail to reject $H_0$ when $H_1$ true | Power = $1-\beta$ |
| **Power** | $1-\beta$ | P(Reject $H_0 \mid H_1$ true) | ↑ with $n$, effect size |

---

### Q4(b) Differentiate between T-Test, Z-Test and F-Test. [5]

---

#### Comparison Table

| Aspect | **Z-Test** | **T-Test** | **F-Test** |
|--------|------------|------------|------------|
| **Parameter Tested** | Mean ($\mu$) | Mean ($\mu$) | Variance ($\sigma^2$) or Multiple Means |
| **Population Variance** | **Known** ($\sigma^2$) | **Unknown** (estimated by $s^2$) | N/A (tests variances) |
| **Test Statistic** | $Z = \frac{\bar{x} - \mu_0}{\sigma/\sqrt{n}}$ | $t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}}$ | $F = \frac{s_1^2}{s_2^2}$ or $\frac{MS_{between}}{MS_{within}}$ |
| **Sampling Distribution** | Standard Normal $\mathcal{N}(0,1)$ | Student's $t$ with $df = n-1$ | F-distribution $F(df_1, df_2)$ |
| **Sample Size** | Large ($n \geq 30$) or any $n$ if $\sigma$ known | Small ($n < 30$) typically | Any (but needs normality) |
| **Critical Values** | $z_{\alpha/2}$ (e.g., 1.96) | $t_{\alpha/2, n-1}$ | $F_{\alpha, df_1, df_2}$ |
| **Tail Heaviness** | Light tails | Heavier tails | Right-skewed, positive only |
| **Degrees of Freedom** | Not applicable | $df = n-1$ (one sample) | $df_1, df_2$ (numerator, denominator) |

---

#### When to Use Which

```
                    ┌──────────────────────┐
                    │ What parameter?      │
                    └──────────┬───────────┘
                               │
              ┌────────────────┼────────────────┐
              ▼                ▼                ▼
         MEAN (μ)         MEAN (μ)         VARIANCE (σ²)
              │                │                │
              ▼                ▼                ▼
       ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
       │ σ KNOWN?    │  │ σ UNKNOWN?  │  │ Compare 2   │
       └──────┬──────┘  └──────┬──────┘  │ variances?  │
              │                │         └──────┬──────┘
       ┌──────┴──────┐        │                │
       ▼             ▼        ▼                ▼
    YES             NO       n≥30?           YES
       │             │        │              (F-test for
       ▼             ▼        ▼               2 variances)
  Z-TEST         Z-TEST    YES/NO          ANOVA
 (any n)       (CLT)       │                (F-test for
                            ▼                multiple means)
                       ┌─────────┐
                       │ T-TEST  │
                       └─────────┘
```

---

#### Detailed Test Types

**Z-Tests**:
- One-sample: $H_0: \mu = \mu_0$
- Two-sample: $H_0: \mu_1 = \mu_2$
- Proportion: $H_0: p = p_0$

**T-Tests**:
| Test | Purpose | Formula |
|------|---------|---------|
| **One-Sample** | $\mu = \mu_0$ | $t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}}$ |
| **Two-Sample (Independent)** | $\mu_1 = \mu_2$ | $t = \frac{\bar{x}_1 - \bar{x}_2}{s_p\sqrt{1/n_1 + 1/n_2}}$ |
| **Paired** | $\mu_d = 0$ | $t = \frac{\bar{d}}{s_d/\sqrt{n}}$ |
| **Welch's** | $\mu_1 = \mu_2$, unequal var | $t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{s_1^2/n_1 + s_2^2/n_2}}$ |

**F-Tests**:
| Test | Purpose | Formula |
|------|---------|---------|
| **Two Variances** | $\sigma_1^2 = \sigma_2^2$ | $F = \frac{s_1^2}{s_2^2}$ |
| **ANOVA (One-Way)** | $\mu_1 = \mu_2 = \dots = \mu_k$ | $F = \frac{MS_{between}}{MS_{within}}$ |
| **Regression** | Overall significance | $F = \frac{MSR}{MSE}$ |

---

#### Example Comparison

**Data**: Sample $n=15$, $\bar{x}=52$, $s=8$, Test $H_0: \mu=50$

**If $\sigma=8$ known (Z-test)**:
$$Z = \frac{52-50}{8/\sqrt{15}} = 0.968$$
Critical $z_{0.025} = 1.96$ → **Fail to reject** $H_0$

**If $\sigma$ unknown (T-test)**:
$$t = \frac{52-50}{8/\sqrt{15}} = 0.968$$
Critical $t_{0.025, 14} = 2.145$ → **Fail to reject** $H_0$

> T-test has **wider CI** and **larger p-value** (more conservative).

---

### Q4(c) Explain Transition State Diagram and Emission State Diagram of Hidden Markov Model with the help of example. [5]

---

#### Hidden Markov Model (HMM)

An HMM is a **statistical model** where the system is a **Markov process with unobserved (hidden) states**, each generating an **observation**.

**Components**:
- **Hidden States**: $S = \{s_1, s_2, \dots, s_N\}$ (not directly observable)
- **Observations**: $V = \{v_1, v_2, \dots, v_M\}$ (visible outputs)
- **Transition Matrix**: $A = [a_{ij}]$, $a_{ij} = P(s_j \mid s_i)$
- **Emission Matrix**: $B = [b_j(k)]$, $b_j(k) = P(v_k \mid s_j)$
- **Initial Distribution**: $\pi = [\pi_i]$, $\pi_i = P(s_i \text{ at } t=1)$

---

#### 1. Transition State Diagram

**Shows**: Probabilities of moving **between hidden states**.

```
        ┌─────────────┐
        │             ▼
    ┌───────┐   a₂₁  ┌───────┐
    │  S₁   ├────────►│  S₂   │
    └───┬───┘         └───┬───┘
        │ a₁₂         a₂₂ │
        │                 │
        ▼                 ▼
   (Loop a₁₁)         (Loop a₂₂)
```

**Matrix** (2 states):
$$A = \begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{bmatrix} = \begin{bmatrix} 0.7 & 0.3 \\ 0.4 & 0.6 \end{bmatrix}$$

- Rows sum to 1: $\sum_j a_{ij} = 1$

---

#### 2. Emission State Diagram

**Shows**: Probabilities of **observing symbols** from each hidden state.

```
         EMISSIONS from State S₁
    
    ┌──────────┐
    │   S₁     │
    └────┬─────┘
         │ b₁(v₁)=0.5
         ▼
      ┌─────┐
      │ v₁  │
      └─────┘
         │
         │ b₁(v₂)=0.3
         ▼
      ┌─────┐
      │ v₂  │
      └─────┘
         │
         │ b₁(v₃)=0.2
         ▼
      ┌─────┐
      │ v₃  │
      └─────┘
```

**Matrix** (2 states, 3 observations):
$$B = \begin{bmatrix} b_1(v_1) & b_1(v_2) & b_1(v_3) \\ b_2(v_1) & b_2(v_2) & b_2(v_3) \end{bmatrix} = \begin{bmatrix} 0.5 & 0.3 & 0.2 \\ 0.1 & 0.4 & 0.5 \end{bmatrix}$$

---

#### Combined Temporal Diagram

```
         TIME →
             
    t=1        t=2        t=3        t=4
    ▼          ▼          ▼          ▼
┌───────┐  ┌───────┐  ┌───────┐  ┌───────┐
│  S₁   │──►│  S₂   │──►│  S₁   │──►│  S₂   │  ← HIDDEN STATES
│ (0.7) │   │ (0.6) │   │ (0.7) │   │ (0.6) │
└───┬───┘   └───┬───┘   └───┬───┘   └───┬───┘
    │          │          │          │
    ▼          ▼          ▼          ▼
┌───────┐  ┌───────┐  ┌───────┐  ┌───────┐
│  v₂   │  │  v₃   │  │  v₁   │  │  v₃   │  ← OBSERVATIONS
│  0.3  │  │  0.5  │  │  0.5  │  │  0.5  │
└───────┘  └───────┘  └───────┘  └───────┘
```

---

#### Example: Weather & Umbrella

**Hidden States**: Weather $S = \{\text{Sunny}, \text{Rainy}\}$
**Observations**: Umbrella $V = \{\text{Yes}, \text{No}\}$

**Transition Matrix**:
| From \ To | Sunny | Rainy |
|-----------|-------|-------|
| **Sunny** | 0.8 | 0.2 |
| **Rainy** | 0.4 | 0.6 |

**Emission Matrix**:
| State | Umbrella=Yes | Umbrella=No |
|-------|--------------|-------------|
| **Sunny** | 0.1 | 0.9 |
| **Rainy** | 0.8 | 0.2 |

**Initial**: $\pi = [0.6, 0.4]$

---

#### Diagrams for Weather Example

**Transition Diagram**:
```
       0.8
  ┌─────────┐
  │         │
  ▼         │
┌──────┐   │
│Sunny │───┼──┐
└───┬───┘   │  │ 0.2
    │       │  │
    │ 0.4   │  │
    ▼       │  │
┌──────┐    │  │
│Rainy │◄───┘  │
└───┬───┘       │
    │           │
    │    0.6    │
    └───────────┘
```

**Emission Diagram**:
```
         Sunny                  Rainy
       ┌───────┐              ┌───────┐
       │       │              │       │
       │       │              │       │
       ▼       ▼              ▼       ▼
    ┌─────┐ ┌─────┐        ┌─────┐ ┌─────┐
    │ Yes │ │ No  │        │ Yes │ │ No  │
    │ 0.1 │ │ 0.9 │        │ 0.8 │ │ 0.2 │
    └─────┘ └─────┘        └─────┘ └─────┘
```

---

#### Three Fundamental Problems

| Problem | Question | Algorithm |
|---------|----------|-----------|
| **Evaluation** | $P(O \mid \lambda)$ | Forward / Backward |
| **Decoding** | $\arg\max_Q P(Q \mid O, \lambda)$ | Viterbi |
| **Learning** | $\arg\max_\lambda P(O \mid \lambda)$ | Baum-Welch (EM) |

---

#### Applications

- **Speech Recognition**: Phonemes (states) → Audio features (emissions)
- **POS Tagging**: POS tags (states) → Words (emissions)
- **Bioinformatics**: Gene regions (states) → DNA bases (emissions)
- **Finance**: Market regimes (states) → Returns (emissions)
- **Gesture Recognition**: Hand poses (states) → Sensor readings (emissions)

---

---

## Formula Sheet (DMV SEP24)

### Covariance & CLT
$$\text{Cov}(X,Y) = \frac{1}{n}\sum(x_i-\bar{x})(y_i-\bar{y}), \quad \rho = \frac{\text{Cov}}{\sigma_X\sigma_Y}$$
$$\bar{X}_n \xrightarrow{d} \mathcal{N}(\mu, \sigma^2/n), \quad Z = \frac{\bar{X}-\mu}{\sigma/\sqrt{n}} \sim \mathcal{N}(0,1)$$

### Discrete vs Continuous RV
- Discrete: PMF $P(X=x)$, sum for probability
- Continuous: PDF $f(x)$, integral for probability, $P(X=x)=0$

### Independent Variable Types
- Quantitative (Continuous/Discrete)
- Qualitative (Nominal/Ordinal/Binary)

### Data Modeling
- Conceptual (ER) → Logical (Normalized) → Physical (DDL)

### Chebyshev
$$P(|X-\mu| \geq k\sigma) \leq \frac{1}{k^2}$$

### Descriptive vs Graphical
- Descriptive: Numerical (mean, var, skew, corr)
- Graphical: Visual (histogram, boxplot, scatter, etc.)

### Estimation
- Point: MoM, MLE, Bayesian, Least Squares
- Interval: CI = Estimate ± Critical × SE
- Bootstrap: Resampling

### Stochastic Process
- $\{X(t), t \in T\}$ collection of RVs
- Random Walk: $X_n = X_{n-1} + Z_n$
- Poisson Process: $N(t) \sim \text{Poisson}(\lambda t)$
- Brownian Motion: $B(t) - B(s) \sim \mathcal{N}(0, t-s)$

### Monte Carlo π
$$\pi \approx 4 \times \frac{\text{# points in circle}}{\text{total points}}$$

### Hypothesis Testing Errors
- Type I (α): Reject $H_0$ when true
- Type II (β): Fail to reject $H_0$ when false
- Power = $1-\beta$

### Hypothesis Testing Steps
1. State $H_0, H_1$
2. Choose α
3. Select test statistic
4. Determine rejection region
5. Compute test statistic
6. Decide
7. Interpret

### Z vs T vs F
- Z: σ known, mean
- T: σ unknown, mean
- F: variances, ANOVA

### HMM
- Transition: $A = [a_{ij}]$, $a_{ij} = P(s_j \mid s_i)$
- Emission: $B = [b_j(k)]$, $b_j(k) = P(v_k \mid s_j)$
- Initial: $\pi_i = P(s_i \text{ at } t=1)$

---

## Tags
#SPPU #AIDS #SEM7 #DMV #DataModelingVisualization #InSem #SEP24 #ExamAnswers #Covariance #CentralLimitTheorem #DiscreteContinuousRV #IndependentVariables #DataModeling #ChebyshevInequality #DescriptiveStatistics #GraphicalStatistics #EstimationMethods #StochasticProcesses #MonteCarlo #Type1Type2Errors #HypothesisTesting #ZTestTTestFTest #HiddenMarkovModel