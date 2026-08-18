---
tags: [probability, statistics, gate-da, numerical-tricks, shortcuts, revision]
---

# GATE Numerical Tricks - Probability & Statistics

> [!tip] Collection of mental shortcuts, elimination techniques, and quick formulas for GATE DA numerical problems

---

## PROBABILITY SHORTCUTS

### Complement Rule
> [!tip]
> **Always check the complement first!** Often $P(A^c)$ is easier than $P(A)$.
> $$P(A) = 1 - P(A^c)$$
> **Example**: Probability of at least one success = $1 - P(\text{no successes})$

### Union of Events
> [!tip]
> **Inclusion-Exclusion**: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
> - If mutually exclusive: just add
> - If independent: $P(A \cup B) = P(A) + P(B) - P(A)P(B)$

### Bayes Theorem - Quick Pattern
> [!tip]
> **Posterior = Prior × Likelihood / Evidence**
> $$P(B_i|A) = \frac{P(A|B_i)P(B_i)}{\sum P(A|B_j)P(B_j)}$$
> **Mental model**: Draw a tree diagram - multiply along branches, sum at root.

### Odds Form of Bayes
> [!tip]
> **Posterior Odds = Prior Odds × Likelihood Ratio**
> $$\frac{P(H|D)}{P(H^c|D)} = \frac{P(H)}{P(H^c)} \times \frac{P(D|H)}{P(D|H^c)}$$
> - Very fast for binary hypothesis problems

---

## COUNTING SHORTCUTS

### Stars and Bars (Identical Objects)
> [!tip]
> **Distributing $n$ identical items into $k$ distinct boxes**:
> - No restrictions: $\binom{n+k-1}{k-1}$
> - At least 1 per box: $\binom{n-1}{k-1}$

### Arrangements with Repetitions
> [!tip]
> **Word with repeated letters**: $\frac{n!}{n_1! n_2! ... n_k!}$

### Circular Arrangements
> [!tip]
> **$n$ distinct objects around a circle**: $(n-1)!$
> - If reflections are same (necklace): $\frac{(n-1)!}{2}$

### Complementary Counting
> [!tip]
> **"At least one" problems**: Total - None
> - At least one head in $n$ coin tosses: $2^n - 1$
> - At least one pair adjacent: Total arrangements - No pairs adjacent

### Gap Method (No Adjacent)
> [!tip]
> **Arrange $k$ items with no two adjacent among $n$ total**:
> 1. Arrange the other $n-k$ items first
> 2. Choose $k$ gaps from $n-k+1$ gaps: $\binom{n-k+1}{k}$

---

## EXPECTATION & VARIANCE TRICKS

### Linearity of Expectation (ALWAYS works!)
> [!tip]
> **$E[X+Y] = E[X] + E[Y]$** even if $X,Y$ are DEPENDENT!
> - Sum of indicators: $E[\text{# events}] = \sum P(\text{each event})$
> - No independence needed!

### Variance Formula
> [!tip]
> **$Var(X) = E[X^2] - (E[X])^2$** - Often easier than $E[(X-\mu)^2]$
> - Compute $E[X^2]$ directly from distribution

### Linear Transformation
> [!tip]
> **$E[aX+b] = aE[X] + b$**
> **$Var(aX+b) = a^2 Var(X)$**
> - Adding constant changes mean but NOT variance
> - Multiplying by $a$ scales variance by $a^2$

### Sum of Independent Variables
> [!tip]
> **$Var(X+Y) = Var(X) + Var(Y)$** if independent
> - For $n$ i.i.d. variables: $Var(\sum X_i) = n Var(X)$
> - $Var(\bar{X}) = \frac{Var(X)}{n}$

### Covariance Shortcut
> [!tip]
> **$Cov(X,Y) = E[XY] - E[X]E[Y]$**
> - If independent: $Cov = 0$ (but converse NOT always true!)
> - $Cov(X,X) = Var(X)$

### Correlation from Covariance
> [!tip]
> **$\rho = \frac{Cov(X,Y)}{\sigma_X \sigma_Y}$**
> - Always between -1 and 1
> - $\rho = \pm 1$ iff perfect linear relationship

---

## DISCRETE DISTRIBUTIONS - QUICK RECALL

### Bernoulli(p)
> [!tip]
> - Mean = $p$, Variance = $p(1-p) = pq$
> - $E[X^k] = p$ for any $k \geq 1$

### Binomial(n, p)
> [!tip]
> - Mean = $np$, Variance = $npq$
> - Sum of $n$ Bernoullis
> - Mode ≈ $\lfloor (n+1)p \rfloor$
> - If $np$ and $nq$ both > 5, approx normal with $\mu=np, \sigma^2=npq$

### Geometric(p) - Trials until first success
> [!tip]
> - $P(X=k) = (1-p)^{k-1}p$
> - Mean = $\frac{1}{p}$, Variance = $\frac{q}{p^2}$
> - Memoryless: $P(X > m+n | X > m) = P(X > n)$

### Poisson(λ)
> [!tip]
> - Mean = $\lambda$, Variance = $\lambda$ ⭐ **MEMORIZE THIS!**
> - $P(X=0) = e^{-\lambda}$, $P(X=1) = \lambda e^{-\lambda}$
> - Sum of independent Poissons: $Poisson(\lambda_1 + \lambda_2)$
> - Binomial approx: $n$ large, $p$ small, $np = \lambda$

---

## CONTINUOUS DISTRIBUTIONS - QUICK RECALL

### Uniform(a, b)
> [!tip]
> - Mean = $\frac{a+b}{2}$ (midpoint)
> - Variance = $\frac{(b-a)^2}{12}$
> - $P(X \leq x) = \frac{x-a}{b-a}$ for $a \leq x \leq b$

### Exponential(λ)
> [!tip]
> - Mean = $\frac{1}{\lambda}$, Variance = $\frac{1}{\lambda^2}$
> - $P(X > x) = e^{-\lambda x}$ (survival function)
> - Memoryless: only continuous distribution with this property
> - Related to Poisson: time between events ~ Exp(λ) if events ~ Poisson(λ)

### Normal(μ, σ²)
> [!tip]
> - Standardize: $Z = \frac{X-\mu}{\sigma}$
> - $P(X \leq x) = P(Z \leq \frac{x-\mu}{\sigma})$
> - Empirical rule: 68-95-99.7 within 1,2,3 $\sigma$

### Standard Normal - Key Percentiles
> [!tip]
> | z-value | Two-tail α | One-tail α |
> |---------|------------|------------|
> | 1.645   | 0.10       | 0.05       |
> | 1.96    | 0.05       | 0.025      |
> | 2.326   | 0.02       | 0.01       |
> | 2.576   | 0.01       | 0.005      |

---

## NORMAL DISTRIBUTION - MENTAL MATH

### Quick Standardization
> [!tip]
> **$Z = \frac{X - \mu}{\sigma}$**
> - If $X \sim N(10, 4)$ and $X=14$: $Z = \frac{14-10}{2} = 2$

### Symmetry Tricks
> [!tip]
> - $P(Z > z) = P(Z < -z) = 1 - \Phi(z)$
> - $P(|Z| < z) = 2\Phi(z) - 1$
> - $P(a < Z < b) = \Phi(b) - \Phi(a)$

### Common Probabilities to Memorize
> [!tip]
> - $P(|Z| < 1) \approx 0.68$
> - $P(|Z| < 2) \approx 0.95$
> - $P(|Z| < 3) \approx 0.997$
> - $P(Z > 1.645) = 0.05$
> - $P(Z > 1.96) = 0.025$
> - $P(Z > 2.576) = 0.005$

---

## CENTRAL LIMIT THEOREM - QUICK APPLICATION

### Sample Mean Distribution
> [!tip]
> **$\bar{X} \sim N(\mu, \frac{\sigma^2}{n})$** for large $n$ (usually $n \geq 30$)
> - Standardize: $Z = \frac{\bar{X} - \mu}{\sigma/\sqrt{n}}$
> - **Standard Error = $\frac{\sigma}{\sqrt{n}}$** - NOT $\frac{\sigma}{n}$!

### When to Use CLT vs t-distribution
> [!tip]
> | Situation | Use |
> |-----------|-----|
> | $\sigma$ known, any $n$ | z-test |
> | $\sigma$ unknown, $n \geq 30$ | z-test (approx) |
> | $\sigma$ unknown, $n < 30$, normal pop | t-test |
> | $\sigma$ unknown, $n < 30$, not normal | Non-parametric |

---

## MLE - QUICK PATTERNS

### Common MLEs (MEMORIZE)
> [!tip]
> | Distribution | MLE |
> |--------------|-----|
> | Bernoulli($p$) | $\hat{p} = \bar{x}$ |
> | Binomial($n,p$) | $\hat{p} = \bar{x}/n$ |
> | Poisson($\lambda$) | $\hat{\lambda} = \bar{x}$ |
> | Normal($\mu,\sigma^2$) | $\hat{\mu} = \bar{x}$, $\hat{\sigma}^2 = \frac{1}{n}\sum(x_i-\bar{x})^2$ |
> | Exponential($\lambda$) | $\hat{\lambda} = 1/\bar{x}$ |

### MLE Steps (Memorize)
```
1. Write likelihood L(θ) = ∏ f(x_i; θ)
2. Take log: ℓ(θ) = ∑ log f(x_i; θ)
3. Differentiate: dℓ/dθ = 0
4. Solve for θ̂
5. Check boundary/second derivative
```

---

## HYPOTHESIS TESTING - QUICK DECISION

### p-Value Rule
> [!tip]
> **If p-value < α → Reject H₀**
> **If p-value ≥ α → Fail to reject H₀**
> - p-value = probability of observing data as extreme as (or more than) observed, assuming H₀ true

### Test Statistic Pattern
> [!tip]
> **Test Stat = $\frac{\text{Estimate} - \text{Hypothesized Value}}{\text{Standard Error}}$**
> - z = $\frac{\bar{x} - \mu_0}{\sigma/\sqrt{n}}$
> - t = $\frac{\bar{x} - \mu_0}{s/\sqrt{n}}$
> - z (proportion) = $\frac{\hat{p} - p_0}{\sqrt{p_0(1-p_0)/n}}$

### Two-Tailed vs One-Tailed
> [!tip]
> - Two-tailed: H₁: μ ≠ μ₀ → rejection region in BOTH tails
> - One-tailed: H₁: μ > μ₀ or μ < μ₀ → rejection in ONE tail
> - For two-tailed: compare |test stat| with $z_{\alpha/2}$ or $t_{\alpha/2}$

---

## CONFIDENCE INTERVALS - QUICK FORMULAS

### Mean (σ known)
> [!tip]
> $\bar{x} \pm z_{\alpha/2} \frac{\sigma}{\sqrt{n}}$

### Mean (σ unknown, n large)
> [!tip]
> $\bar{x} \pm z_{\alpha/2} \frac{s}{\sqrt{n}}$

### Mean (σ unknown, n small, normal)
> [!tip]
> $\bar{x} \pm t_{\alpha/2, n-1} \frac{s}{\sqrt{n}}$

### Proportion
> [!tip]
> $\hat{p} \pm z_{\alpha/2} \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$

### Variance
> [!tip]
> $\left(\frac{(n-1)s^2}{\chi^2_{\alpha/2}}, \frac{(n-1)s^2}{\chi^2_{1-\alpha/2}}\right)$

---

## PROBABILITY INEQUALITIES - BOUNDS

### Markov (X ≥ 0)
> [!tip]
> $P(X \geq a) \leq \frac{E[X]}{a}$
> - Only needs $E[X]$ and $X \geq 0$

### Chebyshev (Any distribution with finite variance)
> [!tip]
> $P(|X - \mu| \geq k\sigma) \leq \frac{1}{k^2}$
> - Equivalently: $P(|X - \mu| < k\sigma) \geq 1 - \frac{1}{k^2}$
> - For $k=2$: at least 75% within 2$\sigma$
> - For $k=3$: at least 88.9% within 3$\sigma$

---

## ELIMINATION TRICKS FOR MCQ

### Probability Range Check
> [!tip]
> - All probabilities must be between 0 and 1
> - Variances must be ≥ 0
> - Standard deviations must be ≥ 0
> - Correlation must be in [-1, 1]

### Dimensional Analysis
> [!tip]
> - Mean has units of X
> - Variance has units of X²
> - Standard deviation has units of X
> - Correlation is unitless
> - Covariance has units of X × Y

### Symmetry Checks
> [!tip]
> - Normal distribution is symmetric about mean
> - If problem gives $P(X < \mu - a) = p$, then $P(X > \mu + a) = p$
> - $P(X < \mu) = 0.5$ for symmetric continuous distributions

### Special Values
> [!tip]
> - For Uniform(0,1): $E[X] = 0.5$, $Var(X) = 1/12 \approx 0.083$
> - For Exponential(1): $E[X] = 1$, $Var(X) = 1$
> - For Poisson(1): $E[X] = 1$, $Var(X) = 1$

---

## MENTAL ARITHMETIC

### Common Fractions
> [!tip]
> | Fraction | Decimal | Percentage |
> |----------|---------|------------|
> | 1/3      | 0.333   | 33.3%      |
> | 1/6      | 0.167   | 16.7%      |
> | 1/12     | 0.0833  | 8.33%      |
> | 1/√2π    | 0.399   | -          |
> | 1/√2     | 0.707   | -          |

### Quick Square Roots
> [!tip]
> - $\sqrt{2} \approx 1.414$
> - $\sqrt{3} \approx 1.732$
> - $\sqrt{5} \approx 2.236$
> - $\sqrt{10} \approx 3.162$
> - $\sqrt{2\pi} \approx 2.507$

### Log Values
> [!tip]
> - $\ln(2) \approx 0.693$
> - $\ln(10) \approx 2.303$
> - $\log_{10}(e) \approx 0.434$
> - $\ln(0.05) \approx -3$
> - $\ln(0.01) \approx -4.6$

---

## DISTRIBUTION RECOGNITION

### When to Use Which Distribution
> [!tip]
> | Scenario | Distribution |
> |----------|--------------|
> | Success/failure, n trials | Binomial |
> | Trials until first success | Geometric |
> | Count events in interval | Poisson |
> | Time between events | Exponential |
> | Measurements/heights/errors | Normal |
> | All outcomes equally likely | Uniform |
> | Proportions/percentages | Beta (Bayesian) |

### Binomial vs Poisson
> [!tip]
> - Binomial: fixed n, each trial has p
> - Poisson: rate λ over interval, no fixed n
> - If n large, p small, np = λ → Poisson approx

---

## COMMON GATE PATTERNS

### Pattern 1: "At Least One"
> [!tip]
> Use complement: $1 - P(\text{none})$

### Pattern 2: Conditional Probability with Numbers
> [!tip]
> Draw 2×2 table or tree diagram. Fill in numbers, compute ratios.

### Pattern 3: Sum of Independent RVs
> [!tip]
> $E[\sum X_i] = \sum E[X_i]$
> $Var(\sum X_i) = \sum Var(X_i)$ (if independent)

### Pattern 4: Sample Mean Questions
> [!tip]
> Standardize: $Z = \frac{\bar{x} - \mu}{\sigma/\sqrt{n}}$
> **Don't forget the $\sqrt{n}$ in denominator!**

### Pattern 5: MLE for Exponential/Normal
> [!tip]
> Exponential: $\hat{\lambda} = \frac{1}{\bar{x}}$
> Normal: $\hat{\mu} = \bar{x}$, $\hat{\sigma}^2 = \frac{1}{n}\sum(x_i-\bar{x})^2$

### Pattern 6: Hypothesis Test from CI
> [!tip]
> If $(1-\alpha)$ CI doesn't contain $\mu_0$ → reject $H_0$ at level $\alpha$

---

## RELATED NOTES

- [[Formula Sheet]]
- [[Glossary]]
- [[05 Conditional Probability]]
- [[06 Bayes Theorem]]
- [[14 Expectation]]
- [[15 Variance and Standard Deviation]]
- [[23 Important Discrete Distributions]]
- [[28 Important Continuous Distributions]]
- [[33 Central Limit Theorem]]
- [[43 Hypothesis Testing]]
- [[47 Confidence Intervals]]

---

#probability #statistics #gate-da #numerical-tricks #shortcuts #revision