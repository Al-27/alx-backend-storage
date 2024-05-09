-- SQL COMMENT
SELECT band_name, IF(split > 0, split - formed, 2022 - formed) AS lifespan FROM metal_bands WHERE style LIKE "%Glam rock%" ORDER BY lifespan DESC;
