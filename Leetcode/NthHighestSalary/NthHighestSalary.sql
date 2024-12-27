CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    SET N = N-1;
    RETURN (
        SELECT DISTINCT(salary) AS 'getNthHighestSalary(2)' FROM Employee ORDER BY salary DESC LIMIT 1 OFFSET N
    );
END
