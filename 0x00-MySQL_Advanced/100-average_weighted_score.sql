-- Create stored procedure to compute weighted average score
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    IN user_id INT
)
BEGIN
    UPDATE users
    SET average_score = (
        SELECT SUM(c.score * p.weight) / SUM(p.weight)
        FROM corrections c
        JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = user_id
    )
    WHERE id = user_id;
END //
DELIMITER ; 