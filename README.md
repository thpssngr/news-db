# Udacity IPND Final Project Submission

## About
This is the final project of the Udacity ["Introduction to Programming Nanodegree"](https://www.udacity.com/course/intro-to-programming-nanodegree--nd000), following the backend development path. The objective of this program is to connect to an SQL database and return different statistics in a readable format.

## Setup
If you haven't, first set up the news database with the following command:
```sh
psql -d news -f newsdata.sql
```

Execute the python file "newsqueries.py", to get the query results.

## SQL queries
The file will access the news database and return some queries as views that are used to get the answers for the different questions:

* page_views.sql contains the query to get back the information on the most popular articles of all times
* author_views.sql returns the results about the most popular author
* errorlogs.sql will provide information about the error % on different days

(the views created are described in more detail in each sql file)
