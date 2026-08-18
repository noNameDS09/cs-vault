---
tags: [statistics, gate-da, chi-square-test, hypothesis-testing, revision]
---

# 50 Chi Square Test

> [!note] Chi-square test uses chi-square distribution for categorical data analysis.

---

## Overview

The chi-square test is used for categorical data to test goodness of fit, independence, and homogeneity. It compares observed frequencies with expected frequencies under the null hypothesis.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **Chi-square distribution** | Distribution of sum of squared standard normals |
| **Goodness of Fit** | Test if sample follows a specified distribution |
| **Test of Independence** | Test if two categorical variables are independent |
| **Test of Homogeneity** | Test if distributions are same across groups |

---

## Formulae

### Chi-Square Test Statistic
$$\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}$$
where $O_i$ = observed frequency, $E_i$ = expected frequency

### Goodness of Fit
- $H_0$: Data follows specified distribution
- $E_i = n \times p_i$ (expected under $H_0$)
- $df = k - 1 - m$ where $k$ = categories, $m$ = estimated parameters
- $\chi^2 \sim \chi^2_{df}$

### Test of Independence (Contingency Table)
- $H_0$: Variables are independent
- $E_{ij} = \frac{R_i \times C_j}{N}$ (row total × column total / grand total)
- $df = (r-1)(c-1)$
- $\chi^2 = \sum \frac{(O_{ij} - E_{ij})^2}{E_{ij}}$

### Test of Homogeneity
- $H_0$: Distributions are identical across groups
- Same formula as independence test
- $df = (r-1)(c-1)$

### Variance Test (Normal Population)
$$\chi^2 = \frac{(n-1)s^2}{\sigma_0^2} \sim \chi^2_{n-1}$$
Tests $H_0: \sigma^2 = \sigma_0^2$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $O_i$ | Observed frequency |
| $E_i$ | Expected frequency |
| $df$ | Degrees of freedom |
| $\chi^2$ | Test statistic |

---

## Important Properties

### Chi-Square Distribution
- $\chi^2_{df}$ = sum of $df$ independent $Z^2$ where $Z \sim N(0,1)$
- Mean = $df$, Variance = $2df$
- Right-skewed, approaches normal for large $df$

### Assumptions
1. Data are counts/frequencies
2. Observations independent
3. Expected frequency $\geq 5$ (or combine categories)

---

## GATE Tricks

> [!tip>
> **$\chi^2 = \sum (O-E)^2/E$**
> **Goodness of fit**: df = k - 1 - m
> **Independence**: df = (r-1)(c-1)
> **Variance test**: $\chi^2 = (n-1)s^2/\sigma_0^2$
> **Expected freq $\geq 5$**: Combine categories if needed!

---

## Common Mistakes

> [!warning>
> **Using $\chi^2$ on continuous data**: Must be counts!
> **Expected freq < 5**: Invalid, combine categories!
> **df calculation**: k-1-m for GOF, (r-1)(c-1) for independence!
> **One-tailed**: $\chi^2$ test is always right-tailed!

---

## Memory Tricks

> [!tip>
> **Chi-square** = **Chi** = **X** = cross = compare observed vs expected
> **$(O-E)^2/E$** = squared difference over expected
> **Right-tailed only**: Large $\chi^2$ = reject

---

## Previous GATE Patterns

- **Goodness of fit**: Test if data fits Poisson/Normal/etc.
- **Independence**: 2×2 or r×c contingency table
- **Variance test**: $\chi^2 = (n-1)s^2/\sigma_0^2$
- **df calculation**: Correct formula

---

## Revision Summary

```
CHI-SQUARE TEST
├── $\chi^2 = \sum (O-E)^2/E$
├── Goodness of Fit: df = k-1-m
├── Independence: df = (r-1)(c-1)
├── Homogeneity: df = (r-1)(c-1)
├── Variance: $\chi^2 = (n-1)s^2/\sigma_0^2$, df = n-1
├── Always right-tailed
├── Expected $\geq 5$ (combine if needed)
└── Key: Compare observed vs expected frequencies!
```

---

## Related Notes

- [[43 Hypothesis Testing]]
- [[48 z Test]]
- [[49 t Test]]
- [[51 ANOVA]]
- [[GATE Numerical Tricks]]

---

#statistics #gate-da #chi-square-test #hypothesis-testing #revision