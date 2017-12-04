#!/usr/bin/env python
import psycopg2
import os

# this program allow querying the news db provided as part of the IPND
# nanodegree backend project, and to get back results for different questions
# about the data included.

# connect to the new database via the postgresql module
c = psycopg2.connect("dbname=news")
cursor = c.cursor()
os.system('psql -d news -a -f page_views.sql')
os.system('psql -d news -a -f author_views.sql')
os.system('psql -d news -a -f errorlogs.sql')


# 1. What are the most popular three articles of all time?

# get the article titles and their count from the view "top_articles"
cursor.execute(
    "select title from top_articles")
articles = cursor.fetchall()
cursor.execute(
    "select count from top_articles")
views = cursor.fetchall()

# format the result as an easy to read list
print "\n1. WHAT ARE THE MOST POPULAR THREE ARTICLES OF ALL TIME?\n"
for title, number in zip(articles, views):
    title = "".join(title)
    number = number[0]
    print '"'+title+'" - ' + str(number) + ' views'

# 2. Who are the most popular article authors of all time?

# get the author names and their total page view count
# from the view "top_authors"
cursor.execute(
    "select name from top_authors")
authors = cursor.fetchall()
cursor.execute(
    "select sum from top_authors")
totals = cursor.fetchall()

# format the result as an easy to read list
print "\n2. WHO ARE THE MOST POPULAR ARTICLE AUTHORS OF ALL TIME?\n"
for name, number in zip(authors, totals):
    name = "".join(name)
    number = number[0]
    print '"'+name+'" - ' + str(number) + ' views'

# 3. On which days did more than 1% of requests lead to errors?
cursor.execute(
    "select dates from percentages")
dates = cursor.fetchall()
cursor.execute(
    "select percent from percentages")
percent = cursor.fetchall()

# format the result as an easy to read list
print "\n1. ON WHICH DAYS DID MORE THAN 1 PERCENT OF REQUESTS LEAD TO ERRORS?"
for day, number in zip(dates, percent):
    day = str(day[0])
    number = str(number[0])
    number = "".join(number)

    print day+' - ' + number + '% errors\n'

c.close()
