-- 2. Who are the most popular article authors of all time?

-- Create a view (“page_views”) to get the total number of page views
-- for each article (articles can be identified by the last part of the
-- url (“path” column), which matches the  column “slugs” in the table “articles”.
-- Remove the  ‘/articles/‘ in every url using a regular expression
create or replace view page_views as
select (regexp_replace(path, '/article/','')) as path, count(status) from log
where status = '200 OK'
and path != '/'
group by path
order by count desc;

-- Join the author colum from articles & sum page_views
-- for all articles of each author.
create or replace view author_pageviews as
select sum(page_views.count), articles.author
from page_views join articles
on page_views.path = articles.slug
group by author
order by sum desc;

--Create view “top_authors” with the author name & count sorted by count
create view top_authors as
select authors.name, author_pageviews.sum
from authors join  author_pageviews
on authors.id = author_pageviews.author;

--Print view to csv file
\copy (select * from top_authors) To '/vagrant/author_views_output.csv' With CSV Header
