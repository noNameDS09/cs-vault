# [175. Combine Two Tables](https://leetcode.com/problems/combine-two-tables/)

## Problem Statement

### Table: `Person`

| Column Name | Type |
|-------------|------|
| personId | int |
| lastName | varchar |
| firstName | varchar |

- `personId` is the primary key (contains unique values).
- This table contains the ID, first name, and last name of each person.

---

### Table: `Address`

| Column Name | Type |
|-------------|------|
| addressId | int |
| personId | int |
| city | varchar |
| state | varchar |

- `addressId` is the primary key (contains unique values).
- Each row contains the city and state of a person identified by `personId`.

---

Write a query to report the **first name**, **last name**, **city**, and **state** of every person in the `Person` table.

If a person's address is not present in the `Address` table, return `NULL` for the city and state.

Return the result table in any order.

---

## Example

### Input

**Person**

| personId | lastName | firstName |
|----------|----------|-----------|
| 1 | Wang | Allen |
| 2 | Alice | Bob |

**Address**

| addressId | personId | city | state |
|-----------|----------|---------------|------------|
| 1 | 2 | New York City | New York |
| 2 | 3 | Leetcode | California |

---

### Output

| firstName | lastName | city | state |
|-----------|----------|---------------|----------|
| Allen | Wang | NULL | NULL |
| Bob | Alice | New York City | New York |

---

### Explanation

- `personId = 1` has no matching record in the `Address` table, so `city` and `state` are `NULL`.
- `personId = 2` has an address, so its corresponding city and state are returned.

## Code

```SQL
# Write your MySQL query statement below
select p.firstName, p.lastName, a.city, a.state
from Person p
left join Address a
on p.personId = a.personId;
```