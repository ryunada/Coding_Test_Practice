# version.1 
SELECT CART_ID
FROM CART_PRODUCTS
WHERE NAME = 'Milk' AND CART_ID IN(
    SELECT CART_ID
    FROM CART_PRODUCTS
    WHERE NAME = 'Yogurt'
)
ORDER BY CART_ID

# version.2 
SELECT CART_ID
FROM CART_PRODUCTS
WHERE NAME IN ('Milk','Yogurt')
GROUP BY CART_ID
HAVING COUNT(DISTINCT NAME)>1
