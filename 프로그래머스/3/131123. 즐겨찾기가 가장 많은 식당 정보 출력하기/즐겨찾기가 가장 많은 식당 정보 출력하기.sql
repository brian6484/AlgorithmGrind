-- 코드를 입력하세요
SELECT food_type, rest_id, rest_name, favorites
from REST_INFO 
join 
(
select food_type as type, max(favorites) as cnt
from REST_INFO 
group by food_type
) t
on food_type = type
where favorites = cnt
order by food_type desc