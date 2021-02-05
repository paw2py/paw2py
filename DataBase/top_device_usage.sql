Table structure device_usage(account_id ,device_id,play_time,play_date)

values:
insert into device_usage('a1','d1',30,'01-June-2019');
insert into device_usage('a1','d1',10,'01-June-2019');
insert into device_usage('a1','d1',5,'01-June-2019');
insert into device_usage('a1','d1',60,'01-June-2019');
insert into device_usage('a1','d2',20,'01-June-2019');
insert into device_usage('a1','d2',10,'01-June-2019');
insert into device_usage('a1','d2',5,'01-June-2019');
insert into device_usage('a1','d2',4,'01-June-2019');


insert into device_usage('a2','d1',30,'01-June-2019');
insert into device_usage('a2','d1',10,'01-June-2019');
insert into device_usage('a2','d1',5,'01-June-2019');
insert into device_usage('a2','d1',60,'01-June-2019');
insert into device_usage('a2','d2',20,'01-June-2019');
insert into device_usage('a2','d2',10,'01-June-2019');
insert into device_usage('a2','d2',5,'01-June-2019');
insert into device_usage('a2','d2',100,'01-June-2019');

#we want to find the account_id and device_id that was used the most , 
#this can be done by sum(play_time) for respective account_id and device_id for give month June

#get records for month June =6
with base as (
Select account_id,device_id,play_time from device_usage where extract(MONTH FROM play_date) =  6
),
sum_device(
select account_id,device_id,play_time, sum(play_time) over (partition by account_id,device_id) as sm 
from base
),
Top_device as(
select account_id,device_id, row_number() over (partition by account_id order by sm desc) as rn from sum_device
)
select account_id,device_id from top_device where rn =1 ;
