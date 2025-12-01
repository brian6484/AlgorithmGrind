-- 코드를 작성해주세요
select distinct a.id, a.email, a.first_name, a.last_name
from developers a
join SKILLCODES b
on a.skill_code & b.code = b.code
WHERE b.NAME IN ('Python', 'C#')
order by a.id asc