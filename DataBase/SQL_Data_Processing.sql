###########
nOTE: MANAGER_STAT table will have the rspective column as 
Manager_Id
Manager
Number_of_Employees
Average_Salary_Under_manager
###########

Merge INTO MANAGER_STAT mgr_stat
 USING (select manager_id,manager,emp_cnt,avg_sal from (
			select mgr.manager_id , mgr.emp_name as manager, 
			count(1) over(partiton by mgr.manager_id ) as emp_cnt,
			avg(salary) over(partiton by mgr.manager_id) as avg_sal
			,row_number() over (partiton by mgr.managear_id order by mgr.manager_id) as rn
			from employee emp,employee mgr 
			where emp.emp_id = mgr.managear_id) where rn =1) base
   ON  (MGR_sTAT.manager_id = base.manager_id)  
  WHEN MATCHED THEN 
   UPDATE SET mgr_stat.manager = base.manager,
              mgr.number_of_employees = base.emp_cnt,
              mgr.average_salary_under_manager = base.avg_sal
  WHEN NOT MATCHED THEN
    INSERT (manager_id,manager,number_of_employees,average_salary_under_manager)
    VALUES(base.managear_id,base.manager,base.emp_cnt,base.avg_sal);


at line 16 there should not be where conditon .

--this is what we want
with base as (
select manager_id,count(1) over (partition by manager_id) as emp_cnt,
avg(salary) over (partition by manager_id) as avg_sal,
rom_number() over (partition by manager_id order by manager_id) as rn
from employees
)
select b.manager_id,e.emp_name as manager,b.emp_cnt,b.avg_sal from base b 
join employee e on (b.manager_id = e.emp_id)
where b.rn = 1

--final query witih merger
Merge inot MANAGER_STAT mgr_stat 
 USING( 
with base as (
select manager_id,count(1) over (partition by manager_id) as emp_cnt,
avg(salary) over (partition by manager_id) as avg_sal,
rom_number() over (partition by manager_id order by manager_id) as rn
from employees
)
select b.manager_id,e.emp_name as manager,b.emp_cnt,b.avg_sal from base b 
join employee e on (b.manager_id = e.emp_id)
where b.rn = 1
) upd
ON (mgr_stat.manager_id = upd.manager_id)
WHEN MATCHED THEN
	UPDATE SET mgr_stat.manager = upd.manager,
			   mgr_stat.number_of_employees = upd.emp_cnt,
			   mgr_stat.average_salary_under_manager = upd.avg_sal
WHEN NOT MATCHED THEN
	INSERT INTO MANAGER_STAT(manager_id,manager,number_of_employees,average_salary_under_manager)
	VALUES(upd.manager_id,upd.manager,upd.emp_cnt,upd.avg_sal);
	
				

----solution using connect by to get the hierarchical infomaion of emp , and connect_by_root will get the respctive manager name from root .
select manager_id,connect_by_root emp_name as manager,
count(1) over (partition by manager_id) as emp_cnt,
avg(salary) over (partition by manager_id) as avg_sal,
rom_number() over (partition by manager_id order by manager_id) as rn
from employees 
connect by prior emp_id = manager_id start with manager_id is not null