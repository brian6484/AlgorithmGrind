-- 코드를 작성해주세요
select 
count(*) as FISH_COUNT,
max(coalesce(LENGTH,10)) as MAX_LENGTH,
FISH_TYPE
from FISH_INFO 
group by FISH_TYPE
having avg(coalesce(LENGTH,10)) >=33
ORDER BY FISH_TYPE;