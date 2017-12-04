# Udacity IPND Final Project Submission

## About
This is the final project of the Udacity ["Introduction to Programming Nanodegree"](https://www.udacity.com/course/intro-to-programming-nanodegree--nd000), following the backend development path. The objective of this program is to connect to an SQL database and return different statistics in a readable format.

## Setup
We shall assume that you have your environment setup as per the instructions in the Logs Analysis Project: [Lesson 3: Prepare the software and data.](https://classroom.udacity.com/nanodegrees/nd000/parts/b910112d-b5c0-4bfe-adca-6425b137ed12/modules/a3a0987f-fc76-4d14-a759-b2652d06ab2b/lessons/0aa64f0e-30be-455e-a30d-4cae963f75ea/concepts/a9cf98c8-0325-4c68-b972-58d5957f1a91)
Once you have the vagrant VM setup installed, [download the data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) needed to set up the news database. Then set up the news database with the following command:
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
