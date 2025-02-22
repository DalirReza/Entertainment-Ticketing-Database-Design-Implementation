SELECT p.username, COUNT(*) AS purchase_count
FROM purchase AS p
GROUP BY p.username
HAVING purchase_count = (
    SELECT MAX(purchase_count)
    FROM (
        SELECT COUNT(*) AS purchase_count
        FROM purchase
        GROUP BY username
    ) AS max_purchase_count_subquery
);