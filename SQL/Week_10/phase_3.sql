-- 45. Display the dept_name and the maximum salary in that department, but only for departments where the maximum salary exceeds $80,000.
SELECT d.dept_name, MAX(e.salary) as max_sal FROM Departments d
INNER JOIN Employees e 
ON d.dept_id = e.dept_id 
GROUP BY d.dept_id, d.dept_name
HAVING MAX(salary) > 80000;

-- 46. Explain what a Candidate Key is and how it relates to a Primary Key and a Unique Key
-- Candidate Key: Any column or set of columns that can uniquely identify a row without redundancy.
-- Primary Key: The specific Candidate Key chosen by the database designer as the main identifier (cannot accept NULL).
-- Unique Key: Any remaining Candidate Key(s) enforced to maintain unique values across rows (can accept NULL in most RDBMSs).

-- 47. Write a query to retrieve all employees who work in either the 'Engineering' or 'Marketing' departments using IN with a subquery.
SELECT emp_id, full_name FROM Employees WHERE dept_id IN ( SELECT dept_id FROM Departments WHERE dept_name = 'Engineering' OR dept_name = 'Marketing');
-- 48. Find all projects that have an assigned employee whose salary is under $70,000.
SELECT p.project_name FROM projects p
INNER JOIN
employee_projects ep on p.project_id = ep.project_id
INNER JOIN
employees e on e.emp_id = ep.emp_id
WHERE e.salary < 70000;

-- 49. What is a FULL OUTER JOIN? What does the result set look like when two tables have non-matching rows on both sides?
-- A FULL OUTER JOIN returns all rows from both the left and right tables.
-- Where rows match on the join condition, columns from both tables are combined.
-- Where there is no match, the non-matching side contains NULL values.

-- 50. List all employees whose manager_id is in the same department as the employee themselves.
SELECT e1.emp_id, e1.full_name, e1.manager_id FROM employees e1 
WHERE e1.dept_id 
IN (SELECT dept_id FROM employees e2 where e1.dept_id = e2.dept_id AND e2.emp_id = e1.manager_id);
SELECT e.emp_id, e.full_name
FROM Employees e
INNER JOIN Employees m ON e.manager_id = m.emp_id
WHERE e.dept_id = m.dept_id;
-- 51. Write a query to fetch the employee count per department, ordered from highest count to lowest count, limiting the output to the top 3 departments.
SELECT d.dept_name, COUNT(e.emp_id) AS total_employees
FROM Departments d
JOIN Employees e ON d.dept_id = e.dept_id
GROUP BY d.dept_id, d.dept_name
ORDER BY total_employees DESC
LIMIT 3;

SELECT dept_id, COUNT(*) as emp_count FROM Employees 
GROUP BY dept_id
ORDER BY emp_count DESC 
LIMIT 3;

-- 52. Explain what an Update Anomaly is in an unnormalized database.
-- An Update Anomaly occurs when duplicate copies of the same data exist across multiple rows in an unnormalized table. Updating the value in one row while missing another causes data inconsistency.

-- 53. Find all projects that have total assigned hours_worked greater than the storewide/companywide average hours_worked per project.
SELECT project_id, SUM(hours_worked) AS total_project_hours
FROM Employee_Projects
GROUP BY project_id
HAVING SUM(hours_worked) > (
    SELECT AVG(proj_hours) FROM (
        SELECT SUM(hours_worked) AS proj_hours
        FROM Employee_Projects
        GROUP BY project_id
    ) AS ProjTotals);
-- 54. Write a query to retrieve all employees who were hired in the year 2022 or 2023, but whose salary is strictly below $60,000.
SELECT * FROM Employees WHERE YEAR(hire_date) IN (2020, 2022) AND salary < 80000;

-- 55. What is a SQL View? Does a standard view store physical data on disk?
-- A SQL View is a virtual table defined by an underlying SELECT query. Standard views do not store physical data on disk; the query is executed dynamically whenever the view is queried.

-- 56. List all departments along with the total salary paid to all employees in that department. If a department has no employees, display 0 or NULL.
SELECT d.dept_id, d.dept_name, SUM(e.salary) FROM Departments d 
LEFT JOIN Employees e ON d.dept_id = e.dept_id
GROUP BY d.dept_id, d.dept_name
HAVING SUM(e.salary);
-- 57. Find all employees whose name does not contain the letter 'a' or 'E' using NOT LIKE or regular string checks.
SELECT * FROM Employees WHERE full_name NOT LIKE '%a%' OR '%e%' OR '%A%' OR '%E%';
-- 58. Write a query using IN with a multi-column subquery to find employees who match both the dept_id and salary of any employee hired before 2020.
SELECT emp_id, full_name FROM Employees WHERE (dept_id, salary) IN (SELECT dept_id, salary FROM Employees WHERE YEAR(hire_date) < 2020);

-- 59. What is the purpose of the NOT NULL constraint? Can a table have multiple NOT NULL columns?
-- The NOT NULL constraint enforces that a column cannot store NULL values. A table can have as many NOT NULL columns as required.

-- 60. Find all projects that have more than 3 employees assigned to them and a budget over $50,000.
SELECT p.project_id, p.project_name,  p.budget, COUNT(ep.emp_id) as emp_count FROM projects p
INNER JOIN 
employee_projects ep on ep.project_id = p.project_id
GROUP BY p.project_id
HAVING COUNT(ep.emp_id) > 2 AND p.budget > 50000;
-- 61. Write a query to display each project's name and the percentage of its total hours contributed by each employee on that project.
SELECT 
    p.project_name,
    e.full_name,
    ep.hours_worked,
    ROUND((ep.hours_worked * 100.0 / pt.total_hours), 2) AS percentage_of_project
FROM Employee_Projects ep
JOIN Projects p ON ep.project_id = p.project_id
JOIN Employees e ON ep.emp_id = e.emp_id
JOIN (
    SELECT project_id, SUM(hours_worked) AS total_hours
    FROM Employee_Projects
    GROUP BY project_id
) pt ON ep.project_id = pt.project_id;

-- 62. List the names of all employees who work on projects managed or owned by the department named 'Research & Development'.
SELECT DISTINCT e.full_name
FROM Employees e
INNER JOIN Employee_Projects ep1 ON e.emp_id = ep1.emp_id
INNER JOIN Employee_Projects ep2 ON ep1.project_id = ep2.project_id
INNER JOIN Employees rd_emp ON ep2.emp_id = rd_emp.emp_id
INNER JOIN Departments d ON rd_emp.dept_id = d.dept_id
WHERE d.dept_name = 'Finance';

-- 63. What is an Insertion Anomaly? How does 3NF help prevent it?
-- Your ordering and summation logic is on point, but the query is not fully correct due to the missing d.dept_name in the GROUP BY clause (which triggers a syntax error in most SQL engines) and the use of INNER JOIN omitting empty departments.

-- 64. Write a query that ranks departments by their total salary spend, displaying dept_id, dept_name, total_spend, sorted from highest to lowest spend.
SELECT d.dept_id, d.dept_name, SUM(e.salary) as total_spend FROM departments d
INNER JOIN employees e ON e.dept_id = d.dept_id
GROUP BY dept_id, dept_name
ORDER BY total_spend DESC;