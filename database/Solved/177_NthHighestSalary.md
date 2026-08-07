# [177. Nth Highest Salary](https://leetcode.com/problems/nth-highest-salary/)

## Problem Statement

### Table: `Employee`

| Column Name | Type |
|-------------|------|
| id | int |
| salary | int |

- `id` is the primary key (contains unique values).
- Each row contains the salary of an employee.

---

Write a solution to find the **nth highest distinct salary** from the `Employee` table.

If there are fewer than `n` distinct salaries, return `NULL`.

The result should contain a single column named:

```text
getNthHighestSalary(n)
```

where `n` is the given input.

---

## Example 1

### Input

**Employee**

| id | salary |
|----|--------|
| 1 | 100 |
| 2 | 200 |
| 3 | 300 |

```text
n = 2
```

### Output

| getNthHighestSalary(2) |
|------------------------|
| 200 |

---

## Example 2

### Input

**Employee**

| id | salary |
|----|--------|
| 1 | 100 |

```text
n = 2
```

### Output

| getNthHighestSalary(2) |
|------------------------|
| NULL |

## Code

```SQL
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    set N = N-1;
  RETURN (
      # Write your MySQL query statement below.
        select distinct salary
        from Employee
        order by salary desc
        limit 1 offset N
  );
END
```