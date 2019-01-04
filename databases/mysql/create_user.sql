/*
 * MySQL create user script.
 */


BEGIN;
CREATE USER 'username' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON * . * TO 'username';
FLUSH PRIVILEGES;
COMMIT;
