
# 0x0E. SQL - More queries
![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/66988091.jpg)

## Resources

**Read or watch**:

-   [How To Create a New User and Grant Permissions in MySQL](https://intranet.hbtn.io/rltoken/u4h2MXcCQfadszlRMQy-gw "How To Create a New User and Grant Permissions in MySQL")
-   [How To Use MySQL GRANT Statement To Grant Privileges To a User](https://intranet.hbtn.io/rltoken/ztrEKQexfEDtZ-8EUsG70Q "How To Use MySQL GRANT Statement To Grant Privileges To a User")
-   [MySQL constraints](https://intranet.hbtn.io/rltoken/LBrFqCMm9N9woTX7sS7e0g "MySQL constraints")
-   [SQL technique: subqueries](https://intranet.hbtn.io/rltoken/YYpPtkqFeKSCsAU4Y_y3Og "SQL technique: subqueries")
-   [Basic query operation: the join](https://intranet.hbtn.io/rltoken/npLCp3WasK0SUSUQqCF25A "Basic query operation: the join")
-   [SQL technique: multiple joins and the distinct keyword](https://intranet.hbtn.io/rltoken/GmRLMhkY-pPvjcpzyDvmRg "SQL technique: multiple joins and the distinct keyword")
-   [SQL technique: join types](https://intranet.hbtn.io/rltoken/ryjyRRN7696rJV0maP03Xw "SQL technique: join types")
-   [SQL technique: union and minus](https://intranet.hbtn.io/rltoken/L7Fi5w8GZG5MSdQZ19e88g "SQL technique: union and minus")
-   [MySQL Cheat Sheet](https://intranet.hbtn.io/rltoken/V9vpLbtkFwV4EZYoiz2NBA "MySQL Cheat Sheet")
-   [The Seven Types of SQL Joins](https://intranet.hbtn.io/rltoken/ySKSdhFeMDddea07XrDzeQ "The Seven Types of SQL Joins")
-   [MySQL Tutorial](https://intranet.hbtn.io/rltoken/-uqP0a89xUl3SsmV_ZtxRA "MySQL Tutorial")
-   [SQL Style Guide](https://intranet.hbtn.io/rltoken/jn4SHgwVtOJF0LQYPEIs-g "SQL Style Guide")
-   [MySQL 8.0 SQL Statement Syntax](https://intranet.hbtn.io/rltoken/v1VjRjcgXmGeGq8ojvOPnA "MySQL 8.0 SQL Statement Syntax")

Extra resources around relational database model design:

-   [Design](https://intranet.hbtn.io/rltoken/9ppVdXqFMn-v1eKuxsOvaQ "Design")
-   [Normalization](https://intranet.hbtn.io/rltoken/zo6dqYxsXby3S3uON5JfOg "Normalization")
-   [ER Modeling](https://intranet.hbtn.io/rltoken/ZaMMezT-GdpgHB9pmM78iw "ER Modeling")

## Learning Objectives

At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/fwbj7FkG_ikCVBmGg82PLg "explain to anyone"),  **without the help of Google**:

### General

-   How to create a new MySQL user
-   How to manage privileges for a user to a database or table
-   What’s a  `PRIMARY KEY`
-   What’s a  `FOREIGN KEY`
-   How to use  `NOT NULL`  and  `UNIQUE`  constraints
-   How to retrieve datas from multiple tables in one request
-   What are subqueries
-   What are  `JOIN`  and  `UNION`

## Requirements

### General

-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files will be executed on Ubuntu 20.04 LTS using  `MySQL 8.0`  (version 8.0.25)
-   All your files should end with a new line
-   All your SQL queries should have a comment just before (i.e. syntax above)
-   All your files should start by a comment describing the task
-   All SQL keywords should be in uppercase (`SELECT`,  `WHERE`…)
-   A  `README.md`  file, at the root of the folder of the project, is mandatory
-   The length of your files will be tested using  `wc`

## More Info

### Comments for your SQL file:

```
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$

```

### Install MySQL 8.0 on Ubuntu 20.04 LTS

```
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$

```

Connect to your MySQL server:

```
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$

```

### Use “container-on-demand” to run MySQL

**In the container, credentials are  `root/root`**

-   Ask for container  `Ubuntu 20.04`
-   Connect via SSH
-   OR connect via the Web terminal
-   In the container, you should start MySQL before playing with it:

```
$ service mysql start                                                   
 * Starting MySQL database server mysqld 
$
$ cat 0-list_databases.sql | mysql -uroot -p                               
Database                                                                                   
information_schema                                                                         
mysql                                                                                      
performance_schema                                                                         
sys                      
$

```

**In the container, credentials are  `root/root`**

### How to import a SQL dump

```
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$

```

![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/3/bc2575fee3303b731031.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220914T044218Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=110c2f1f3f8975036c49da81fad0d4d086dcc19be5f1b87856dacf5683f1a70d)

```
