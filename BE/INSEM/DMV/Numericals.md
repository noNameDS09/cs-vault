# **20 students are selected at random. Find the probability that mean GPA is more than 5. Given mean=4.91 and SD=0.72**

Assuming the **population is approximately normal** (or $n=20$ is large enough for the CLT):

Given:

- Population mean: $\mu = 4.91$
    
- Population SD: $\sigma = 0.72$
    
- Sample size: $n=20$
    
- Find: $P(\bar X > 5)$
    

### 1. Find the standard error

$SE=\frac{\sigma}{\sqrt n}$

$=\frac{0.72}{\sqrt{20}}$

$\approx 0.161$

### 2. Convert 5 to a Z-score

$Z=\frac{\bar X-\mu}{SE}$

$=\frac{5-4.91}{0.161}$

$\approx 0.559$

### 3. Find the probability

We want:

$P(\bar X>5)=P(Z>0.559)$

From the standard normal table:

$P(Z<0.559)\approx0.712$

Therefore:

$P(Z>0.559)=1-0.712$

$\boxed{P(\bar X>5)\approx0.288}$

### Answer

$\boxed{\text{Probability} \approx 28.8\%}$

So there is about a **29% chance** that the mean GPA of 20 randomly selected students is greater than 5.

---
