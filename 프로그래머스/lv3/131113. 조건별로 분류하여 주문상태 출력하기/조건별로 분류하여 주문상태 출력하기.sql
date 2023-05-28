-- 코드를 입력하세요
SELECT order_id, product_id, TO_CHAR(out_date, 'yyyy-MM-dd'),
    CASE WHEN out_date <= TO_DATE('2022-05-01', 'yyyy-MM-dd') THEN '출고완료'
         WHEN out_date > TO_DATE('2022-05-01', 'yyyy-MM-dd') THEN '출고대기'
         ELSE '출고미정'
    END AS "출고여부"
FROM food_order
ORDER BY order_id