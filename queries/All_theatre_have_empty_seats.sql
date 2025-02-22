SELECT e.Event_ID FROM event AS e
INNER JOIN 
(SELECT Event_ID FROM seat_status AS s
INNER JOIN session AS sess
ON sess.Session_no = s.Session_no
WHERE s.Status=0
GROUP BY Event_ID) AS m
ON e.Event_ID = m.Event_ID
WHERE Event_type = "theatre";