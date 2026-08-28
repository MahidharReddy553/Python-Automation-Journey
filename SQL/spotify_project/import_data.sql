USE music_analysis_project;
SHOW VARIABLES LIKE 'local_infile';

LOAD DATA LOCAL INFILE 'D:/Python Automation Journey/SQL/spotify_project/spotify_songs.csv'
INTO TABLE raw_tracks
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
SELECT COUNT(*) FROM raw_tracks;
DESCRIBE raw_tracks;