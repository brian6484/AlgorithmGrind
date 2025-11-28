-- 코드를 입력하세요
select a.USER_ID, a.NICKNAME, concat(a.CITY, " ", a.STREET_ADDRESS1, " ", a.STREET_ADDRESS2) as "전체주소", 
CONCAT(
    SUBSTRING(a.TLNO, 1, 3),
    '-',
    SUBSTRING(a.TLNO, 4, 4),
    '-',
    SUBSTRING(a.TLNO, 8, 4)
) AS "전화번호"
from USED_GOODS_USER a
join
(
SELECT count(WRITER_ID) as count, WRITER_ID 
FROM USED_GOODS_BOARD 
group by WRITER_ID
having count >=3
) t
on a.USER_ID = t.WRITER_ID
order by a.USER_ID desc