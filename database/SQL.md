
## **MODULE 1: SQL BASICS**

### Core Concept

SQL has 4 main operations: **SELECT, INSERT, UPDATE, DELETE** (CRUD).

### 1. **SELECT** - Retrieve Data

```sql
SELECT * FROM employees;  -- All columns
SELECT name, salary FROM employees;  -- Specific columns
```

### 2. **WHERE** - Filter Rows

```sql
SELECT * FROM employees WHERE salary > 50000;
SELECT * FROM employees WHERE department = 'IT' AND salary > 60000;
```

### 3. **ORDER BY** - Sort Results

```sql
SELECT * FROM employees ORDER BY salary DESC;  -- Descending
SELECT * FROM employees ORDER BY department ASC, salary DESC;  -- Multiple columns
```

### 4. **LIMIT** - Restrict Rows

```sql
SELECT * FROM employees LIMIT 10;  -- First 10 rows
SELECT * FROM employees ORDER BY salary DESC LIMIT 5;  -- Top 5 highest paid
```

### 5. **INSERT** - Add Data

```sql
INSERT INTO employees (name, salary, department) 
VALUES ('Raj', 70000, 'IT');
```

### 6. **UPDATE** - Modify Data

```sql
UPDATE employees SET salary = 75000 WHERE name = 'Raj';
```

### 7. **DELETE** - Remove Data

```sql
DELETE FROM employees WHERE id = 5;
```

---

### **Quick Practice**

1. Write a query to find all employees in 'Sales' department
2. Find employees with salary between 50k-80k
3. Sort employees by name alphabetically
```SQL
SELECT * FROM Sales;
SELECT * FROM Sales WHERE salary > 50000 AND salary < 80000;
-- SELECT * FROM Sales WHERE salary BETWEEN 50000 AND 80000;
SELECT name FROM Sales ORDER BY name ASC;
```




## **MODULE 2: JOINS** (Critical for interviews)

### The 4 Types

**1. INNER JOIN** - Only matching rows from both tables

```sql
SELECT e.name, d.department_name 
FROM employees e 
INNER JOIN departments d ON e.dept_id = d.id;
```

**2. LEFT JOIN** - All rows from left table + matching from right

```sql
SELECT e.name, d.department_name 
FROM employees e 
LEFT JOIN departments d ON e.dept_id = d.id;
```

**3. RIGHT JOIN** - All rows from right table + matching from left

```sql
SELECT e.name, d.department_name 
FROM employees e 
RIGHT JOIN departments d ON e.dept_id = d.id;
```

**4. FULL OUTER JOIN** - All rows from both tables

```sql
SELECT e.name, d.department_name 
FROM employees e 
FULL OUTER JOIN departments d ON e.dept_id = d.id;
```

### Key Concept

- **ON** = join condition (like WHERE for joins)
- Table aliases (e, d) = shorter code

---

### **Quick Practice**

1. Write INNER JOIN to get employee names + their manager names
2. Write LEFT JOIN to get all employees even if they don't have a department assigned

```SQL
-- EMPLOYEES TABLE
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    salary INT,
    dept_id INT,
    manager_id INT
);

-- Sample data:
--| id | name    | salary | dept_id | manager_id |
--|----|---------|--------|---------|------------|
--| 1  | Raj     | 70000  | 1       | NULL       |
--| 2  | Priya   | 60000  | 1       | 1          |
--| 3  | Arjun   | 55000  | 2       | 1          |
--| 4  | Neha    | 65000  | NULL    | 1          |

-- DEPARTMENTS TABLE
CREATE TABLE departments (
    id INT PRIMARY KEY,
    department_name VARCHAR(100)
);

-- Sample data:
--| id | department_name |
--|----|-----------------|
--| 1  | IT              |
--| 2  | Sales           |
--| 3  | HR              |


SELECT e.name, m.name
FROM employees e
INNER JOIN employees m
ON e.manager_id = m.id;

-- Output
--| employee_name | manager_name |
--|---------------|--------------|
--| Priya         | Raj          |
--| Arjun         | Raj          |
--| Neha          | Raj          |

SELECT e.*
FROM employees e
LEFT JOIN departments d
ON e.dept_id = d.id;
--Shows all employees + their dept (Neha will have NULL for dept_name since no dept_id)
```


## **MODULE 3: AGGREGATIONS & GROUP BY**

### Aggregation Functions

```sql
SELECT COUNT(*) FROM employees;           -- Count rows
SELECT SUM(salary) FROM employees;        -- Total salary
SELECT AVG(salary) FROM employees;        -- Average salary
SELECT MAX(salary) FROM employees;        -- Highest salary
SELECT MIN(salary) FROM employees;        -- Lowest salary
```

### GROUP BY - Aggregate by category

```sql
SELECT dept_id, COUNT(*) as emp_count
FROM employees
GROUP BY dept_id;
```

**Result:**

```
| dept_id | emp_count |
|---------|-----------|
| 1       | 3         |
| 2       | 1         |
| NULL    | 1         |
```

### Multiple Grouping

```sql
SELECT dept_id, COUNT(*) as count, AVG(salary) as avg_salary
FROM employees
GROUP BY dept_id;
```

### HAVING - Filter groups (like WHERE but for aggregates)

```sql
SELECT dept_id, COUNT(*) as emp_count
FROM employees
GROUP BY dept_id
HAVING COUNT(*) > 1;  -- Only departments with 2+ employees
```

---

### **Key Difference**

- **WHERE** = filters rows BEFORE grouping
- **HAVING** = filters groups AFTER grouping

```sql
SELECT dept_id, COUNT(*) as count
FROM employees
WHERE salary > 50000      -- Filter rows first
GROUP BY dept_id
HAVING COUNT(*) > 1;      -- Filter groups after
```

---

### **Quick Practice**

1. Find average salary by department
2. Find departments with total salary > 100000
3. Count employees per department, show only depts with 2+ employees

```SQL
SELECT d.department_name, AVG(e.salary) as avg_salary
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.id
GROUP BY d.department_name;

SELECT d.department_name, SUM(e.salary) as total_salary
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.id
GROUP BY d.department_name
HAVING SUM(e.salary) > 100000;


SELECT COUNT(*) as total, d.department_name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.id
GROUP BY d.department_name
HAVING COUNT(*) > 1;
```

