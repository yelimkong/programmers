-- 코드를 입력하세요
-- 년, 월, 성별 별로 상품을 구매한 회원수를 집계
-- 년, 월, 성별을 기준으로 오름차순 정렬
-- 성별 정보가 없는 경우 결과에서 제외
SELECT YEAR(SALES_DATE) AS "YEAR", MONTH(SALES_DATE) AS "MONTH", GENDER, COUNT(DISTINCT(O.USER_ID)) AS "USERS"
    FROM ONLINE_SALE AS O INNER JOIN USER_INFO AS U 
    ON O.USER_ID = U.USER_ID
    WHERE U.GENDER IS NOT NULL
    GROUP BY MONTH, GENDER
    ORDER BY  1, 2, 3 ASC;
                                                                         
