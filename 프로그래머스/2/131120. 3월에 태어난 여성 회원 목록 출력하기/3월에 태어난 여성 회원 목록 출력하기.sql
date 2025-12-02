-- 코드를 입력하세요
SELECT MEMBER_ID	,MEMBER_NAME	,GENDER	, SUBSTRING(DATE_OF_BIRTH,1,10)
from MEMBER_PROFILE 
where tlno is not null
and gender = 'W'
and MONTH(DATE_OF_BIRTH)=3
order by member_id asc