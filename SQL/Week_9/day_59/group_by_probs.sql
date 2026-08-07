SELECT dept, count(dept) as dept_count FROM employees GROUP BY dept;

SELECT city, COUNT(city) FROM employees GROUP BY city;

SELECT AVG(salary), dept, count(dept) FROM employees GROUP BY dept;

SELECT MAX(salary), dept, COUNT(dept) FROM employees GROUP BY dept;

SELECT MIN(salary), dept, COUNT(dept) FROM employees GROUP BY dept;

SELECT SUM(salary), dept, COUNT(dept) FROM employees GROUP BY dept;

SELECT AVG(exp_yrs), dept, COUNT(dept) FROM employees GROUP BY dept;

SELECT designation, COUNT(*) FROM employees GROUP BY designation;

SELECT city, COUNT(*) FROM employees GROUP BY city;

SELECT city, SUM(salary) FROM employees GROUP BY city;