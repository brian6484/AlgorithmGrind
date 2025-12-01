-- 코드를 작성해주세요
select sum(PRICE) as total_price
from item_info a
where a.rarity = "legend"