<br>

<h1 align='center'>Python<br>ORM - Object-relational mapping<br>
<img src='https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue'><img src='https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white'>
</h1>

<br>

## Background Context

In this project, you will link two amazing worlds: **Databases and Python!**

In the first part, you will use the module `MySQLdb` to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module `SQLAlchemy` (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

## Resources

**Read or watch**

- [Object-relational Mappers (ORMs)](https://www.fullstackpython.com/object-relational-mappers-orms.html)
- [Python and MySQL Database: A Practical Introduction](https://realpython.com/python-mysql/)
- [Python MySQL](https://www.mikusa.com/python-mysql-docs/index.html)
- [MySQLdb's documentation!](https://mysqlclient.readthedocs.io/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/14/)
- [SQLAlchemy Tutorial](https://j2logo.com/python/sqlalchemy-tutorial-de-python-sqlalchemy-guia-de-inicio/)
- [Flask SQLAlchemy](https://www.youtube.com/playlist?list=PLXmMXHVSvS-BlLA5beNJojJLlpE0PJgCW)
- [SQLAlchemy CheatSheet](https://www.pythonsheets.com/notes/python-sqlalchemy.html)

## Learning Objectives

- Why Python programming is awesome
- How to connect to a MySQL database from a Python script
- How to `SELECT` rows in a MySQL table from a Python script
- How to `INSERT` rows in a MySQL table from a Python script
- What ORM means
- How to map a Python Class to a MySQL table

## More Info

### Install MySQLdb module version 2.0.x

For installing MySQLdb, you need to have MySQL installed: [How to install MySQL 8.0 in Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)

```python
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)
```

### Install SQLAlchemy module version 1.4.x

```python
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'
``bash
```
