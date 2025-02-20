-- script that lists all bands with glam rock, as their main style, ranked by longevity
SELECT band_name, TIMESTAMPDIFF(year, MAKEDATE(formed, 1), IF(split IS NULL, CURDATE(), MAKEDATE(split, 1))) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;