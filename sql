CREATE TABLE yt_pages (
    id INT UNSIGNED PRIMARY KEY NOT NULL
    name VARCHAR(255) NOT NULL,
    publish_date DATE NOT NULL,
    duration INT UNSIGNED NOT NULL,
    likes INT UNSIGNED NOT NULL,
    dislikes INT UNSIGNED NOT NULL,
    views BIGINT UNSIGNED NOT NULL
    )
;
