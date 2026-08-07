SELECT AVG(salary) FROM employees WHERE dept = 'marketing' GROUP BY city;

SELECT dept, COUNT(*) FROM employees GROUP BY dept ORDER BY COUNT(*) DESC;

SELECT dept, AVG(salary) FROM employees GROUP BY dept HAVING AVG(salary)>60000 ORDER BY AVG(salary) desc;

SELECT city, COUNT(*) FROM employees GROUP BY city HAVING COUNT(*)>2 ORDER BY city;

SELECT dept, SUM(salary) from employees GROUP BY dept ORDER BY SUM(salary) DESC;

SELECT dept, AVG(exp_yrs) FROM employees GROUP BY dept ORDER BY AVG(exp_yrs) DESC;

SELECT city, COUNT(*) FROM employees WHERE salary > 50000 GROUP BY city;