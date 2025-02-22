SELECT t1.event_id, t1.name, t1.discount
FROM event AS t1
RIGHT JOIN Theatre AS t2
ON t2.event_id = t1.event_id
WHERE t1.discount IS NOT NULL;