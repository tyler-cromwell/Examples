BEGIN;

/*
 * Import data from a CSV file into a database
 *
 * Replace the following:
 *   1) "csvdb" with the appropriate database name
 *   2) "'data.csv'" with the appropriate file name
 *   3) "csvtable" with the appropriate table name
 *   4) "(col1, col2, col3)" with the appropriate column names.
 */

CREATE DATABASE IF NOT EXISTS csvdb;
USE csvdb;

/* Import the CSV data */
LOAD DATA LOCAL INFILE 'data.csv' INTO TABLE csvtable
fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(col1, col2, col3);

/* Optional - delete the column name row */
DELETE FROM csvtable LIMIT 1;

COMMIT;
