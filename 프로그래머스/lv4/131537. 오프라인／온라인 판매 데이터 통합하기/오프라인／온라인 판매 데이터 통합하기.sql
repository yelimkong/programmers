-- 코드를 입력하세요
/*
목적 :
아웃풋 : 판매 날짜, 상품ID, 유저ID, 판매량
조건
1. 대상기간 : 2022년 3월
2. OFFLINE_SALE 테이블의 판매 데이터의 USER_ID 값은 NULL 로 표시해주세요
3. 판매일을 기준으로 오름차순 정렬
4. 상품 ID를 기준으로 오름차순
5. 유저 ID를 기준으로 오름차순 정렬



*/

SELECT 
    DATE_FORMAT(SALES_DATE,"%Y-%m-%d") AS SALES_DATE
    ,PRODUCT_ID
    ,USER_ID
    ,SALES_AMOUNT 
FROM ONLINE_SALE 
WHERE 
    SALES_DATE >='2022-03-01 00:00:00' AND SALES_DATE <'2022-04-01 00:00:00'

UNION ALL
SELECT 
    DATE_FORMAT(SALES_DATE,"%Y-%m-%d") AS SALES_DATE
    ,PRODUCT_ID
    , null AS user_id
    , SALES_AMOUNT 
FROM OFFLINE_SALE
WHERE 
    SALES_DATE >='2022-03-01 00:00:00' AND SALES_DATE <'2022-04-01 00:00:00'
ORDER BY 1,2,3