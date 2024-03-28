-- SQL request(s)​​​​​​‌​‌​‌‌‌​‌​​‌​​‌​‌‌​​‌​‌‌‌ below
SELECT pixelUpdates.newColor AS color, COUNT(*) AS count FROM pixels
INNER JOIN pixelUpdates ON pixels.id = pixelUpdates.pixelId
WHERE pixelUpdates.updatedAt <> pixels.firstPaintedAt
GROUP BY pixelUpdates.newColor
ORDER BY count DESC;