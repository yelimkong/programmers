-- 코드를 입력하세요
SELECT I.REST_ID,
       I.REST_NAME, 
       I.FOOD_TYPE,
       I.FAVORITES, 
       I.ADDRESS, 
       R.SCORE
    FROM REST_INFO I 
        INNER JOIN (
            SELECT REST_ID,
                ROUND(AVG(REVIEW_SCORE), 2) SCORE
            FROM REST_REVIEW R
         GROUP BY REST_ID
        ) AS R
    ON (I.REST_ID = R.REST_ID)
    GROUP BY I.ADDRESS
    HAVING I.ADDRESS LIKE '서울%'
    ORDER BY SCORE DESC, I.FAVORITES DESC;
    
