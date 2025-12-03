-- 코드를 작성해주세요
select 
case
    when month(DIFFERENTIATION_DATE)<=3 then '1Q'
    when month(DIFFERENTIATION_DATE)<=6 then '2Q'
    when month(DIFFERENTIATION_DATE)<=9 then '3Q'
    else '4Q'
end as 'QUARTER',
count(*) as ECOLI_COUNT
from ECOLI_DATA 
group by QUARTER
order by QUARTER asc
