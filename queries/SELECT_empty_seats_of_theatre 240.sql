SELECT Seat_no FROM seat_status AS s
INNER JOIN session as sess 
ON sess.Session_no = s.Session_no
WHERE s.Status=0 AND sess.Event_ID=240;