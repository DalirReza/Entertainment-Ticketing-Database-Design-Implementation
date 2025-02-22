SELECT t1.event_id 
FROM cast_occupation AS t1
LEFT JOIN cast AS t2
ON t1.Cast_ID = t2.Cast_ID
WHERE t2.First_name = 'امیر علی'
AND t2.Last_name = 'میردامادی';