-- creates a function SafeDiv that divides (and returns) the first
-- by the second number or returns 0 if the second number is equal to 0
DELIMITER //

CREATE FUNCTION SafeDiv(a int, b int)
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