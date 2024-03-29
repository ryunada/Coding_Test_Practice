-- 코드를 입력하세요
SELECT FO.PRODUCT_ID AS PRODUCT_ID, FP.PRODUCT_NAME AS PRODUCT_NAME, SUM(FO.AMOUNT * FP.PRICE) AS TOTAL_SALES
FROM FOOD_ORDER AS FO LEFT JOIN FOOD_PRODUCT AS FP ON FO.PRODUCT_ID = FP.PRODUCT_ID
WHERE FO.PRODUCE_DATE LIKE '2022-05%'
GROUP BY FO.PRODUCT_ID
ORDER BY TOTAL_SALES DESC, FO.PRODUCT_ID


