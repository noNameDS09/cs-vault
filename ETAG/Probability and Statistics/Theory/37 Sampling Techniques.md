---
tags: [statistics, gate-da, sampling, revision]
---

# 37 Sampling Techniques

> [!note] Methods for selecting a representative subset from a population.

---

## Overview

Sampling techniques determine how we select a sample from a population. The goal is to obtain a representative sample that allows valid statistical inference.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **Sampling Frame** | List of all population units |
| **Probability Sampling** | Each unit has known, non-zero probability of selection |
| **Non-probability Sampling** | Selection based on convenience/judgment |
| **Sampling Bias** | Systematic error from non-representative sample |

---

## Formulae

### Sample Size for Proportion
$$n = \frac{z_{\alpha/2}^2 \cdot p(1-p)}{E^2}$$
where $E$ = margin of error

### Sample Size for Mean
$$n = \left(\frac{z_{\alpha/2} \cdot \sigma}{E}\right)^2$$

### Finite Population Correction
$$n_{adj} = \frac{n}{1 + \frac{n-1}{N}}$$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $n$ | Sample size |
| $N$ | Population size |
| $E$ | Margin of error |
| $p$ | Estimated proportion |

---

## Important Properties

### Probability Sampling Methods

| Method | Description | Advantages |
|--------|-------------|------------|
| **Simple Random** | Each unit equally likely | Unbiased, simple |
| **Stratified** | Divide into strata, sample from each | Precision, representation |
| **Systematic** | Every $k$-th unit | Easy, spread |
| **Cluster** | Random clusters, sample all in cluster | Cost-effective |
| **Multistage** | Multiple stages of clustering | Large populations |

### Non-probability Sampling
- **Convenience**: Easy to reach units
- **Quota**: Fill quotas for subgroups
- **Judgmental**: Expert selects units
- **Snowball**: Existing subjects recruit others

---

## GATE Tricks

> [!tip>
> **Simple Random**: Gold standard for unbiasedness
> **Stratified**: Reduces variance when strata are homogeneous
> **Cluster**: Cost-effective for geographically dispersed populations
> **Systematic**: Every k-th, but risk of periodicity bias

---

## Common Mistakes

> [!warning>
> **Convenience sampling**: Not representative!
> **Voluntary response**: Self-selection bias
> **Undercoverage**: Missing parts of population

---

## Memory Tricks

> [!tip>
> **SRS** = **S**imple **R**andom **S**ampling = everyone equal chance
> **Stratified** = **Stra**ta = layers = subgroups
> **Cluster** = **Clus**ter = groups = areas

---

## Previous GATE Patterns

- **Identify sampling method**: From description
- **Sample size calculation**: Given margin of error, confidence
- **Bias identification**: What bias in given design?

---

## Revision Summary

```
SAMPLING TECHNIQUES
├── Probability sampling (random): SRS, Stratified, Systematic, Cluster
├── Non-probability: Convenience, Quota, Judgment, Snowball
├── SRS: Each unit equal probability
├── Stratified: Homogeneous strata, sample each
├── Cluster: Random clusters, all units in selected clusters
├── Sample size: n = (z*σ/E)² for mean, n = z²p(1-p)/E² for proportion
└── Key: Probability sampling = unbiased inference!
```

---

## Related Notes

- [[36 Population and Sample]]
- [[38 Sampling Distribution]]
- [[39 Point Estimation]]
- [[47 Confidence Intervals]]
- [[GATE Numerical Tricks]]

---

#statistics #gate-da #sampling #revision