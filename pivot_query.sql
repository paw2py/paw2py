
#Pivot the Occupation column in OCCUPATIONS so that each Name is sorted alphabetically and displayed underneath its corresponding Occupation. 
#The output column headers should be Doctor, Professor, Singer, and Actor, respectively.

Note: Print NULL when there are no more names corresponding to an occupation.

Input Format

The OCCUPATIONS table is described as follows:



Occupation will only contain one of the following values: Doctor, Professor, Singer or Actor.

Sample Input



Sample Output

Jenny    Ashley     Meera  Jane
Samantha Christeen  Priya  Julia
NULL     Ketty      NULL   Maria
Explanation

The first column is an alphabetically ordered list of Doctor names.
The second column is an alphabetically ordered list of Professor names.
The third column is an alphabetically ordered list of Singer names.
The fourth column is an alphabetically ordered list of Actor names.
The empty cell data for columns with less than the maximum number of names per occupation (in this case, the Professor and Actor columns) are filled with NULL values.

---solution----
with base as (
select name,occupation , row_number() over(partition by occupation order by name) as rn from 
occupations),
result as (
select doc,pro,sing,act from base
pivot(
max(name) FOR occupation in  
    ('Doctor' as doc,
     'Professor' as pro,
     'Singer' as sing,
     'Actor' as act
    )
))
select doc,pro,sing,act from result order by doc,pro,sing,act;
