-- Lists all the cities of California of the database hbtn_0d_usa:
-- * The states table contains only one record where name = California (but the id can be different, as per the example)
-- * Results must be sorted in ascending order by cities.id
SELECT id, name FROM cities
WHERE state_id=(
    SELECT id FROM states WHERE name='California'
);
