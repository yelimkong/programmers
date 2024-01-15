-- 코드를 입력하세요
-- 2021년에 가입한 전체 회원들 중 
-- 상품을 구매한 회원수와 상품을 구매한 회원의 비율(=2021년에 가입한 회원 중 상품을 구매한 회원수 / 2021년에 가입한 전체 회원 수)
-- 년, 월 별로 출력
-- 상품을 구매한 회원의 비율은 소수점 두번째자리에서 반올림
-- 전체 결과는 년을 기준으로 오름차순 정렬
-- 년이 같다면 월을 기준으로 오름차순 정렬

-- 1. 2021 가입한 전체 회원들
WITH TZTO AS (
    SELECT USER_ID, JOINED
    FROM USER_INFO 
    WHERE JOINED BETWEEN '2021-01-01' AND '2021-12-31' ),
    PURCHASED AS (
    SELECT YEAR(SALES_DATE) AS 'YEAR',
           MONTH(SALES_DATE) AS 'MONTH',
           COUNT(DISTINCT USER_ID) AS 'PUCHASED_USERS'
        FROM ONLINE_SALE 
        WHERE USER_ID IN (SELECT USER_ID FROM TZTO ) 
        GROUP BY YEAR(SALES_DATE) ,  MONTH(SALES_DATE)          
    ) 
    
# SELECT *
#     FROM TZTO;


# SELECT *
#     FROM PURCHASED ;


SELECT P.YEAR, P.MONTH, P.PUCHASED_USERS, 
        ROUND(P.PUCHASED_USERS / (SELECT COUNT(*) FROM TZTO), 1) AS 'PUCHASED_RATIO'
    FROM PURCHASED P
    ORDER BY P.YEAR, P.MONTH;

