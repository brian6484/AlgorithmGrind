-- 코드를 작성해주세요
select a.ID, c.FISH_NAME, a.LENGTH
from FISH_INFO a
join 
(select FISH_TYPE, coalesce(max(LENGTH),0) as MAX_LENGTH
from FISH_INFO 
where LENGTH is not null
group by FISH_TYPE) 
b
on a.FISH_TYPE = b.FISH_TYPE
and a.LENGTH = b.MAX_LENGTH
join FISH_NAME_INFO c
on a.FISH_TYPE = c.FISH_TYPE
order by a.ID ASC