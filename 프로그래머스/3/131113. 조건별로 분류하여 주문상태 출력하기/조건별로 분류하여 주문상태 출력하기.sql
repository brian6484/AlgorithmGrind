-- 코드를 입력하세요
SELECT order_id, product_id, left(out_date,10) as out_date, 
case
when out_date <= '2022-05-01' then '출고완료'
when out_date >  '2022-05-01' then '출고대기'
else '출고미정'
end as 출고여부
from food_order
order by order_id asc