# 0x0D. SQL - Introduction

This project is about basic use of DBMS, DDL and DML project on MySQL (A Relational Datatabase Managment System).

## Tasks:

Exist two types of tasks in this project:

- Mandatory
- Advanced

### Mandatory

- **0-list_databases.sql** &rarr; Lists all databases of your MySQL server.

- **1-create_database_if_missing.sql** &rarr; Creates the database hbtn_0c_0 in your MySQL server.

	- If the database hbtn_0c_0 already exists, your script should not fail

- **2-remove_database.sql** &rarr; Deletes the database hbtn_0c_0 in your MySQL server.

	- If the database hbtn_0c_0 doesn’t exist, your script should not fail

- **3-list_tables.sql** &rarr; Lists all the tables of a database in your MySQL server.

	- The database name will be passed as argument of mysql command

- **4-first_table.sql** &rarr; Creates a table called first_table in the current database in your MySQL server.

	### first_table description:
		- id INT
		- name VARCHAR(256)
	- The database name will be passed as an argument of the mysql command
	- If the table first_table already exists, your script should not fail

- **5-full_table.sql** &rarr; Prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.

	- The database name will be passed as an argument of the mysql command

- **6-list_values.sql** &rarr; lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.

	- All fields should be printed
	- The database name will be passed as an argument of the mysql command

- **7-insert_value.sql** &rarr; Inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.

	### Format:
		New row:
		id = 89
		name = Best School

	- The database name will be passed as an argument of the mysql command

- **8-count_89.sql** &rarr; Displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.

- **9-full_creation.sql** &rarr; Creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.

- **10-top_score.sql** &rarr; Lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

- **11-best_score.sql** &rarr; Lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.

- **12-no_cheating.sql** &rarr; Updates the score of Bob to 10 in the table second_table.

- **13-change_class.sql** &rarr; Removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.

- **14-average.sql** &rarr; Computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server.

- **15-groups.sql** &rarr; Lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.

- **16-no_link.sql** &rarr; Lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

### Advanced

- **100-move_to_utf8.sql** &rarr; Converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.

- **101-avg_temperatures.sql** &rarr; Displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

- **102-top_city.sql** &rarr; Displays the top 3 of cities temperature during July and August ordered by temperature (descending)

- **103-max_state.sql** &rarr; Displays the max temperature of each state (ordered by State name).
