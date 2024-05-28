### Lab5 part 2: Advanced SQL commands

#### What am I about to learn?

Today's lab session is essential for a solid start in this module. Make sure you complete all the tasks before the next class.


####  Running the commands on the GCP

* **You should start your MySQL server on the GCP to run this tutorial.** 

1. First, you must set up your command line to the current project ID.

2. Type the following command and press enter. Make sure you replace the `<PROJECT_ID>` with your project id, as presented in the previous video.

```shell
$ gcloud config set project <PROJECT_ID>
```

>  Enter a new password when prompted.
>  :rotating_light: Do not expect to see any characters on the screen! 

Then, connect to the SQL server using the following command, by replacing `<SQL-SERVER>` with your server.

```shell
$ gcloud sql connect <SQL-SERVER> --user=root
```

3. Let us run the following commands and learn how to use the MySQL command line interface (CLI).
4. List the databases (e.g. the `film_db`) you created in the previous class.

```sql
mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| DBname             |
| film_db            |
| information_schema |
| lab1_exercise_db   |
| mydb               |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
9 rows in set (0.11 sec)
```

5. We will create a new database called `movies_db`.

```sql
mysql> CREATE DATABASE movies_db;
Query OK, 1 row affected (0.11 sec)
```

> The database is now ready so that we can `use` it.
>
> If you run the `SHOW DATABASES` command once more, the new database, it will appear on the list.

6. Select the `film_db` database as the current database to work on.

```sql
mysql> USE movies_db;
Database changed
```

7. Create a new table called actors, following the following data and specification.

   a. The table looks like this:

| city_id | city_name | city_country | city_population |
| ------- | --------- | ------------ | --------------- |
| C1      | London    | England      | 8.982.000       |
| C2      | Athens    | Greece       | 3.154.000       |
| C3      | Toronto   | Canada       | 6.197.000       |

The table specification is as follows:

* `city_id` is based on characters, so that you will use the `VARCHAR`. This field will accept a maximum of 30 characters per input. The `city_id` is a primary key, that means it is always required and it is unique.
* `city_name` is based on characters, so that you will use the `VARCHAR`. This field will accept a maximum of 30 characters per input.
* `city_country` is based on characters, so that you will use the `VARCHAR`. This field will accept a maximum of 30 characters per input.
* `city_population` is based an integer filed of up to 8 digits, so we will use `INT(8)`

> Do not worry about the records for the moment; we only care about the creation of our table.

8. To create the table, run the following script.

```sql
CREATE TABLE cities (
city_id VARCHAR(30),
city_name VARCHAR(30) NOT NULL,
city_country VARCHAR(30) NOT NULL,
city_population INT(8),
PRIMARY KEY (city_id)
);
```

9. Now, run the `SHOW` command to see the available tables in the selected database.

```
mysql> SHOW TABLES;
+-------------------+
| Tables_in_film_db |
+-------------------+
| cities            |
+-------------------+
1 row in set (0.11 sec)
```

10. Run the `DESCRIBE actors` command.

```shell
mysql> DESCRIBE cities;
+-----------------+-------------+------+-----+---------+-------+
| Field           | Type        | Null | Key | Default | Extra |
+-----------------+-------------+------+-----+---------+-------+
| city_id         | varchar(30) | NO   | PRI | NULL    |       |
| city_name       | varchar(30) | NO   |     | NULL    |       |
| city_country    | varchar(30) | NO   |     | NULL    |       |
| city_population | int         | YES  |     | NULL    |       |
+-----------------+-------------+------+-----+---------+-------+
4 rows in set (0.11 sec)
```

> The `DESCRIBE`command shows the structure of a table which including column names, data-types and the nullability which means, that column can contain null values or not.

11. Let us insert the data into the database using the following command.

* Be extra careful when you type long commands. It is recommended that you type the commands in an editor and then paste it to the Google shell.

```sql
INSERT INTO 
cities (city_id, city_name, city_country, city_population) 
VALUES 	
('C1','London','England',8982000),
('C2','Athens','Greece',3154000),
('C3','Toronto','Canada',6197000); 
```

> Note that a successful command output should looks like this:
>
> ```shell
> Query OK, 3 rows affected (0.11 sec)
>    Records: 3  Duplicates: 0  Warnings: 0
> ```

13. Let us run our first query to extract all the data from the `cities` table. For this query, you will use the `SELECT` command, so run the following script.

```mysql
mysql> SELECT * FROM cities;

+---------+-----------+--------------+-----------------+
| city_id | city_name | city_country | city_population |
+---------+-----------+--------------+-----------------+
| C1      | London    | England      |         8982000 |
| C2      | Athens    | Greece       |         3154000 |
| C3      | Toronto   | Canada       |         6197000 |
+---------+-----------+--------------+-----------------+
3 rows in set (0.11 sec)
```

> The use of the `*` can help us to select all the available columns, so we can now extract and print all the columns and the data.
>
> :rotating_light: You can clear the terminal by pressing `ctl`+`L`. You can also bring up the previous commands by pressing the up button from the keyboard :arrow_up:. 
>
> * Press it, and you will see the last command.
> * Press up and down, and you will access all the previous commands.

14. You will create a new `actors` table and link it to the `cities` table. Each time we insert data into the actors table we will refer to the `city_id` of the `cities` table.

| actor_id | actor_name        | actor_age | actor_gender | **city_id** |
| -------- | ----------------- | --------- | ------------ | ----------- |
| A1       | Emilia  Clarke    | 34        | F            | C1          |
| A2       | Jennifer  Aniston | 51        | F            | C2          |
| A3       | Jim  Carrey       | 58        | M            | C3          |

The data model looks like the following figure.

![](images/er-1.png)

The table specification is as follows:

* `actor_id` includes characters and it is a primary key, so we will use the `VARCHAR(30)`.

* `actor_name` includes characters and is  `VARCHAR(30)`. This field cannot be empty.

* `actor_age` includes numbers, so we will use the `INT(8)`. 

* `actor_gender` includes characters, so we will use the `VARCHAR(10)`. This field cannot be empty.

* `city_id` is a foreign key to the `city_id` of the `cities` table.

> Note  that the **cities.city_id** and **actors.city_id** are exactly the same. This means that both are of the same data type VARCHAR(30).

15. The next command creates the `actors` table. 
    * Before typing it, spend a minute to examine the code.

```mysql
CREATE TABLE actors (
actor_id VARCHAR(30),
actor_name VARCHAR(30) NOT NULL,
actor_age INT(8),
actor_gender VARCHAR(30) NOT NULL,
city_id VARCHAR(30),
PRIMARY KEY (actor_id),
FOREIGN KEY (city_id) REFERENCES cities(city_id)
);
```

16. Now, let's insert the data.

```mysql
INSERT INTO actors VALUES 	
('A1','Emilia Clarke',34,'F','C1'),
('A2','Jennifer Aniston',51,'F','C2'),
('A3','Jim Carrey',58,'M','C3');  
```

17. Let's try to insert a new record as follows.

```mysql
INSERT INTO actors VALUES 	
('A4','Sarah Paulson',46,'F','C4');
```

18. This command will fail :rotating_light:

* Did you find the error?

```mysql
ERROR 1452 (23000): Cannot add or update a child row: a foreign key constraint fails (`steliosdb`.`actors`, CONSTRAINT `actors_ibfk_1` FOREIGN KEY (`city_id`) REFERENCES `cities` (`city_id`))
```

* The issue is that you are trying to insert data for a city with id `C4` that does not exist in the `cities`vtable. This is called **referential integrity**. To insert this record into the **actors** table you will need to insert a new city with `city_id` C4 in the `cities` table.

19. Insert the following record into the `cities`.

| city_id | city_name | city_country   | city_population |
| ------- | --------- | -------------- | --------------- |
| C4      | Tampa     | United  States | 392.890         |

* Run the folloiwing command.

```mysql
INSERT INTO cities VALUES
('C4','Tampa','United States',392890);
```

18. Now, record `C4` exists in the `cities` so let's insert once more `Sarah Paulson` record.

```mysql
INSERT INTO actors VALUES 	
('A4','Sarah Paulson',46,'F','C4');
```

19. Let's confirm that the new value is there.

```mysql
mysql> SELECT * FROM actors;
+----------+------------------+-----------+--------------+---------+
| actor_id | actor_name       | actor_age | actor_gender | city_id |
+----------+------------------+-----------+--------------+---------+
| A1       | Emilia Clarke    |        34 | F            | C1      |
| A2       | Jennifer Aniston |        51 | F            | C2      |
| A3       | Jim Carrey       |        58 | M            | C3      |
| A4       | Sarah Paulson    |        46 | F            | C4      |
+----------+------------------+-----------+--------------+---------+
4 rows in set (0.10 sec)
```

* Press `ctrl` and `L` to clear your screen.

20. Now we have our data linked and following the referential integrity, let's try to retrieve linked data. Let us query the actors and the cities table to show all the data using a cartesian product. This will show a combination of each possible match of record from both tables.
    * The output looks like this.

```mysql
mysql> SELECT * FROM actors,cities;
+----------+------------------+-----------+--------------+---------+---------+-----------+
| actor_id | actor_name       | actor_age | actor_gender | city_id | city_id | city_name | city_country  | city_population |
+----------+------------------+-----------+--------------+---------+---------+-----------+
| A4       | Sarah Paulson    |        46 | F            | C4      | C1      | London    | England       |      8982000 |
| A3       | Jim Carrey       |        58 | M            | C3      | C1      | London    | England       |      8982000 |
| A2       | Jennifer Aniston |        51 | F            | C2      | C1      | London    | England       |      8982000 |
| A1       | Emilia Clarke    |        34 | F            | C1      | C1      | London    | England       |      8982000 |
| A4       | Sarah Paulson    |        46 | F            | C4      | C2      | Athens    | Greece        |      3154000 |
| A3       | Jim Carrey       |        58 | M            | C3      | C2      | Athens    | Greece        |      3154000 |
| A2       | Jennifer Aniston |        51 | F            | C2      | C2      | Athens    | Greece        |      3154000 |
| A1       | Emilia Clarke    |        34 | F            | C1      | C2      | Athens    | Greece        |      3154000 |
| A4       | Sarah Paulson    |        46 | F            | C4      | C3      | Toronto   | Canada        |      6197000 |
| A3       | Jim Carrey       |        58 | M            | C3      | C3      | Toronto   | Canada        |      6197000 |
| A2       | Jennifer Aniston |        51 | F            | C2      | C3      | Toronto   | Canada        |      6197000 |
| A1       | Emilia Clarke    |        34 | F            | C1      | C3      | Toronto   | Canada        |      6197000 |
| A4       | Sarah Paulson    |        46 | F            | C4      | C4      | Tampa     | United States |       392890 |
| A3       | Jim Carrey       |        58 | M            | C3      | C4      | Tampa     | United States |       392890 |
| A2       | Jennifer Aniston |        51 | F            | C2      | C4      | Tampa     | United States |       392890 |
| A1       | Emilia Clarke    |        34 | F            | C1      | C4      | Tampa     | United States |       392890 |
+----------+------------------+-----------+--------------+---------+---------+-----------+
16 rows in set (0.11 sec)
```

:rotating_light: **We shouls avoid using this command, as it does not bring any useful results.**

21. Let us run an inner join query to combine the records according to the appropriate relationships that is the combination of primary and foreign keys. These are the `city_id` of the `cities` table and the `city_id` of the `actors` table.

> You can represent these as `cities.city_id` and `actors.city_id`

![](images/er-1.png)

* Run the following command to extract all the columns using the inner join.

```mysql
mysql> SELECT * FROM actors, cities WHERE actors.city_id=cities.city_id;
+----------+------------------+-----------+--------------+---------+---------+---------+
| actor_id | actor_name       | actor_age | actor_gender | city_id | city_id | city_name | city_country  | city_population |
+----------+------------------+-----------+--------------+---------+---------+---------+
| A1       | Emilia Clarke    |        34 | F            | C1      | C1      | London    | England       |         8982000 |
| A2       | Jennifer Aniston |        51 | F            | C2      | C2      | Athens    | Greece        |         3154000 |
| A3       | Jim Carrey       |        58 | M            | C3      | C3      | Toronto   | Canada        |         6197000 |
| A4       | Sarah Paulson    |        46 | F            | C4      | C4      | Tampa     | United States |          392890 |
+----------+------------------+-----------+--------------+---------+---------+---------+
4 rows in set (0.10 sec)
```

22. Which actors born in Toronto?
    * Let us select the `city_name`, `city_country` of cities table and the `actor_name` of ` actors` table for actors born in Toronto.

```mysql
SELECT cities.city_name, cities.city_country, actors.actor_name 
FROM actors,cities 
WHERE cities.city_name='Toronto' AND actors.city_id=cities.city_id;

+-----------+--------------+------------+
| city_name | city_country | actor_name |
+-----------+--------------+------------+
| Toronto   | Canada       | Jim Carrey |
+-----------+--------------+------------+
1 row in set (0.11 sec)
```

23 What is the population of the city that Jennifer Aniston born?

```mysql
SELECT actors.actor_name, cities.city_name, cities.city_population 
FROM actors,cities 
WHERE actors.actor_name='Jennifer Aniston' AND actors.city_id=cities.city_id;

+------------------+-----------+-----------------+
| actor_name       | city_name | city_population |
+------------------+-----------+-----------------+
| Jennifer Aniston | Athens    |         3154000 |
+------------------+-----------+-----------------+
1 row in set (0.11 sec)
```

24. Which actors born in a city with population greater than four million?

```mysql
SELECT actors.actor_name, cities.city_population 
FROM actors,cities 
WHERE cities.city_population>4000000 AND actors.city_id=cities.city_id;

+---------------+-----------------+
| actor_name    | city_population |
+---------------+-----------------+
| Emilia Clarke |         8982000 |
| Jim Carrey    |         6197000 |
+---------------+-----------------+
2 rows in set (0.11 sec)
```

25. Are there any female actors that born in Greece?

```mysql
SELECT actors.actor_name, actors.actor_gender, cities.city_country 
FROM actors,cities 
WHERE actors.actor_gender='F' AND cities.city_country='Greece' AND actors.city_id=cities.city_id;

+------------------+--------------+--------------+
| actor_name       | actor_gender | city_country |
+------------------+--------------+--------------+
| Jennifer Aniston | F            | Greece       |
+------------------+--------------+--------------+
1 row in set (0.11 sec)
```

26. How many actors born in a city with population greeter that four million?

```mysql
SELECT COUNT(actors.actor_name) AS counter_name
FROM actors,cities 
WHERE cities.city_population>4000000 AND actors.city_id=cities.city_id;

+--------------+
| counter_name |
+--------------+
|            2 |
+--------------+
1 row in set (0.11 sec)
```

27. How many female or male actors born in a city with population greeter than one million?

```mysql
SELECT actors.actor_gender,COUNT(actors.actor_gender) AS counter_gender
FROM actors,cities 
WHERE cities.city_population>1000000 AND actors.city_id=cities.city_id 
GROUP BY actors.actor_gender;
```

28. Well done :clap: , you completed the MySQL tutorial.

:checkered_flag: Well done! 