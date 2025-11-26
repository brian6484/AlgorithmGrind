-- 코드를 작성해주세요
select e.ID,
coalesce((select count(*)
 from ECOLI_DATA t
 where e.ID= t.PARENT_ID),0) as CHILD_COUNT
from ECOLI_DATA e