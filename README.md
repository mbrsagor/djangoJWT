# psql
> This is PSQL database basic command line here. If you if want to learn aobut `PSQL` you may follow the tutorial.
###### Open database using terminal.
` psql postgres`

###### How to create database?
`CREATE DATABASE db_name;`

###### How to show list of database?
`\l`

###### Switch/connection database form shell.
` \c db_name`

###### Drop database.
`DROP DATABASE db_name;`

###### How to create table?
```
CREATE TABLE student (
id INT NOT NULL PRIMARY KEY,
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50) NOT NULL,
gender VARCHAR(10) NOT NULL,
email VARCHAR(75),
date DATE);
```
Then show table `data` using `\d`

###### Descripte table.
` \d table_name;`
`\dt`

###### How to drop table?
`DROP TABLE table_name;`

###### Insert data into table.
```
INSERT INTO student(first_name, last_name, gender, date, email)
VALUES('mbr', 'sagor', 'yes', date '2020-10-10', 'mbrsagor@gmail.com');
```
