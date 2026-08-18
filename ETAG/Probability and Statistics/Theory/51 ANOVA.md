---
tags: [statistics, gate-da, anova, hypothesis-testing, revision]
---

# 51 ANOVA (Analysis of Variance)

> [!note] ANOVA compares means of three or more groups by analyzing variance components.

---

## Overview

ANOVA (Analysis of Variance) tests whether there are significant differences between the means of three or more groups by comparing between-group variance to within-group variance.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **One-Way ANOVA** | Compare means of $k$ independent groups |
| **Factor** | Independent variable (grouping variable) |
| **Levels** | Categories of the factor |
| **Between-Group Variance** | Variance due to group differences |
| **Within-Group Variance** | Variance due to random error |

---

## Formulae

### One-Way ANOVA

**Total Sum of Squares:**
$$SS_{Total} = \sum_{i=1}^k \sum_{j=1}^{n_i} (y_{ij} - \bar{\bar{y}})^2$$

**Between-Group Sum of Squares:**
$$SS_{Between} = \sum_{i=1}^k n_i (\bar{y}_i - \bar{\bar{y}})^2$$

**Within-Group Sum of Squares:**
$$SS_{Within} = \sum_{i=1}^k \sum_{j=1}^{n_i} (y_{ij} - \bar{y}_i)^2$$

**Relationship:**
$$SS_{Total} = SS_{Between} + SS_{Within}$$

### Mean Squares
$$MS_{Between} = \frac{SS_{Between}}{k-1}$$
$$MS_{Within} = \frac{SS_{Within}}{N-k}$$

### F-Statistic
$$F = \frac{MS_{Between}}{MS_{Within}} \sim F_{k-1, N-k}$$

### ANOVA Table
| Source | SS | df | MS | F |
|--------|----|----|----|---|
| Between | $SS_B$ | $k-1$ | $MS_B = SS_B/(k-1)$ | $MS_B/MS_W$ |
| Within | $SS_W$ | $N-k$ | $MS_W = SS_W/(N-k)$ | |
| Total | $SS_T$ | $N-1$ | | |

### Assumptions
1. Independence of observations
2. Normality within each group
3. Homogeneity of variances (homoscedasticity)

### Post-hoc Tests
If ANOVA significant, use pairwise comparisons:
- Tukey's HSD
- Bonferroni correction
- Scheffé's method

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $k$ | Number of groups |
| $n_i$ | Sample size of group $i$ |
| $N$ | Total sample size |
| $\bar{y}_i$ | Mean of group $i$ |
| $\bar{\bar{y}}$ | Grand mean |

---

## GATE Tricks

> [!tip>
> **ANOVA**: Compare $k \geq 3$ means
> **F = MS_Between / MS_Within**
> **df**: $k-1$ (between), $N-k$ (within)
> **Total SS** = Between SS + Within SS
> **Assumptions**: Normal, equal variances, independent

---

## Common Mistakes

> [!warning>
> **ANOVA only tells if ANY difference exists**: Need post-hoc for which groups!
> **Equal variance assumption**: Check with Levene's test
> **Multiple t-tests**: Increases Type I error! Use ANOVA first.
> **F is always right-tailed**: Large F = reject

---

## Memory Tricks

> [!tip>
> **ANOVA** = **AN**alysis **O**f **VA**riance
> **Between** = **B**etween groups
> **Within** = **W**ithin groups
> **F** = **F**isher = ratio of variances

---

## Previous GATE Patterns

- **Complete ANOVA table**: Fill missing values
- **Compute F**: Given SS and df
- **Interpretation**: Significant F → at least one group differs
- **Assumptions**: Normality, homogeneity of variances

---

## Revision Summary

```
ANOVA (One-Way)
├── Compare $k \geq 3$ group means
├── SS_Total = SS_Between + SS_Within
├── MS_Between = SS_Between / (k-1)
├── MS_Within = SS_Within / (N-k)
├── F = MS_Between / MS_Within ~ F_{k-1, N-k}
├── Assumptions: Normal, Equal variances, Independent
├── If significant → Post-hoc tests
└── Key: F = Between variance / Within variance
```

---

## Related Notes

- [[43 Hypothesis Testing]]
- [[48 z Test]]
- [[49 t Test]]
- [[50 Chi Square Test]]
- [[GATE Numerical Tricks]]

---

#statistics #gate-da #anova #hypothesis-testing #revision