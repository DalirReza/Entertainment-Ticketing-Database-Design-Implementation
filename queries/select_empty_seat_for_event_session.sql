SELECT t1.Seat_no AS seatNum
FROM seat_status AS t1
LEFT JOIN session AS t2
ON t1.Session_no = t2.Session_no
WHERE t2.event_id = 212
AND t2.session_no = 1
AND t1.Status = 0;