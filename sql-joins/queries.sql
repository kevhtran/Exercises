-- write your queries here --
-- SELECT * FROM owners FULL OUTER JOIN vehicles ON owners.id = vehicles.owner_id; --
-- SELECT first_name, last_name, COUNT(*) FROM owners JOIN vehicles ON owners.id = vehicles.owner_id GROUP BY (first_name, last_name) ORDER BY first_name; --
-- SELECT first_name, last_name, ROUND(AVG(price)), COUNT(*) FROM owners JOIN vehicles ON owners.id = vehicles.owner_id GROUP BY (first_name, last_name) HAVING ROUND(AVG(price)) > 10000 AND COUNT(*) > 1 ORDER BY first_name DESC; --