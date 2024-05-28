### Lab5 part-1: Exercise Solutions

Complete the following exercises by providing the appropriate SQL scripts. You can use the Google Cloud SQL server to complete this task.

1. First, you must set up your command line to the current project id.

* Type the following command and press enter. Make sure you replace the `<PROJECT_ID>` with your project id, as presented in the previous video.

```shell
$ gcloud config set project <PROJECT_ID>
```

>  Enter a password when prompted.
>  :rotating_light: Do not expect to see any characters on the screen! 

* Then, run the next command to connect to the SQL terminal.

```shell
$ gcloud sql connect <DATABASE_NAME> --user=<USER_NAME>
```

3. You are now connected to the SQL terminal, your terminal should look like this.

```shell
$ mysql>
```

3. Use SQL to create the following commands and review the existing material.
4. Provide an SQL script to list all the available databases.

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

5. Create a new database called `lab1_exercise_db`.

```sql
mysql> CREATE DATABASE lab1_exercise_db;

Query OK, 1 row affected (0.11 sec)
```

6. Select the `lab1_exercise_db` database as the current database to work.

```sql
mysql> use lab1_exercise_db;

Database changed
```

7. Create a new table called `planets`, following the next data and specifications.

   a. The table data includes the next:

| planet_id | planet_name | planet_terrain | planet_size |
| --------- | ----------- | -------------- | ----------- |
| A1        | Tatooine    | Desert         | 10465       |
| A2        | Coruscant   | Urban  area    | 6100        |

​	b. The table specification is as follows:

* `planet_id` is based on characters, and it is a primary key. This field will accept a maximum of 30 characters per input.
* `planet_name` is based on characters. This field will accept a maximum of 30 characters per input.
* `planet_terrain` is based on characters. This field will accept a maximum of 30 characters per input.
* `planet_size` is integer based.

8. Provide the SQL script to create the table.

```sql
mysql> CREATE TABLE planets(
    -> planet_id VARCHAR(30),
    -> planet_name VARCHAR (30),
    -> planet_terrain VARCHAR (30),
    -> planet_size INT,
    -> PRIMARY KEY (planet_id)
    -> );
    
Query OK, 0 rows affected (0.14 sec)
```

9. Run a command to show the available tables.

```
mysql> SHOW TABLES;
+----------------------------+
| Tables_in_lab1_exercise_db |
+----------------------------+
| planets                    |
+----------------------------+
1 row in set (0.11 sec)
```

10. Provide an SQL script to insert all the data into the `planets` table.

```sql
mysql> INSERT INTO
    -> planets
    -> VALUES
    -> ('A1','Tatooine','Desert',10465),
    -> ('A2', 'Coruscant','Urban area',6100);
    
Query OK, 2 rows affected (0.11 sec)
Records: 2  Duplicates: 0  Warnings: 0
```

11. Provide an SQL script to extract all the data and print it.

```mysql
mysql> SELECT * FROM planets;

+-----------+-------------+----------------+-------------+
| planet_id | planet_name | planet_terrain | planet_size |
+-----------+-------------+----------------+-------------+
| A1        | Tatooine    | Desert         |       10465 |
| A2        | Coruscant   | Urban area     |        6100 |
+-----------+-------------+----------------+-------------+
2 rows in set (0.10 sec)
```

12. Provide an SQL script to insert the following data.

| planet_id | planet_name  | planet_terrain | planet_size |
| --------- | ------------ | -------------- | ----------- |
| A3        | Death  Start | Urban  area    | 120         |

```mysql
mysql> INSERT INTO planets VALUES ('A3','Death Start','Urban area',120);

Query OK, 1 row affected (0.11 sec)
```

13. Run the previous insert command once more. Does it fail, and why?

```mysql
mysql> INSERT INTO planets VALUES ('A3','Death Start','Urban area',120);
ERROR 1062 (23000): Duplicate entry 'A3' for key 'planets.PRIMARY'

--The command fails since a record with the same id already exists!--
```

13. Provide an SQL script to **extract all the data** and print it.

```mysql
mysql> SELECT * FROM planets;

+-----------+-------------+----------------+-------------+
| planet_id | planet_name | planet_terrain | planet_size |
+-----------+-------------+----------------+-------------+
| A1        | Tatooine    | Desert         |       10465 |
| A2        | Coruscant   | Urban area     |        6100 |
| A3        | Death Start | Urban area     |         120 |
+-----------+-------------+----------------+-------------+
3 rows in set (0.11 sec)
```

14. Provide an SQL script to **extract all the planets** that have a size **greater than 5000** km.

```mysql
mysql> SELECT * FROM planets WHERE planet_size>5000;

+-----------+-------------+----------------+-------------+
| planet_id | planet_name | planet_terrain | planet_size |
+-----------+-------------+----------------+-------------+
| A1        | Tatooine    | Desert         |       10465 |
| A2        | Coruscant   | Urban area     |        6100 |
+-----------+-------------+----------------+-------------+
2 rows in set (0.11 sec)
```

15. Provide an SQL script to extract the planet names that have a **desert** terrain.

```mysql
mysql> SELECT planet_name FROM planets WHERE planet_terrain='Desert';

+-------------+
| planet_name |
+-------------+
| Tatooine    |
+-------------+
1 row in set (0.10 sec)
```

16. Provide an SQL script to **update** the size of the **Coruscant** planet to **6120**.

```mysql
mysql> UPDATE planets SET planet_size=6120 WHERE planet_id='A2';

Query OK, 1 row affected (0.11 sec)
Rows matched: 1  Changed: 1  Warnings: 0
```

17. Provide an SQL script to add a new column called `planet_population`. The new column should include **integers of up to 20 digits** in size.

```mysql
ALTER TABLE planets ADD planet_population INT(20);

Query OK, 0 rows affected, 1 warning (0.13 sec)
Records: 0  Duplicates: 0  Warnings: 1
```

18. Provide an SQL script to **update Tatooine's population to 200000**.

```mysql
mysql> UPDATE planets SET planet_population=200000 WHERE planet_id='A1';

Query OK, 1 row affected (0.11 sec)
Rows matched: 1  Changed: 1  Warnings: 0

-- It is a good practice to use ht planet_id when updat
```

19. Provide an SQL script to **delete the planet** `Death Star` from the table.

```mysql
DELETE FROM planets WHERE planet_id='A3';

Query OK, 1 row affected (0.12 sec)
```

20. Provide an SQL script to extract all the **planet names, terrains and sizes** for those **planets that start with the letter** `T`.

```mysql
mysql> SELECT * FROM planets WHERE planet_name LIKE 'T%';

+-----------+-------------+----------------+-------------+-------------------+
| planet_id | planet_name | planet_terrain | planet_size | planet_population |
+-----------+-------------+----------------+-------------+-------------------+
| A1        | Tatooine    | Desert         |       10465 |            200000 |
+-----------+-------------+----------------+-------------+-------------------+
1 row in set (0.11 sec)
```

:checkered_flag: Well done! 