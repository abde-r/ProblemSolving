SELECT agent.name AS NAME, COUNT(mutant.recruiterId) AS SCORE FROM mutant
INNER JOIN agent ON agent.agentId = mutant.recruiterId
GROUP BY mutant.recruiterId, agent.name
ORDER BY SCORE DESC LIMIT 10;
