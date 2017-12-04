-- 3. On which days did more than 1% of requests lead to errors?
-- create a temporary table containing only the count of error messages,
-- grouped by days
create or replace view error_log as
select date(time) as errordates, count(status) as errorstatus
from log
where status = '404 NOT FOUND'
group by date(time)
;

-- create a temporary table containing only the count of all status messages,
-- grouped by days
create or replace view requests as
select date(time) as requestdates, count(status) as requeststatus
from log
group by date(time)
;

-- create a temporary table to calculate the percentage of error requests out
-- of all requests, grouped by days
create or replace view errors as
select error_log.errordates as dates,
((errorstatus * 100.00 / requeststatus)::decimal(4,2)) as percent
from error_log join requests
on error_log.errordates = requests.requestdates
;

-- create a view to select the days from errors where there are more than
-- 1% error messages
create or replace view percentages as
select dates, percent
from errors
where percent > 1.0
;

--Print view to csv file
\copy (select * from percentages) To '/vagrant/errorlogs_output.csv' With CSV Header
