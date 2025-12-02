-- 코드를 입력하세요
SELECT  floor(price/10000)*10000 as PRICE_GROUP, count(*) as PRODUCTS 
from product 
group by price_group
ORDER BY PRICE_GROUP asc