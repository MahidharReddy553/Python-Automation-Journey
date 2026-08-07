SELECT COUNT(*) FROM employees;

SELECT SUM(salary) FROM employees;

SELECT dept, AVG(salary) FROM employees GROUP BY dept;

SELECT MAX(salary) FROM employees;

SELECT MIN(salary) FROM employees;

SELECT dept, COUNT(*) FROM employees GROUP BY dept ORDER BY COUNT(*) DESC LIMIT 1;

SELECT city, COUNT(*) FROM employees GROUP BY city ORDER BY COUNT(*) DESC LIMIT 1;

SELECT dept, AVG(exp_yrs) FROM employees GROUP BY dept;

SELECT dept, COUNT(*) FROM employees GROUP BY dept HAVING COUNT(*) > 3;

SELECT dept, AVG(salary) FROM employees GROUP BY dept HAVING AVG(salary)>70000;