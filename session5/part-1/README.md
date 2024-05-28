### Lab5: Introduction to SQL

#### What am I about to learn?

Today's lab session is essential for a solid start in this module. Make sure you complete all the tasks before the next class.

Lab 5 part 1 focuses on how to:

**Part A**    Connect to the Google Cloud Platform and start the SQL server.

**Part B**    Learn the basic SQL commands.



#### How to best approach the tutorials?

The labs are in the form of a complete step-by-step tutorial that you need to follow.

- Do not just copy and paste the commands, but try to understand the steps by typing in the commands.

- Do not worry if you don't remember everything after the first class; we will have the opportunity to work with these commands repeatedly in the next ten weeks.

- Do not be afraid to try the commands repeatedly or adapt and get used to them. During this lab, commands that could be potentially harmful (for example, deleting data, etc.) will be highlighted.



####  Part A

* Follow the next video on how to perform this task. The video will show you how to connect to the Google Cloud Platform, redeem your coupon and configure an SQ server.
* Firstly, watch the following video on configuring MySQL on the GCP.  

[![Watch the video](https://i.ytimg.com/vi/jWkeFjfrCxQ/hqdefault.jpg)](https://www.youtube.com/watch?v=jWkeFjfrCxQ)

* Please make sure you complete **Part A** before proceeding.

**Here is the updated configuration page regarding the MySQL.**

![](mysql-configuration.png)

#### Part B

The following tutorial describes a list of commands to interact with the MySQL server deployed on the GCP.

1. First, you must set up your command line to the current project ID.

2. Type the following command and press enter. Make sure you replace the `<PROJECT_ID>` with your project ID, as presented in the previous video.

```shell
$ gcloud config set project <PROJECT_ID>
```

>  Enter a new password when prompted.
>  :rotating_light: Do not expect to see any characters on the screen! 

Then, connect to the SQL server using the next command.

```shell
$ gcloud sql connect <SQL-SERVER> --user=root
```

3. Let us run some basic commands and learn to use the MySQL command line interface (CLI).
4. List the databases that are already created.

```sql
mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| DBname             |
| information_schema |
| mydb               |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
6 rows in set (0.11 sec)
```

> This command shows the available databases; as you can see, a few were created already. In this tutorial, we will create a new database.

5. Create a new database called `film_db`.

```sql
mysql> CREATE DATABASE film_db;
Query OK, 1 row affected (0.11 sec)
```

> The database is now ready so that we can `use` it.
>
> If you run the `SHOW DATABASES` command once more, the new database will appear on the list.

6. Select the `film_db` database as the current database to work on.

```sql
mysql> USE film_db;
Database changed
```

7. Create a new table called actors, following the following data and specification.

   a. The table looks like this:

| actor_id | actor_first_name | actor_last_name | actor_city   |
| -------- | ---------------- | --------------- | ------------ |
| 1        | Tom              | Hanks           | Los  Angeles |
| 2        | Jude             | Law             | London       |
| 3        | Stephen          | Fry             | London       |

​	b. The table specification is as follows:

* `actor_id` is an integer so you will use an integer field `INT`. This field should accept unique values and cannot be empty.
* `actor_firstname` is based on characters, so that you will use the `VARCHAR`. This field will accept a maximum of 30 characters per input.
* `actor_last_name` is based on characters, so we will use the `VARCHAR`. This field will accept a maximum of 30 characters per input.
* `actor_city` is based on characters, so you will use the `VARCHAR`. This field will accept a maximum of 30 characters per input.

> Do not worry about the records for the moment; we only care about the creation of our table.

8. To create the table, run the following script.

```sql
CREATE TABLE actors (
actor_id INT(6),
actor_first_name VARCHAR(30),
actor_last_name VARCHAR(30),
actor_city VARCHAR(20),
PRIMARY KEY (actor_id)
);
```

> Note that when you type the command into the MySQL server, the terminal will look like this:
>
> ```shell
> mysql> CREATE TABLE actors (
>     -> actor_id INT(6),
>     -> actor_first_name VARCHAR(30),
>     -> actor_last_name VARCHAR(30),
>     -> actor_city VARCHAR(20),
>     -> PRIMARY KEY (actor_id)
>     -> );
> Query OK, 0 rows affected, 1 warning (0.14 sec)
> ```

> Each time you press and enter, you will see the `->` symbol.
>
> The `PRIMARY KEY`, ensures that the `actor_id` is always unique and cannot be empty. Do not worry about the `PRIMARY KEY` for the moment.

9. Now, run the `SHOW` command to see the available tables in the selected database.

```
mysql> SHOW TABLEs;
+-------------------+
| Tables_in_film_db |
+-------------------+
| actors            |
+-------------------+
1 row in set (0.11 sec)
```

10. Run the `DESCRIBE actors` command.

```shell
mysql> DESCRIBE actors;
+------------------+-------------+------+-----+---------+-------+
| Field            | Type        | Null | Key | Default | Extra |
+------------------+-------------+------+-----+---------+-------+
| actor_id         | int         | NO   | PRI | NULL    |       |
| actor_first_name | varchar(30) | YES  |     | NULL    |       |
| actor_last_name  | varchar(30) | YES  |     | NULL    |       |
| actor_city       | varchar(20) | YES  |     | NULL    |       |
+------------------+-------------+------+-----+---------+-------+
4 rows in set (0.10 sec)
```

> The `DESCRIBE`command shows the structure of a table which including column names, data-types and the nullability which means, that column can contain null values or not.

11. Let us insert the data into the database using the following command.

```sql
mysql> INSERT INTO actors (actor_id, actor_first_name, actor_last_name, actor_city) 
VALUES 	(1, 'Tom', 'Hanks', 'Los Angeles');
```

> Note that the command looks like this in SQL
>
> ```shell
> mysql> INSERT INTO actors (actor_id, actor_first_name, actor_last_name, actor_city)
>     -> VALUES (1, 'Tom', 'Hanks', 'Los Angeles');
> Query OK, 1 row affected (0.11 sec)
> ```

12. It seems that our first record is now created! Now let's insert the other two records using a single script.

```mysql
mysql> INSERT INTO actors (actor_id, actor_first_name, actor_last_name, actor_city) 
VALUES 
(2, 'Jude', 'Law', 'London'),
(3, 'Stephen', 'Fry', 'London');
```

> The output shows `Query OK, 2 rows affected (0.01 sec)`, that means the records have been now created.

13. Let us run our first query to extract all the data from the `actors` table. For this query, you will use the `SELECT` command, so run the following script.

```mysql
mysql> SELECT * FROM actors;

+----------+------------------+-----------------+-------------+
| actor_id | actor_first_name | actor_last_name | actor_city  |
+----------+------------------+-----------------+-------------+
|        1 | Tom              | Hanks           | Los Angeles |
|        2 | Jude             | Law             | London      |
|        3 | Stephen          | Fry             | London      |
+----------+------------------+-----------------+-------------+
```

> The use of the `*` can help us to select all the available columns, so we can now extract and print all the columns and the data.
>
> :rotating_light: You can clear the terminal by pressing `ctl`+`L`. You can also bring up the previous commands by pressing the up button from the keyboard :arrow_up:. 
>
> * Press it, and you will see the last command.
> * Press up and down, and you will access all the previous commands.

14. Now, let us select only some of the columns, and run the next script.

```mysql
mysql> SELECT actor_first_name, actor_last_name, actor_city FROM actors;

+------------------+-----------------+-------------+
| actor_first_name | actor_last_name | actor_city  |
+------------------+-----------------+-------------+
| Tom              | Hanks           | Los Angeles |
| Jude             | Law             | London      |
| Stephen          | Fry             | London      |
+------------------+-----------------+-------------+
3 rows in set (0.11 sec)
```

15. Extract data for actors first and last names from the actors table, only for those living in London.

```mysql
mysql> SELECT actor_first_name, actor_last_name FROM actors WHERE actor_city='London';

+------------------+-----------------+
| actor_first_name | actor_last_name |
+------------------+-----------------+
| Jude             | Law             |
| Stephen          | Fry             |
+------------------+-----------------+
2 rows in set (0.11 sec)
```

16. We can change the `actor` table and include a new column called `salary`. The salary will store integer data of up to 10 digits. To add a new column, we will use the `ALTER TABLE` command.

```mysql
mysql> ALTER TABLE actors ADD salary INT(10);

Query OK, 0 rows affected, 1 warning (0.13 sec)
Records: 0  Duplicates: 0  Warnings: 1
```

> Note that ideally, salary it should be named as `actor_salary` and it should be a float number.
>
> :rotating_light: Always be consistent when structuring your tables.

17. Let's drop the newly created column and then create it again using the appropriate naming and data type.

```mysql
mysql> ALTER TABLE actors DROP COLUMN salary;
```

18. Now let's create it again.

```mysql
mysql> ALTER TABLE actors ADD actor_salary FLOAT(10);
Query OK, 0 rows affected (0.12 sec)
Records: 0  Duplicates: 0  Warnings: 0
```

19. Extract and print all the actors, now it should look better.

```mysql
mysql> SELECT * FROM actors;

+----------+------------------+-----------------+-------------+--------------+
| actor_id | actor_first_name | actor_last_name | actor_city  | actor_salary |
+----------+------------------+-----------------+-------------+--------------+
|        1 | Tom              | Hanks           | Los Angeles |         NULL |
|        2 | Jude             | Law             | London      |         NULL |
|        3 | Stephen          | Fry             | London      |         NULL |
+----------+------------------+-----------------+-------------+--------------+
3 rows in set (0.10 sec)
```

> As you can see, the `actor_salary` is initialised with a `NULL` for all the current records.

18. Let's update the actor salaries using the following scripts.

```mysql
mysql> UPDATE actors SET actor_salary = 1000 WHERE actor_id = 1;

Query OK, 1 row affected (0.11 sec)
Rows matched: 1  Changed: 1  Warnings: 0
```

19. Let's confirm that the updated value is there.

```mysql
mysql> SELECT * FROM actors;

+----------+------------------+-----------------+-------------+--------------+
| actor_id | actor_first_name | actor_last_name | actor_city  | actor_salary |
+----------+------------------+-----------------+-------------+--------------+
|        1 | Tom              | Hanks           | Los Angeles |         1000 |
|        2 | Jude             | Law             | London      |         NULL |
|        3 | Stephen          | Fry             | London      |         NULL |
+----------+------------------+-----------------+-------------+--------------+
3 rows in set (0.10 sec)
```

20. Update the salaries of the next two records.

```mysql
mysql> UPDATE actors SET actor_salary = 2000 WHERE actor_id = 2;

Query OK, 1 row affected (0.11 sec)
Rows matched: 1  Changed: 1  Warnings: 0
```

21. And, now the last record.

```mysql
mysql> UPDATE actors SET actor_salary = 3000 WHERE actor_id = 3;

Query OK, 1 row affected (0.11 sec)
Rows matched: 1  Changed: 1  Warnings: 0
```

21. Use your up keyboard button :arrow_up_small: and bring up your `SELECT *` statement.

```mysql
mysql> SELECT * FROM actors;

+----------+------------------+-----------------+-------------+--------------+
| actor_id | actor_first_name | actor_last_name | actor_city  | actor_salary |
+----------+------------------+-----------------+-------------+--------------+
|        1 | Tom              | Hanks           | Los Angeles |         1000 |
|        2 | Jude             | Law             | London      |         2000 |
|        3 | Stephen          | Fry             | London      |         3000 |
+----------+------------------+-----------------+-------------+--------------+
3 rows in set (0.10 sec)
```

22. Let us select all the actors with a salary equal to or higher than 1500. Run the next command.

```
mysql> SELECT * FROM actors WHERE actors_salary>=1500;
ERROR 1054 (42S22): Unknown column 'actors_salary' in 'where clause'
```

> It seems that I have an error, the correct column name is `actor_salary`!
>
> Always read the `ERROR` statement. Now, let's fix it.

```mysql
mysql> SELECT * FROM actors WHERE actor_salary>=1500;

+----------+------------------+-----------------+------------+--------------+
| actor_id | actor_first_name | actor_last_name | actor_city | actor_salary |
+----------+------------------+-----------------+------------+--------------+
|        2 | Jude             | Law             | London     |         2000 |
|        3 | Stephen          | Fry             | London     |         3000 |
+----------+------------------+-----------------+------------+--------------+
2 rows in set (0.10 sec)
```

23. Let's insert more data in the database.

```mysql
mysql> INSERT INTO actors
    -> VALUES
    -> (4, 'Will', 'Smith', 'Los Angeles', 4000),
    -> (5, 'Angelina', 'Jolie', 'Los Angeles', 5000);
    
Query OK, 2 rows affected (0.11 sec)
Records: 2  Duplicates: 0  Warnings: 0
```

> You might notice that we did not define the column names in the `INSERT INTO actors` statement. Each time you insert data into all the records, you skip typing the column names. 
>
> To summarise, you can either type:
>
> ```mysql
>INSERT INTO actors 
> 	(actor_id, actor_first_name, actor_last_name, actor_city, actor_salary)
> VALUES 
> 	...
> ```
> 
> Or use the following:
>
> ```mysql
>INSERT INTO actors 
> VALUES 
> 	...
> ```

24. Extract all the actors once more.

```mysql
mysql> SELECT * FROM actors;

+----------+------------------+-----------------+-------------+--------------+
| actor_id | actor_first_name | actor_last_name | actor_city  | actor_salary |
+----------+------------------+-----------------+-------------+--------------+
|        1 | Tom              | Hanks           | Los Angeles |         1000 |
|        2 | Jude             | Law             | London      |         2000 |
|        3 | Stephen          | Fry             | London      |         3000 |
|        4 | Will             | Smith           | Los Angeles |         4000 |
|        5 | Angelina         | Jolie           | Los Angeles |         5000 |
+----------+------------------+-----------------+-------------+--------------+
5 rows in set (0.10 sec)
```

25. Let us select all the actors with a salary between 1500 and 4000. Note that between means including 1500 and 4000.

```mysql
mysql> SELECT * FROM actors WHERE actor_salary BETWEEN 1500 AND 4000;

+----------+------------------+-----------------+-------------+--------------+
| actor_id | actor_first_name | actor_last_name | actor_city  | actor_salary |
+----------+------------------+-----------------+-------------+--------------+
|        2 | Jude             | Law             | London      |         2000 |
|        3 | Stephen          | Fry             | London      |         3000 |
|        4 | Will             | Smith           | Los Angeles |         4000 |
+----------+------------------+-----------------+-------------+--------------+
3 rows in set (0.10 sec)
```

26. There is an alternative way to run this command, which is as follows.

```mysql
mysql> SELECT * FROM actors WHERE actor_salary>=1500 AND actor_salary<=4000;

+----------+------------------+-----------------+-------------+--------------+
| actor_id | actor_first_name | actor_last_name | actor_city  | actor_salary |
+----------+------------------+-----------------+-------------+--------------+
|        2 | Jude             | Law             | London      |         2000 |
|        3 | Stephen          | Fry             | London      |         3000 |
|        4 | Will             | Smith           | Los Angeles |         4000 |
+----------+------------------+-----------------+-------------+--------------+
3 rows in set (0.11 sec)
```

> I can define the selection boundaries using the appropriate conditions:
>
> * `>`: greater
>
> *  `<`: less
> * `<=`: less or equal
> * `>=`: greater or equal
> * `=`: equal
> * `<>`: not equal (or `!=` can be used)

27. Extract all the data except the data for the actor with id `2`.

```mysql
mysql> SELECT * FROM actors WHERE actor_id<>2;

+----------+------------------+-----------------+-------------+--------------+
| actor_id | actor_first_name | actor_last_name | actor_city  | actor_salary |
+----------+------------------+-----------------+-------------+--------------+
|        1 | Tom              | Hanks           | Los Angeles |         1000 |
|        3 | Stephen          | Fry             | London      |         3000 |
|        4 | Will             | Smith           | Los Angeles |         4000 |
|        5 | Angelina         | Jolie           | Los Angeles |         5000 |
+----------+------------------+-----------------+-------------+--------------+
4 rows in set (0.10 sec)
```

28. Now, let us delete the actor with id 5 from our table using the following command.

```mysql
mysql> DELETE FROM actors WHERE actor_id = 5;

Query OK, 1 row affected (0.11 sec)
```

> :rotating_light: Use the `DELETE` command with care, a wrong `DELETE` statement might delete a lot of data!

29. Extract all the data once more.

```mysql
mysql> SELECT * FROM actors;

+----------+------------------+-----------------+-------------+--------------+
| actor_id | actor_first_name | actor_last_name | actor_city  | actor_salary |
+----------+------------------+-----------------+-------------+--------------+
|        1 | Tom              | Hanks           | Los Angeles |         1000 |
|        2 | Jude             | Law             | London      |         2000 |
|        3 | Stephen          | Fry             | London      |         3000 |
|        4 | Will             | Smith           | Los Angeles |         4000 |
+----------+------------------+-----------------+-------------+--------------+
4 rows in set (0.10 sec)
```

30. Well done :clap: , you completed the first MySQL tutorial.

:checkered_flag: Well done! 