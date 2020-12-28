CREATE TABLE IF NOT EXISTS contacts
(
    id INT(32) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255),
    phone VARCHAR(255) NOT NULL,
    address VARCHAR(255),
    score INTEGER
);