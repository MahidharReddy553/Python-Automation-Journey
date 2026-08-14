-- 1. Find the top 3 highest-paid employees in department `101`. Display their `full_name` and `salary`.
SELECT emp_id, full_name, salary FROM employees WHERE dept_id = 1 ORDER BY salary DESC LIMIT 3;

-- 2. What is the fundamental difference between INNER JOIN and LEFT JOIN? What happens to non-matching rows from the right table in a LEFT JOIN?
-- Difference between INNER JOIN and LEFT JOIN
-- INNER JOIN: Returns only the rows where there is a match in both joined tables.
-- LEFT JOIN: Returns all rows from the left table and matched rows from the right table. For non-matching rows from the right table, all its column values in the result set are filled with NULL.

-- 3. Write a query to retrieve all employees whose email ends with '@company.com' and whose salary is between $50,000 and $90,000.
SELECT * FROM employees WHERE email LIKE '%@example.com' AND salary BETWEEN 50000 AND 90000;
-- 4. Find all department IDs where the average employee salary is greater than $75,000.
SELECT dept_id FROM employees GROUP BY dept_id HAVING AVG(salary) > 75000;

-- 5. What is First Normal Form (1NF)? What two main violations keep an unnormalized table from meeting 1NF?
-- What is First Normal Form (1NF)? What two main violations keep an unnormalized table from meeting 1NF?
-- A table is in 1NF if:
    -- Every column contains atomic (indivisible) values (no multi-value lists or CSVs in a single cell).
    -- There are no repeating groups of similar columns (e.g., phone1, phone2, phone3).
    -- Each record is uniquely identifiable (has a primary key).

-- 6. Write a query using EXISTS to list all departments that currently have at least one employee assigned to them.
SELECT d.dept_id, d.dept_name FROM Departments d
WHERE EXISTS (
    SELECT 1 FROM Employees e 
    WHERE e.dept_id = d.dept_id);
-- 7. Display the total number of employees and the average salary across the entire company. Alias the columns as Total_Staff and Average_Pay.
SELECT COUNT(*) as Total_Staff, ROUND(AVG(salary), 2) as Average_Pay FROM employees;

-- 8. What happens when you execute a DELETE statement on a parent table row if the child table's Foreign Key constraint is configured with ON DELETE CASCADE vs. ON DELETE RESTRICT?
-- What happens when you execute a DELETE statement on a parent table row if the child table's Foreign Key constraint is configured with ON DELETE CASCADE vs. ON DELETE RESTRICT?
-- ON DELETE CASCADE: When the parent record is deleted, all associated child records referencing it are automatically deleted.
-- ON DELETE RESTRICT (or NO ACTION): Prevents deletion of the parent record as long as child records reference it, throwing a foreign key violation error.

-- 9. Find all employees who do not have a manager assigned (manager_id is missing).
SELECT * FROM employees WHERE manager_id IS NULL;
-- 10. Find all employees whose salary is higher than the average salary of their own department (Correlated Subquery).
SELECT * FROM Employees e1 WHERE salary > (SELECT AVG(salary) FROM Employees e2 WHERE e1.dept_id = e2.dept_id);
-- 11. Create a View named vw_ProjectAllocations that shows emp_id, full_name, project_name, and hours_worked.
CREATE VIEW vw_ProjectAllocations
AS
SELECT e.emp_id, e.full_name, p.project_name, ep.hours_worked 
FROM employees e
INNER JOIN
employee_projects ep on ep.emp_id = e.emp_id
INNER JOIN
projects p on ep.project_id = p.project_id;
SELECT * FROM employee_projects;
SELECT * FROM projects;
SELECT * FROM vw_ProjectAllocations;

-- 12. Why does the query SELECT * FROM Employees WHERE manager_id = NULL; fail to return rows? What is the correct syntax?
SELECT * FROM Employees WHERE manager_id IS NULL;
-- Why does the query SELECT * FROM Employees WHERE manager_id = NULL; fail to return rows? What is the correct syntax?
-- In SQL, NULL represents an unknown/missing state. Standard comparison operators (=, !=, <>) return UNKNOWN when compared to NULL. The correct syntax requires the IS NULL or IS NOT NULL predicate:
-- SELECT * FROM Employees WHERE manager_id IS NULL;

-- 13. List all projects along with the total hours worked on each project. Include projects that currently have zero hours or no assigned employees.
SELECT p.project_id, p.project_name, ep.hours_worked FROM Projects p
LEFT JOIN Employee_projects ep 
ON p.project_id = ep.project_id;

-- 14. What is a Composite Primary Key? Give a practical reason why Employee_Projects uses a composite key instead of a single auto-incrementing ID.
-- What is a Composite Primary Key? Give a practical reason why Employee_Projects uses a composite key instead of a single auto-incrementing ID.
-- A Composite Primary Key is a primary key composed of two or more columns that together uniquely identify a record. In Employee_Projects, 
-- (emp_id, project_id) ensures an employee cannot be assigned to the exact same project multiple times, while avoiding duplicate artificial surrogate keys.

-- 15. Write a query to list all distinct locations where departments are located, excluding NULL values, sorted alphabetically.
SELECT DISTINCT location FROM departments WHERE location IS NOT NULL ORDER BY location;
-- 16. Find the employee(s) with the absolute lowest salary in the company using a scalar subquery.
SELECT * FROM Employees WHERE salary = (SELECT MIN(salary) FROM Employees);

-- 17. Explain the concept of Referential Integrity. Which SQL key enforces it?
-- Referential Integrity is a database property ensuring relationships between tables remain consistent. 
-- It prevents child tables from having invalid foreign keys pointing to nonexistent parent records. 
-- It is enforced using Foreign Keys (FOREIGN KEY).

-- 18. Retrieve all employees hired between '2020-01-01' and '2020-12-31' who work in either department 101, 102, or 105.
SELECT * FROM Employees WHERE hire_date BETWEEN '2020-01-01' AND '2020-12-31' AND dept_id IN (1, 2, 5);
-- 19. Write a query that displays each department name and the count of projects assigned to employees in that department.
SELECT d.dept_id, d.dept_name, 
       COUNT(DISTINCT ep.project_id) AS project_count
FROM Departments d
LEFT JOIN Employees e ON e.dept_id = d.dept_id
LEFT JOIN Employee_Projects ep ON e.emp_id = ep.emp_id
GROUP BY d.dept_id, d.dept_name;

-- 20. What is Second Normal Form (2NF)? Which key structural issue does 2NF aim to eliminate?
-- A table is in 2NF if:
    -- It is already in 1NF.
    -- It has no partial dependency — all non-key attributes must be fully functionally dependent on the entire primary key (relevant when tables have composite keys).

-- 21. List all employees who are not currently assigned to any project in the Employee_Projects table using NOT IN or NOT EXISTS.
SELECT * FROM employees e
WHERE NOT EXISTS
(SELECT 1 from employee_projects ep WHERE e.emp_id = ep.emp_id);
-- 22. Combine a list of current project names and department names into a single column result set, keeping all duplicate names if any exist.
SELECT project_name AS names FROM projects
UNION ALL
SELECT dept_name AS names FROM departments;