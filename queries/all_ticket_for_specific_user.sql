SELECT t1.ticket_no
FROM ticket AS t1
LEFT JOIN purchase AS t2
ON t1.Track_no = t2.Track_no
WHERE t2.Username = 'snpgsz9674';