```SQL
-- DEPARTMENTS TABLE
CREATE TABLE departments (
    id INT PRIMARY KEY,
    department_name VARCHAR(100)
);

INSERT INTO departments VALUES
(1, 'IT'),
(2, 'Sales'),
(3, 'HR'),
(4, 'Finance');

-- EMPLOYEES TABLE
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    salary INT,
    dept_id INT,
    manager_id INT,
    hire_date DATE,
    FOREIGN KEY (dept_id) REFERENCES departments(id),
    FOREIGN KEY (manager_id) REFERENCES employees(id)
);

INSERT INTO employees VALUES
(1, 'Raj', 100000, 1, NULL, '2020-01-15'),
(2, 'Priya', 75000, 1, 1, '2021-03-20'),
(3, 'Arjun', 75000, 1, 1, '2021-06-10'),
(4, 'Neha', 120000, 2, NULL, '2019-02-01'),
(5, 'Amit', 65000, 2, 4, '2022-05-15'),
(6, 'Zara', 55000, 3, NULL, '2021-08-22'),
(7, 'Vikram', 95000, 1, 1, '2020-11-30'),
(8, 'Deepa', 85000, NULL, 1, '2022-01-10'),
(9, 'Rohit', 110000, 1, 1, '2020-07-14'),
(10, 'Sana', 45000, 3, 6, '2023-02-28');
```


## **INTERVIEW QUESTIONS (Modules 1-3)**

### **EASY (Warm-up)**

Write a query to find all employees with salary > 60000
```SQL
SELECT *
FROM employees
WHERE salary > 60000;
```

Find the employee with the highest salary
```SQL
SELECT salary, name
FROM employees
ORDER BY salary DESC
LIMIT 1;
```

Count total number of employees
```SQL
SELECT COUNT(*) AS total_employees
FROM employees;
```

List all unique departments
```SQL
SELECT DISTINCT department_name
FROM departments;
-- SELECT department_name FROM departments; -- since id is unique
```

Get top 10 employees ordered by salary (descending)
```SQL
SELECT name, salary
FROM employees
ORDER BY salary DESC
LIMIT 10;
```

Insert a new employee record
```SQL
INSERT INTO employees VALUES
(11, 'Shreyash', 100000, 1, NULL, '2026-01-15');
```

Update employee salary where name = 'Raj'
```SQL
UPDATE employees
SET salary = 100000
WHERE name = 'Raj';
```

Delete employee with id = 5
```SQL
DELETE FROM employees
WHERE id = 5;
```

---

### **MEDIUM (Common)**

Find the 2nd highest salary
```SQL
SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 1;

-- OR --
-- We can get max salary first (sub-query)
-- Then we get max salary from the remaining ones (which is the second highest salary)
SELECT MAX(salary) as max_salary
FROM employees
WHERE salary < (SELECT MAX(salary) from employees);
```

List employees and their department names (use JOIN)
```SQL
SELECT e.name, d.departments
FROM employees e
JOIN department d
ON e.dept_id = d.id;
```

Find employees whose salary is above average
```SQL
SELECT salary, name
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```

Get departments with more than 2 employees
```SQL
SELECT d.department_name, COUNT(*)
FROM departments d
JOIN employees e
ON d.id = e.dept_id
GROUP BY d.id, d.department_name
HAVING COUNT(*) > 2;

-- In strict SQL configurations (like PostgreSQL or standard SQL modes in MySQL), when you use `GROUP BY`, every column in your `SELECT` clause that is not an aggregate function must be included in your `GROUP BY` clause. [[1](https://gobisan.medium.com/behind-the-scenes-of-sql-aa264736b33b)]

-- Because you selected `d.department_name` but grouped only by `d.id`, a strict database engine might throw an error saying `d.department_name` is functionally dependent or missing from the `GROUP BY` clause.
```

Find employees who don't have a manager assigned
```SQL
SELECT e1.name
FROM employees e1
WHERE e1.manager_id is NULL;
```

List all employees with their manager's name (self-join)
```SQL
SELECT 
	e1.name as employee, 
	e2.name as manager
FROM employees e1
JOIN employees e2 -- If you don't want to exclude the managers itself then use `LEFT JOIN employees e2 
ON e1.manager_id = e2.id;
```

Find average salary by department
```SQL
SELECT d.department_name, AVG(e.salary) as avg_salary
FROM departments d
JOIN employees e
ON d.id = e.dept_id
GROUP BY d.department_name;
```

Get total salary expense by department
```SQL
SELECT d.department_name, SUM(e.salary) as total_expenses
FROM departments d
JOIN employees e
ON d.id = e.dept_id
GROUP BY d.department_name;
```

Find departments where average salary > 65000
```SQL
SELECT d.department_name, AVG(e.salary) as avg_salary
FROM departments d
JOIN employees e
ON d.id = e.dept_id
GROUP BY d.department_name
HAVING AVG(e.salary) > 65000;
```

List employees ordered by department then by salary
```SQL
SELECT e.name, d.department_name, e.salary
FROM employees e
JOIN departments d
ON e.dept_id = d.id
ORDER BY d.id ASC, e.salary DESC;
```

---

### **MEDIUM-HARD (LPA Decider)**

Find the employee with the highest salary in each department
```SQL
SELECT *
FROM (
    SELECT
        e.name,
        e.salary,
        d.department_name,
        DENSE_RANK() OVER (
            PARTITION BY e.dept_id
            ORDER BY e.salary DESC
        ) AS salary_rank
    FROM employees e
    JOIN departments d
        ON e.dept_id = d.id
) 
WHERE salary_rank = 1;
```

### Concepts used here RANK, DENSE_RANK, PARTITION BY, OVER : [[SQL]]

Get cumulative salary by department
```SQL

```

Find employees earning more than their department average
```SQL
```

List departments and count of employees, only showing depts with 2+ employees
```SQL
```

Find employees whose salary is in top 3 of their department
```SQL
```

Get the department with the highest average salary
```SQL
```

Find employees who joined before average join date (if hire_date exists)
```SQL
```

List employees with salary between 50k-80k, sorted by department
```SQL
```


---

### **TRICKY (Interview Favorites)**

Find the 2nd, 3rd highest salary WITHOUT using LIMIT/OFFSET
```SQL
```

Get all employees and their manager (even if manager doesn't exist) - handle NULLs
```SQL
```

Find department where total salary = maximum total salary
```SQL
```

Get employees earning more than ALL employees in HR department
```SQL
```

Find departments with both high earners (>70k) AND low earners (<55k)
```SQL
```

Match employees with departments even if some depts have no employees
```SQL
```

Find duplicate salaries (employees earning the same)
```SQL
```

Get employees whose salary is greater than their manager's salary
```SQL
```

---

### **REAL COMPANY PATTERNS**

**Amazon/Microsoft/Google ask:**

- Joins + GROUP BY combinations
- Self-joins (employee-manager)
- Handling NULLs properly
- Subqueries (coming next module)

**Startups ask:**

- Simple aggregations
- Basic JOINs
- GROUP BY + HAVING

---

**I recommend practicing #9, #14, #19, #23, #27, #31 first** (highest frequency).

