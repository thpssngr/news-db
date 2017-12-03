-- 1. What are the most popular three articles of all time?

-- Create a view (“page_views”) to get the total number of page views
-- for each article (articles can be identified by the last part of the
--url (“path” column), which matches the  column “slugs” in the table “articles”.
-- remove the  ‘/articles/‘ in every url using a regular expression
create or replace view page_views as
select (regexp_replace(path, '/article/','')) as path, count(status) from log
where status = '200 OK'
and path != '/'
group by path
order by count desc;

--Create view “top_articles” with the top 3 article name & count sorted by count
create or replace view top_articles as
select articles.title, page_views.count
from articles join page_views
on articles.slug = page_views.path
order by count desc
limit 3
;

--Print view to csv file
\copy (select * from top_articles) To '/vagrant/news/page_views_output.csv' With CSV Header
