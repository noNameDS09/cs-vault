# [176. Second Highest Salary](https://leetcode.com/problems/second-highest-salary/)

## Problem Statement

### Table: `Employee`

| Column Name | Type |
|-------------|------|
| id | int |
| salary | int |

- `id` is the primary key (contains unique values).
- Each row contains the salary of an employee.

---

Write a query to find the **second highest distinct salary** from the `Employee` table.

- If there is no second highest distinct salary, return `NULL` (or `None` in Pandas).

The result should contain a single column named:

```text
SecondHighestSalary
```

---

## Example 1

### Input

**Employee**

| id | salary |
|----|--------|
| 1 | 100 |
| 2 | 200 |
| 3 | 300 |

### Output

| SecondHighestSalary |
|---------------------|
| 200 |

---

## Example 2

### Input

**Employee**

| id | salary |
|----|--------|
| 1 | 100 |

### Output

| SecondHighestSalary |
|---------------------|
| NULL |

```SQL
# Write your MySQL query statement below
select max(salary) as SecondHighestSalary 
from Employee
where salary < (
    select max(salary)
    from Employee
);
```