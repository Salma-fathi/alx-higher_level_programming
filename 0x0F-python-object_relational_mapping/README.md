# 0x0F. Python - Object-relational mapping

## Introduction
This project focuses on bridging the worlds of Databases and Python by implementing Object-relational mapping (ORM) in Python using SQLAlchemy. By leveraging ORM, developers can abstract the storage details and interact with databases using Python objects rather than writing raw SQL queries. This project delves into utilizing modules like MySQLdb and SQLAlchemy to connect to MySQL databases, execute SQL queries, and manipulate data using Python code.

## Background Context
The project is divided into several tasks, each emphasizing different aspects of ORM and database interaction. From basic querying to handling user input and preventing SQL injections, the tasks aim to provide a comprehensive understanding of ORM concepts and practices.

## Resources
Before diving into the project, it's recommended to go through some tutorials and documentation related to ORM and SQLAlchemy. Here are some resources to get started:
- [Object-relational mappers](https://en.wikipedia.org/wiki/Object-relational_mapping)
- [MySQLdb documentation](https://mysqlclient.readthedocs.io/user_guide.html)
- [SQLAlchemy documentation](https://docs.sqlalchemy.org/en/14/)
- [SQLAlchemy Tutorial](https://leportella.com/sqlalchemy-tutorial/)

## Learning Objectives
At the completion of this project, participants are expected to grasp the following concepts:
- Understanding the benefits of using Python for database interactions
- Connecting to a MySQL database from Python
- Performing CRUD operations (Create, Read, Update, Delete) using Python code
- Implementing ORM to map Python classes to database tables
- Creating Python Virtual Environments for managing dependencies

## Requirements
- Development Environment: Ubuntu 20.04 LTS
- Python Version: 3.8.5
- Database: MySQL
- Modules: MySQLdb (version 2.0.x), SQLAlchemy (version 1.4.x)
- Editor: vi, vim, emacs

## Setup Instructions
1. Install MySQL 8.0 on Ubuntu 20.04. Refer to [MySQL installation guide](https://dev.mysql.com/doc/mysql-installation-excerpt/8.0/en/)
2. Install Python 3.8.5 and required modules:
    ```
    $ sudo apt-get install python3.8-venv
    $ python3 -m venv venv
    $ source venv/bin/activate
    $ sudo apt-get install python3-dev
    $ sudo apt-get install libmysqlclient-dev
    $ sudo apt-get install zlib1g-dev
    $ sudo pip3 install mysqlclient
    $ sudo pip3 install SQLAlchemy
    ```
3. Clone the project repository:
    ```
    $ git clone https://github.com/username/alx-higher_level_programming.git
    ```
4. Navigate to the project directory:
    ```
    $ cd alx-higher_level_programming/0x0F-python-object_relational_mapping
    ```

## Tasks Overview
- **Task 0:** Retrieve all states from the database
- **Task 1:** Filter states by name
- **Task 2:** Filter states by user input securely
- **Task 3:** Prevent SQL Injection vulnerability
- **Task 4:** List all cities from the database
- **Task 5:** List all cities by state
- **Task 6:** Implement the State class using SQLAlchemy ORM
- **7-model_state_fetch_all.py**
   - Purpose: Lists all State objects from the database.
   - Usage: 
     ```
     ./7-model_state_fetch_all.py <mysql_username> <mysql_password> <database_name>
     ```
- **8-model_state_fetch_first.py**
   - Purpose: Prints the first State object from the database.
   - Usage: 
     ```
     ./8-model_state_fetch_first.py <mysql_username> <mysql_password> <database_name>
     ```

- **9-model_state_filter_a.py**
   - Purpose: Lists all State objects that contain the letter 'a'.
   - Usage: 
     ```
     ./9-model_state_filter_a.py <mysql_username> <mysql_password> <database_name>
     ```

- **10-model_state_my_get.py**
   - Purpose: Prints the State object with the specified name from the database.
   - Usage: 
     ```
     ./10-model_state_my_get.py <mysql_username> <mysql_password> <database_name> <state_name>
     ```

- **11-model_state_insert.py**
   - Purpose: Adds the State object "Louisiana" to the database.
   - Usage: 
     ```
     ./11-model_state_insert.py <mysql_username> <mysql_password> <database_name>
     ```

- **12-model_state_update_id_2.py**
   - Purpose: Changes the name of the State object with id=2 to "New Mexico".
   - Usage: 
     ```
     ./12-model_state_update_id_2.py <mysql_username> <mysql_password> <database_name>
     ```

- **13-model_state_delete_a.py**
   - Purpose: Deletes all State objects with a name containing the letter 'a'.
   - Usage: 
     ```
     ./13-model_state_delete_a.py <mysql_username> <mysql_password> <database_name>
     ```

- **model_city.py**
   - Purpose: Contains the definition of the City class.

- **14-model_city_fetch_by_state.py**
   - Purpose: Prints all City objects from the database along with their corresponding State.
   - Usage: 
     ```
     ./14-model_city_fetch_by_state.py <mysql_username> <mysql_password> <database_name>
     ```

- **relationship_city.py**
    - Purpose: Contains the definition of the City class with a relationship to the State class.

- **relationship_state.py**
    - Purpose: Contains the definition of the State class with a relationship to the City class.

- **100-relationship_states_cities.py**
    - Purpose: Creates the State "California" with the City "San Francisco" in the database.
    - Usage: 
      ```
      ./100-relationship_states_cities.py <mysql_username> <mysql_password> <database_name>
      ```

- **101-relationship_states_cities_list.py**
    - Purpose: Lists all State objects and their corresponding City objects from the database.
    - Usage: 
      ```
      ./101-relationship_states_cities_list.py <mysql_username> <mysql_password> <database_name>
      ```

- **102-relationship_cities_states_list.py**
    - Purpose: Lists all City objects from the database along with their corresponding State.
    - Usage: 
      ```
      ./102-relationship_cities_states_list.py <mysql_username> <mysql_password> <database_name>
      ```

### Conclusion
These scripts provide a comprehensive toolkit for interacting with a MySQL database using SQLAlchemy in Python. Each script addresses a specific requirement outlined in the project specifications, allowing for efficient manipulation and management of database records.
