

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