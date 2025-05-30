-- List Glam rock bands ranked by longevity
SELECT band_name, (IFNULL(split, 2022) - formed) as lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC; 