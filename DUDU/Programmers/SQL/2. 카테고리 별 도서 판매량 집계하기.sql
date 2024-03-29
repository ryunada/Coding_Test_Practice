SELECT b.CATEGORY
     , SUM(bs.SALES) AS TOTAL_SALES
FROM BOOK AS b
INNER JOIN BOOK_SALES AS bs ON b.BOOK_ID = bs.BOOK_ID
WHERE bs.SALES_DATE LIKE '2022-01%'
GROUP BY b.CATEGORY
ORDER BY b.CATEGORY
