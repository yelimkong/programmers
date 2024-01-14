-- FOOD_PRODUCT 테이블에서 식품분류별로 가격이 제일 비싼 
-- 가격이 제일 비싼 식품의 분류, 가격, 이름을 조회
-- 식품분류가 '과자', '국', '김치', '식용유'인 경우만 출력
-- 식품 가격을 기준으로 내림차순 정렬

WITH MAXPRICE AS (
    SELECT CATEGORY, MAX(PRICE) AS "MAX_PRICE"
    FROM FOOD_PRODUCT 
    WHERE CATEGORY IN ('과자', '국', '김치', '식용유')
    GROUP BY CATEGORY)
    
SELECT M.CATEGORY, M.MAX_PRICE, P.PRODUCT_NAME
    FROM MAXPRICE M INNER JOIN FOOD_PRODUCT P
    ON (M.CATEGORY = P.CATEGORY
       AND M.MAX_PRICE = P.PRICE)
    ORDER BY M.MAX_PRICE DESC;