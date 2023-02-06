# MyKeja
A tenant management system - unifies the landlord, caretaker, and tenant.

#### Using MySQL for the Database
* Install the `mysql-connector-python` library
```
pip install mysql-connector-python
```
* Create a database and table in Mysql
```
CREATE DATABASE mykeja;

USE mykeja;

CREATE TABLE tenants (
  id INT AUTO_INCREMENT PRIMARY KEY,
  Phone_number INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL
);
```


#### Using MySQL for the Database
* Install the `mysql-connector-python` library
```
pip install mysql-connector-python
```
* Create a database and table in Mysql
```
CREATE DATABASE mykeja;

USE mykeja;

CREATE TABLE tenants (
  id INT AUTO_INCREMENT PRIMARY KEY,
  Phone_number INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL
);
```



<h1> 