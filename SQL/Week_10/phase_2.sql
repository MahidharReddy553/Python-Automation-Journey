-- 23. Find all employees whose name contains the substring 'son' or starts with 'J' (case-insensitive).
SELECT * FROM Employees 
WHERE full_name LIKE '%an%' OR 
      full_name LIKE 'r%';
-- 24. Write a query using GROUP BY to calculate the minimum, maximum, and average hours_worked per project.
SELECT project_id, MIN(hours_worked), MAX(hours_worked), AVG(hours_worked) FROM employee_projects GROUP BY project_id;
-- 25. Query your View vw_ProjectAllocations to find all employees who have worked more than 40 hours on a single project.
SELECT * FROM vw_projectallocations WHERE hours_worked > 40;

-- 26. Explain the difference between WHERE and HAVING. Can you use HAVING without a GROUP BY clause?
-- WHERE: Filters rows before any aggregation (GROUP BY) is computed. Cannot contain aggregate functions (like SUM(), AVG()).
-- HAVING: Filters groups after aggregation has occurred.
-- Can HAVING be used without GROUP BY? Yes, it acts on the entire query result as a single group (e.g., SELECT AVG(salary) FROM Employees HAVING AVG(salary) > 50000;).

-- 27. Find all department names that have more than 1 employees
SELECT d.dept_name, COUNT(e.emp_id) as emp_count from departments d
INNER JOIN
employees e on e.dept_id = d.dept_id 
GROUP BY dept_name HAVING COUNT(e.emp_id) > 1;
-- 28. Write a self-join query to display each employee's full_name alongside their manager's full_name. Alias the manager column as Manager_Name.
SELECT 
    e.full_name AS full_name,
    m.full_name AS Manager_Name
FROM Employees e
LEFT JOIN Employees m ON e.manager_id = m.emp_id;

-- 29. What is a Foreign Key? Can a Foreign Key reference a column that is marked UNIQUE instead of a PRIMARY KEY?
-- What is a Foreign Key? Can a Foreign Key reference a column that is marked UNIQUE instead of a PRIMARY KEY?
-- A Foreign Key is a column or combination of columns that establishes a link between data in two tables.
-- Yes, a Foreign Key can reference any column that has a UNIQUE constraint, not just a PRIMARY KEY.

-- 30. Select all employees whose salary is strictly greater than the maximum salary of department 103.
SELECT * FROM employees e1 WHERE salary > (SELECT MAX(salary) FROM employees e2 where e2.dept_id = 3);

-- 31. What is Third Normal Form (3NF)? Explain what a Transitive Dependency is with a quick example.
-- A table is in 3NF if it is in 2NF and contains no transitive dependencies (non-key attributes depending on other non-key attributes: A -> B -> C).
-- Example: If Employees has (emp_id, zip_code, city), city depends on zip_code, which depends on emp_id. To satisfy 3NF, move zip_code and city to a separate ZipCodes table.

-- 32. Write a query to retrieve the 5 most recently hired employees, skipping the single newest hire (i.e., rows 2 through 6).
SELECT * FROM employees ORDER BY hire_date DESC LIMIT 5 OFFSET 1;
-- 33. List all projects where the total budget spent on employee salaries (calculated from assigned project hours or salary proportion) exceeds $100,000.
SELECT p.project_id, p.project_name, SUM(e.salary) FROM projects p
INNER JOIN 
employee_projects ep on ep.project_id = p.project_id
INNER JOIN
employees e on e.emp_id = ep.emp_id
GROUP BY p.project_id HAVING SUM(e.salary) > 100000;
