# GATE DA — Linear Regression: Slope ($m$) & Intercept ($c$)

For **simple linear regression**, write:

$$  
\boxed{\hat y = mx+c}  
$$

where:

- $m$ = slope
    
- $c$ = intercept
    

---

## 1. Most Important GATE Formulas

Given observations:

$$  
(x_1,y_1),(x_2,y_2),\ldots,(x_n,y_n)  
$$

Define the means:

$$  
\bar x=\frac{1}{n}\sum x_i  
$$

$$  
\bar y=\frac{1}{n}\sum y_i  
$$

### Regression Slope

$$  
\boxed{  
m=  
\frac{\sum (x_i-\bar x)(y_i-\bar y)}  
{\sum (x_i-\bar x)^2}  
}  
$$

### Intercept

$$  
\boxed{  
c=\bar y-m\bar x  
}  
$$

### Shortcut Formula for Slope

$$  
\boxed{  
m=  
\frac{  
n\sum xy-(\sum x)(\sum y)  
}{  
n\sum x^2-(\sum x)^2  
}  
}  
$$

### ⭐ GATE Shortcut

Remember:

$$  
\boxed{  
m=\frac{\operatorname{Cov}(X,Y)}  
{\operatorname{Var}(X)}  
}  
$$

and

$$  
\boxed{  
c=\bar Y-m\bar X  
}  
$$

---

# 2. Type 1 — Two Points Are Given

If there are only two points, regression is simply the line passing through those points.

Suppose:

$$  
(1,3),\quad(3,7)  
$$

Slope:

$$  
m=\frac{7-3}{3-1}=2  
$$

Intercept:

$$  
c=3-(2)(1)=1  
$$

Therefore:

$$  
\boxed{\hat y=2x+1}  
$$

### ⚠️ GATE Trap

Do **not** confuse regression slope with $y/x$.

Slope is:

$$  
\boxed{  
m=\frac{\Delta y}{\Delta x}  
}  
$$

---

# 3. Type 2 — Small Dataset

Suppose:

|$x$|$y$|
|--:|--:|
|1|2|
|2|3|
|3|5|

First calculate the means:

$$  
\bar x=2  
$$

$$  
\bar y=\frac{2+3+5}{3}=\frac{10}{3}  
$$

Now:

$$  
m=  
\frac{  
(1-2)(2-\frac{10}{3})  
+(2-2)(3-\frac{10}{3})  
+(3-2)(5-\frac{10}{3})  
}{  
(1-2)^2+(2-2)^2+(3-2)^2  
}  
$$

Numerator:

$$  
\frac{4}{3}+0+\frac{5}{3}=3  
$$

Denominator:

$$  
1+0+1=2  
$$

Therefore:

$$  
\boxed{m=\frac{3}{2}}  
$$

Now calculate the intercept:

$$  
c=\bar y-m\bar x  
$$

$$  
c=\frac{10}{3}-\frac{3}{2}(2)  
$$

$$  
\boxed{c=\frac{1}{3}}  
$$

Hence:

$$  
\boxed{  
\hat y=\frac{3}{2}x+\frac{1}{3}  
}  
$$

---

# 4. Type 3 — GATE Shortcut Using Sums

For the same data:

|$x$|$y$|$x^2$|$xy$|
|--:|--:|--:|--:|
|1|2|1|2|
|2|3|4|6|
|3|5|9|15|
|**$\Sigma$**||**14**|**23**|

Also:

$$  
\sum x=6  
$$

$$  
\sum y=10  
$$

$$  
n=3  
$$

Use:

$$  
m=  
\frac{  
n\sum xy-(\sum x)(\sum y)  
}{  
n\sum x^2-(\sum x)^2  
}  
$$

Substitute:

$$  
m=  
\frac{  
3(23)-(6)(10)  
}{  
3(14)-6^2  
}  
$$

# $$

\frac{69-60}{42-36}  
$$

$$  
=\frac{9}{6}  
$$

Therefore:

$$  
\boxed{m=\frac{3}{2}}  
$$

Then:

$$  
c=\bar y-m\bar x=\frac{1}{3}  
$$

### ⭐ Exam Tip

If the question gives a **table of values**, this formula is often the fastest:

$$  
\boxed{  
m=  
\frac{  
n\Sigma xy-\Sigma x\Sigma y  
}{  
n\Sigma x^2-(\Sigma x)^2  
}  
}  
$$

---

# 5. Type 4 — Data Is Shifted

Suppose instead of $x$, the question gives:

$$  
X=x-5  
$$

A common mistake is to recalculate everything from scratch.

### Key Fact

> **Translation of $x$ does not change the slope.**

For example, suppose:

$$  
y=3x+2  
$$

and define:

$$  
X=x-5  
$$

Since:

$$  
x=X+5  
$$

we get:

$$  
y=3(X+5)+2  
$$

$$  
y=3X+17  
$$

Therefore:

$$  
\boxed{\text{slope}=3}  
$$

but:

$$  
\boxed{\text{intercept}=17}  
$$

### ⭐ Key Idea

If:

$$  
X=x-a  
$$

then changing the origin:

- does **not** change the slope
    
- **does** change the intercept
    

---

# 6. Type 5 — Centered Variables

This is a very useful GATE shortcut.

Suppose:

$$  
u=x-\bar x  
$$

and

$$  
v=y-\bar y  
$$

Then:

$$  
\bar u=0  
$$

and

$$  
\bar v=0  
$$

The regression slope becomes:

$$  
\boxed{  
m=\frac{\sum uv}{\sum u^2}  
}  
$$

Since the centered means are zero:

$$  
\boxed{c=0}  
$$

for the regression of $v$ on $u$.

### Example

|$u$|$v$|
|--:|--:|
|-2|-4|
|-1|-1|
|0|0|
|1|2|
|2|3|

Calculate:

# $$  
\sum uv

= 8+1+0+2+6
= 
17  
$$

and:

# $$  
\sum u^2

= 4+1+0+1+4
=
10  
$$

Therefore:

$$  
\boxed{  
m=\frac{17}{10}  
}  
$$

Since the variables are centered:

$$  
\boxed{c=0}  
$$

---

# 7. Type 6 — Regression Through the Origin

Sometimes the model is explicitly:

$$  
\boxed{\hat y=mx}  
$$

There is **no intercept**.

Therefore:

$$  
c=0  
$$

The least-squares slope is:

$$  
\boxed{  
m=\frac{\sum x_i y_i}{\sum x_i^2}  
}  
$$

### Example

|$x$|$y$|
|--:|--:|
|1|2|
|2|5|
|3|7|

Calculate:

$$  
\sum xy=2+10+21=33  
$$

and:

$$  
\sum x^2=1+4+9=14  
$$

Therefore:

$$  
\boxed{  
m=\frac{33}{14}  
}  
$$

So:

$$  
\boxed{  
\hat y=\frac{33}{14}x  
}  
$$

### ⚠️ Important GATE Distinction

#### Normal Linear Regression

$$  
\boxed{  
m=  
\frac{  
\sum(x-\bar x)(y-\bar y)  
}{  
\sum(x-\bar x)^2  
}  
}  
$$

#### Regression Through Origin

$$  
\boxed{  
m=  
\frac{\sum xy}{\sum x^2}  
}  
$$

These are **not the same formula**.

---

# 8. Type 7 — Regression Coefficient Is Given

A common conceptual question gives:

- correlation coefficient $r$
    
- standard deviations $\sigma_X,\sigma_Y$
    

Remember:

# $$  
\boxed{  
m_{Y|X}

r\frac{\sigma_Y}{\sigma_X}  
}  
$$

Then:

$$  
\boxed{  
c=\bar Y-m\bar X  
}  
$$

### Example

Given:

$$  
r=0.8  
$$

$$  
\sigma_X=2  
$$

$$  
\sigma_Y=5  
$$

Then:

$$  
m=0.8\frac{5}{2}  
$$

$$  
\boxed{m=2}  
$$

If additionally:

$$  
\bar X=3  
$$

and:

$$  
\bar Y=10  
$$

then:

$$  
c=10-(2)(3)  
$$

$$  
\boxed{c=4}  
$$

Therefore:

$$  
\boxed{  
\hat Y=2X+4  
}  
$$

---

# 9. Type 8 — Covariance and Variance Are Given

This is the same idea in another form.

If:

$$  
\operatorname{Cov}(X,Y)=12  
$$

and:

$$  
\operatorname{Var}(X)=4  
$$

then:

$$  
m=  
\frac{  
\operatorname{Cov}(X,Y)  
}{  
\operatorname{Var}(X)  
}  
$$

Therefore:

$$  
\boxed{m=3}  
$$

If:

$$  
\bar X=2  
$$

and:

$$  
\bar Y=8  
$$

then:

$$  
c=8-3(2)  
$$

$$  
\boxed{c=2}  
$$

Thus:

$$  
\boxed{  
\hat Y=3X+2  
}  
$$

---

# 10. Type 9 — Regression Coefficients in Both Directions

This is a **classic GATE concept**.

### Regression of $Y$ on $X$

$$  
Y-\bar Y=b_{YX}(X-\bar X)  
$$

where:

# $$  
\boxed{  
b_{YX}

r\frac{\sigma_Y}{\sigma_X}  
}  
$$

### Regression of $X$ on $Y$

$$  
X-\bar X=b_{XY}(Y-\bar Y)  
$$

where:

# $$  
\boxed{  
b_{XY}

r\frac{\sigma_X}{\sigma_Y}  
}  
$$

### ⭐ Important Relationship

$$  
\boxed{  
b_{YX}b_{XY}=r^2  
}  
$$

### Example

Suppose:

$$  
r=0.6  
$$

$$  
\sigma_X=4  
$$

$$  
\sigma_Y=10  
$$

Then:

# $$  
b_{YX}

= 0.6\frac{10}{4}
=
1.5  
$$

while:

# $$  
b_{XY}

= 0.6\frac{4}{10}
=
0.24  
$$

Their product:

$$  
1.5(0.24)=0.36  
$$

Since:

$$  
r^2=(0.6)^2=0.36  
$$

we get:

$$  
\boxed{  
b_{YX}b_{XY}=r^2  
}  
$$

---

# 11. Type 10 — Matrix Form

For multiple linear regression:

$$  
\boxed{  
Y=X\beta+\epsilon  
}  
$$

The least-squares solution is:

$$  
\boxed{  
\hat\beta=(X^TX)^{-1}X^TY  
}  
$$

For simple linear regression:

$$  
Y=  
\begin{bmatrix}  
y_1\  
y_2\  
\vdots\  
y_n  
\end{bmatrix}  
$$

and:

$$  
X=  
\begin{bmatrix}  
1 & x_1\  
1 & x_2\  
\vdots & \vdots\  
1 & x_n  
\end{bmatrix}  
$$

The coefficient vector is:

$$  
\beta=  
\begin{bmatrix}  
c\  
m  
\end{bmatrix}  
$$

Therefore:

# $$  
\boxed{  
\begin{bmatrix}  
c\  
m  
\end{bmatrix}

(X^TX)^{-1}X^TY  
}  
$$

### ⭐ Remember

The coefficient vector is:

# $$  
\boxed{  
\beta=  
\begin{bmatrix}  
\text{intercept}\  
\text{slope}  
\end{bmatrix}

\begin{bmatrix}  
c\  
m  
\end{bmatrix}  
}  
$$

---

# ⭐ GATE DA — Linear Regression Formula Sheet

|Situation|Formula|
|---|---|
|Line|$\hat y=mx+c$|
|Two points|$m=\frac{y_2-y_1}{x_2-x_1}$|
|General LR slope|$m=\frac{\sum(x-\bar x)(y-\bar y)}{\sum(x-\bar x)^2}$|
|Shortcut slope|$m=\frac{n\sum xy-\sum x\sum y}{n\sum x^2-(\sum x)^2}$|
|Intercept|$c=\bar y-m\bar x$|
|Covariance form|$m=\frac{\operatorname{Cov}(X,Y)}{\operatorname{Var}(X)}$|
|Correlation form|$m=r\frac{\sigma_Y}{\sigma_X}$|
|Through origin|$m=\frac{\sum xy}{\sum x^2}$|
|Matrix LR|$\hat\beta=(X^TX)^{-1}X^TY$|
|Both regression coefficients|$b_{YX}b_{XY}=r^2$|

---

# 🧠 One Mental Picture to Remember

Think of linear regression as:

# $$  
\boxed{  
\text{Slope}

\frac{  
\text{how much X and Y move together}  
}{  
\text{how much X varies}  
}  
}  
$$

In mathematical form:

$$  
\boxed{  
m=  
\frac{  
\operatorname{Cov}(X,Y)  
}{  
\operatorname{Var}(X)  
}  
}  
$$

Then the intercept is automatic:

$$  
\boxed{  
c=\bar y-m\bar x  
}  
$$

### ⭐ The Two Formulas to Memorize First

If you remember only two formulas for GATE DA:

$$  
\boxed{  
m=  
\frac{\operatorname{Cov}(X,Y)}  
{\operatorname{Var}(X)}  
}  
$$

$$  
\boxed{  
c=\bar y-m\bar x  
}  
$$

These two formulas solve a surprisingly large fraction of **GATE DA linear regression** questions.