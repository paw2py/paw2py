Input: 
Logs table:
+----+-----+
| id | num |
+----+-----+
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
+----+-----+
Output: 
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
Explanation: 1 is the only number that appears consecutively for at least three times.
# Write your MySQL query statement below
with base as (
select num,num*3 as re, lead(num) over (order by id) as  nxt, lead(num,2) over (order by id)  as nxt_2 from logs
)
select num as ConsecutiveNums from base where re = num+nxt+nxt_2;
