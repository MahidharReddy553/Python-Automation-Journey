-- SELECT QUERIES

SELECT * FROM employees;

SELECT first_name, dept FROM employees;

SELECT emp_id, first_name, designation, salary FROM employees;

SELECT * FROM employees WHERE dept = "finance";

SELECT * FROM employees WHERE salary > 60000;

SELECT * FROM employees where exp_yrs > 3;

SELECT emp_id, first_name, city FROM employees where city = "hyderabad";

SELECT * FROM employees where designation = "Software Engineer";

SELECT email FROM employees;

SELECT first_name, last_name, joining_date FROM employees;


-- WHERE+ QUERIES


SELECT * FROM employees WHERE salary < 50000;

SELECT * FROM employees WHERE exp_yrs = 5;

SELECT * FROM employees WHERE city = "bangalore";

SELECT * FROM employees WHERE joining_date > '2023-01-01';

SELECT * FROM employees WHERE joining_date < '2022-01-01';

SELECT * FROM employees WHERE dept = "development";

SELECT * FROM employees WHERE salary >= 80000;

SELECT * FROM employees WHERE exp_yrs <= 2;

SELECT * FROM employees WHERE designation = "recruiter";

SELECT * FROM employees WHERE emp_id = 10;



-- AND, OR, NOT


SELECT * FROM employees WHERE dept = 'it' AND city = 'hyderabad';

SELECT * FROM employees WHERE dept = 'HR' and salary > 70000;

SELECT * FROM employees WHERE dept = 'hr' OR dept = 'finance';

SELECT * FROM employees WHERE city = 'hyderabad' or city = 'bangalore';

SELECT * FROM employees WHERE salary > 60000 and exp_yrs > 4;

SELECT * FROM employees WHERE dept = 'marketing' AND designation = 'content writer';

SELECT * FROM employees WHERE NOT dept = 'marketing';

SELECT * FROM employees WHERE NOT city = 'hyderabad';

SELECT * FROM employees WHERE salary < 50000 AND exp_yrs < 2;

SELECT * FROM employees WHERE joining_date > '2022-01-01' AND city = 'bangalore';

SELECT * FROM employees WHERE NOT designation = 'support engineer';

SELECT * FROM employees WHERE dept = 'support' or dept = 'it';

SELECT * FROM employees WHERE salary>90000 or exp_yrs > 8;

SELECT * FROM employees WHERE city = 'chennai' and dept = 'hr';

SELECT * FROM employees WHERE salary > 65000 and NOT city = 'bangalore';


-- PRACTICE PROBLEMS


SELECT * FROM employees WHERE YEAR(joining_date) = '2023' AND designation = 'support engineer';

SELECT * FROM employees WHERE exp_yrs > 5;

SELECT * FROM employees WHERE email LIKE '%@example.com';

SELECT * FROM employees WHERE dept = 'it';
-- Find employees with duplicate first names.
SELECT first_name, COUNT(*) as name_count FROM employees GROUP BY first_name HAVING COUNT(*) > 1;

SELECT * FROM employees WHERE salary BETWEEN 50000 and 80000;

SELECT * FROM employees WHERE YEAR(joining_date) BETWEEN '2023' and '2024';

SELECT * FROM employees WHERE city = 'hyderabad' AND salary > 75000;

SELECT * FROM employees WHERE designation = 'support engineer' OR designation = 'frontend developer';

SELECT * FROM employees WHERE exp_yrs BETWEEN 2 AND 5;

SELECT * FROM employees WHERE salary = 65000;

SELECT * FROM employees WHERE NOT dept = 'hr';

SELECT * FROM employees WHERE joining_date = '2021-11-27';


--BONUS CHALLENGES

SELECT * FROM employees WHERE CONCAT(first_name,' ',last_name) = 'peter parker';

SELECT email, COUNT(*) as same_count FROM employees GROUP BY email HAVING COUNT(*) > 1;

SELECT * FROM employees WHERE dept is NOT NULL;

SELECT * FROM employees WHERE salary > 0;

SELECT * FROM employees WHERE dept = 'it' and salary > 40000;

SELECT COUNT(*) AS emp_count FROM employees;

SELECT * FROM employees WHERE YEAR(joining_date) > '2020';

SELECT * FROM employees WHERE designation like '%manager' AND exp_yrs > 5;

SELECT * FROM employees WHERE email IS NULL;

SELECT emp_id, dept FROM employees WHERE emp_id = 15;