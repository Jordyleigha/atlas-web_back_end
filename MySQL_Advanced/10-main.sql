-- 10-main.sql

-- Drop the function if it already exists
DROP FUNCTION IF EXISTS SafeDiv;

-- Create the SafeDiv function
DELIMITER //

CREATE FUNCTION SafeDiv(a INT, b INT) 
RETURNS INT
BEGIN
    DECLARE result INT;

    -- Check if b is 0
    IF b = 0 THEN
        SET result = 0;  -- Return 0 if b is 0
    ELSE
        SET result = a / b;  -- Perform division if b is not 0
    END IF;

    RETURN result;  -- Return the result
END //

DELIMITER ;

-- Example usage of the SafeDiv function
SELECT SafeDiv(10, 2) AS Result1;  -- Should return 5
SELECT SafeDiv(10, 0) AS Result2;  -- Should return 0
SELECT SafeDiv(15, 3) AS Result3;  -- Should return 5
SELECT SafeDiv(7, 0) AS Result4;   -- Should return 0