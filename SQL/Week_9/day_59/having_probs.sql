SELECT COUNT(*), dept FROM employees GROUP BY dept HAVING COUNT(*) > 3;

SELECT dept, AVG(salary), COUNT(*) FROM employees GROUP BY dept HAVING AVG(salary) > 70000;

SELECT city, COUNT(*) FROM employees GROUP BY city HAVING COUNT(*)>2;

SELECT dept,SUM(salary) FROM employees GROUP BY dept HAVING SUM(salary)>300000;

SELECT designation, COUNT(*) FROM employees GROUP BY designation HAVING COUNT(*) <= 2;

SELECT dept, MIN(salary) FROM employees GROUP BY dept HAVING MIN(salary) > 50000;

SELECT city, COUNT(*) FROM employees GROUP BY city HAVING AVG(exp_yrs)>4;