#!/usr/bin/env python
import psycopg2
import os

# this program allow querying the news db provided as part of the IPND
# nanodegree backend project, and to get back results for different questions
# about the data included.

# create views to prepare the data for each analysis.
os.system('psql -d news -a -f page_views.sql')
os.system('psql -d news -a -f author_views.sql')
os.system('psql -d news -a -f errorlogs.sql')

# connect to the new database via the postgresql module
c = psycopg2.connect("dbname=news")
cursor = c.cursor()

# 1. What are the most popular three articles of all time?

# get the article titles and their count from the view "top_articles"
cursor.execute(
    "select title,count from top_articles")
results = cursor.fetchall()

# format the result as an easy to read list
print "\n1. WHAT ARE THE MOST POPULAR THREE ARTICLES OF ALL TIME?\n"
for title, number in results:
    print '"'+title+'" - ' + str(number) + ' views'
# for title, number in zip(articles, views):
#     title = "".join(title)
#     number = number[0]
#     print '"'+title+'" - ' + str(number) + ' views'

# 2. Who are the most popular article authors of all time?

# get the author names and their total page view count
# from the view "top_authors"
cursor.execute(
    "select name, sum from top_authors")
results = cursor.fetchall()

# format the result as an easy to read list
print "\n2. WHO ARE THE MOST POPULAR ARTICLE AUTHORS OF ALL TIME?\n"
for name, sum in results:
    print '"'+name+'" - ' + str(sum) + ' views'

# 3. On which days did more than 1% of requests lead to errors?
cursor.execute(
    "select dates, percent from percentages")
results = cursor.fetchall()

# format the result as an easy to read list
print "\n1. ON WHICH DAYS DID MORE THAN 1% OF REQUESTS LEAD TO ERRORS?\n"
for day, number in results:
    day = str(day[0])
    number = str(number[0])
    number = "".join(number)

    print day+' - ' + number + '% errors\n'

c.close()
