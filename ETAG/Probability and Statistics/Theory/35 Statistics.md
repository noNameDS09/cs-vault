---
tags: [statistics, gate-da, overview, revision]
---

# 35 Statistics

> [!note] Statistics is the science of collecting, analyzing, interpreting, and presenting data.

---

## Overview

Statistics provides methods for drawing conclusions about populations from samples. It has two main branches: **Descriptive Statistics** (summarizing data) and **Inferential Statistics** (making predictions/generalizations about populations).

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **Population** | Complete set of all items of interest |
| **Sample** | Subset of population selected for study |
| **Parameter** | Numerical characteristic of population |
| **Statistic** | Numerical characteristic of sample |
| **Descriptive Statistics** | Summarize and describe data |
| **Inferential Statistics** | Draw conclusions about population from sample |

---

## Formulae

### Types of Statistics
| Branch | Purpose |
|--------|---------|
| Descriptive | Summarize, visualize, describe |
| Inferential | Estimate, test hypotheses, predict |

### Key Distinctions
| Population | Sample |
|------------|--------|
| Size $N$ | Size $n$ |
| Parameters: $\mu, \sigma^2, p$ | Statistics: $\bar{x}, s^2, \hat{p}$ |
| Usually unknown | Used to estimate population |

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $N$ | Population size |
| $n$ | Sample size |
| $\mu, \sigma^2$ | Population parameters |
| $\bar{x}, s^2$ | Sample statistics |

---

## Important Properties

### Data Types
| Type | Examples | Analysis Methods |
|------|----------|------------------|
| **Nominal** | Categories (gender, color) | Mode, chi-square |
| **Ordinal** | Rankings (low/med/high) | Median, percentiles |
| **Interval** | Temperature (Celsius) | Mean, SD, correlation |
| **Ratio** | Height, weight, time | All parametric tests |

---

## Mathematical Intuition

**Statistics = Data + Uncertainty**: We observe a sample, but want to infer about the population. Probability quantifies the uncertainty.

**Inference Loop**:
1. Model: Assume probability distribution
2. Data: Collect sample
3. Estimate: Compute statistics
4. Inference: Confidence intervals, hypothesis tests
5. Validate: Check assumptions, residuals

---

## Algorithms / Problem-Solving

### Statistical Analysis Pipeline
```
1. Define research question
2. Design study (sampling, experiment)
3. Collect data
4. Explore data (descriptive stats, plots)
5. Choose statistical method
6. Check assumptions
6. Perform inference (estimates, tests)
7. Interpret results
8. Communicate findings
```

---

## Complexity
Not applicable.

---

## GATE Tricks

> [!tip>
> **Statistics = Descriptive + Inferential**
> **Parameter = Population** (Greek letters: $\mu, \sigma, p$)
> **Statistic = Sample** (Latin/English letters: $\bar{x}, s, \hat{p}$)
> **Descriptive** = What does the data look like?
> **Inferential** = What does the data tell us about the population?

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| Parameter | Statistic | Population vs Sample |
| Descriptive | Inferential | Describe vs Generalize |
| Population | Sample | All vs Subset |
| Census | Sample survey | All units vs subset |

---

## Common Mistakes

> [!warning>
> **Confusing parameter and statistic**: $\mu$ vs $\bar{x}$
> **Generalizing beyond population**: Sample only represents population it was drawn from
> **Ignoring sampling bias**: Non-random samples don't represent population

---

## Memory Tricks

> [!tip>
> **Parameter** = **P**opulation = **P**ermanent = Greek ($\mu, \sigma$)
> **Statistic** = **S**ample = **S**ummary = Latin ($\bar{x}, s$)
> **Descriptive** = **D**escribe = what data shows
> **Inferential** = **Inf**er = what we learn about population

---

## Previous GATE Patterns

- **Identify parameter vs statistic**
- **Descriptive vs inferential classification**
- **Data type classification** (nominal/ordinal/interval/ratio)

---

## Revision Summary

```
STATISTICS OVERVIEW
├── Descriptive: Summarize data (mean, median, SD, plots)
├── Inferential: Generalize to population (estimation, testing)
├── Parameter (μ,σ) = Population characteristic
├── Statistic (x̄,s) = Sample characteristic
├── Data types: Nominal, Ordinal, Interval, Ratio
└── Key: Sample → Statistic → Parameter → Population
```

---

## Related Notes

- [[36 Population and Sample]]
- [[37 Sampling Techniques]]
- [[38 Sampling Distribution]]
- [[39 Point Estimation]]
- [[43 Hypothesis Testing]]
- [[52 Descriptive Statistics]]
- [[GATE Numerical Tricks]]

---

#statistics #gate-da #overview #revision