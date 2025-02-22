SELECT SUM(p.Expense) AS TotalExpense
FROM purchase p
INNER JOIN concert c ON p.Event_ID = c.Event_ID;