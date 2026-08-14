CREATE Table Departments(dept_id INT PRIMARY KEY,
                        dept_name VARCHAR(20) UNIQUE NOT NULL,
                        location VARCHAR(20) DEFAULT 'Headquarters');


CREATE Table Employees(emp_id INT PRIMARY KEY,
                        full_name VARCHAR(45) NOT NULL,
                        email VARCHAR(30) UNIQUE,
                        salary DECIMAL(10,2) CHECK(salary>0),
                        dept_id INT,
                        Foreign Key (dept_id) REFERENCES Departments(dept_id) ON DELETE SET NULL,
                        manager_id INT,
                        Foreign Key (manager_id) REFERENCES Employees(emp_id),
                        hire_date DATE);

CREATE Table Projects(project_id INT PRIMARY KEY,
                      project_name VARCHAR(40),
                      budget DECIMAL(10,2));


CREATE TABLE Employee_projects(emp_id INT,
                               FOREIGN KEY (emp_id) REFERENCES Employees(emp_id) ON DELETE CASCADE,
                               project_id INT,
                               Foreign Key (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE,
                               hours_worked DECIMAL(10,2) DEFAULT 0,
                               PRIMARY KEY(emp_id, project_id));

