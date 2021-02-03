##Differece b/w Not In and NOT EXISTS
 
 NOT IN dose not see NULL VALUE in column . if we want to find the list of employes from emp table who are not managers . NOT IN will give 0 result .
 Apprantly not all employes can be manager . This can be solved by NOT EXISTS CLAUSE. 
 
 Create table emp (id number(20),emp_name varchar2(255),manager_id number(20),salary number(20));
 
 insert into emp values(1,'paw',2,2000);
 insert into emp values(2,'bij',null,2000);
 insert into emp values(3,'lak',2,2000);
 insert into emp values(4,'Sid',2,2000);
 insert into emp values(5,'jas',null,2000);
 insert into emp values(6,'dan',5,2000);
 insert into emp values(7,'lav',5,2000);
 insert into emp values(8,'vig',5,2000);
 
 commit;
 
 #Find all emp that are not Managers:
   1) Using NOT IN: select count(1) from emp where id NOT IN (select manager_id from emp) ---> This will resulet in count = 0 , as NOT IN fails to read NULL values
   
   2) Using NOT EXISTS : select count(1) from emp em where NOT EXISTS (select 1 from emp mgr where mgr.manager_id =  em.id) --> This will retrun count = 6 . 