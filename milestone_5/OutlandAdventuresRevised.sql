-- Create the Outland Adventures database
CREATE DATABASE `Outland Adventures`;

-- Use the OutlandAdventures database
USE `Outland Adventures`;

-- Drop the user if exists
DROP USER IF EXISTS 'outland_user'@'localhost';

-- Create outland_user and grant all privileges to the Outland Adventures database
CREATE USER 'outland_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'adventure';
GRANT ALL PRIVILEGES ON `Outland Adventures`.* TO 'outland_user'@'localhost';

-- Drop tables if they exist
DROP TABLE IF EXISTS customer;
DROP TABLE IF EXISTS equipment;
DROP TABLE IF EXISTS destination;
DROP TABLE IF EXISTS guide;

-- Create the equipment table
CREATE TABLE equipment (
    equipID INT NOT NULL AUTO_INCREMENT,
    equipmentName VARCHAR(75) NOT NULL,
    equipmentType VARCHAR(75) NOT NULL,
    acquisitionDate DATE NOT NULL,
    PRIMARY KEY(equipID)
);



CREATE TABLE destination (
    destinationID INT NOT NULL AUTO_INCREMENT,
    continent VARCHAR(75) NOT NULL,
    region VARCHAR(5) NOT NULL,
    startDate DATE NOT NULL,
    endDate DATE NOT NULL,
    PRIMARY KEY(destinationID)
);



-- Create the customer table
CREATE TABLE customer (
    customerID INT NOT NULL AUTO_INCREMENT,
    fname VARCHAR(75) NOT NULL,
	lname VARCHAR(75) NOT NULL,
    destination INT NOT NULL,
    equipUsed INT NOT NULL,
    equipStatus VARCHAR(75) NOT NULL,
    PRIMARY KEY(customerID),
    CONSTRAINT fk_equipUsed FOREIGN KEY(equipUsed) REFERENCES equipment(equipID),
    CONSTRAINT fk_destination FOREIGN KEY(destination) REFERENCES destination(destinationID)
);

-- Create the guide table
CREATE TABLE guide (
    employeeID INT NOT NULL AUTO_INCREMENT,
    fname VARCHAR(75) NOT NULL,
	lname VARCHAR(75) NOT NULL,
    PRIMARY KEY(employeeID)
);

-- Insert guide records
INSERT INTO guide(fname, lname) VALUES('John', 'MacNell');
INSERT INTO guide(fname, lname) VALUES('D.B.', 'Marland');
INSERT INTO guide(fname, lname) VALUES('Anita', 'Gallegos');
INSERT INTO guide(fname, lname) VALUES('Dimitros', 'Stravopolous');
INSERT INTO guide(fname, lname) VALUES('Mei', 'Wong');
INSERT INTO guide(fname, lname) VALUES('Blythe', 'Timmerson');
INSERT INTO guide(fname, lname) VALUES('Jim', 'Ford');

-- Insert equipment records
INSERT INTO equipment(equipmentName, equipmentType, acquisitionDate) VALUES('Hiking Boots', 'Wardrobe', '2010-01-01');
INSERT INTO equipment(equipmentName, equipmentType, acquisitionDate) VALUES('Fishing Rod', 'Outdoors', '2021-01-01');
INSERT INTO equipment(equipmentName, equipmentType, acquisitionDate) VALUES('Backpack', 'Wardrobe', '2022-01-01');
INSERT INTO equipment(equipmentName, equipmentType, acquisitionDate) VALUES('Climbing Gear Set', 'Outdoors', '2022-01-01');
INSERT INTO equipment(equipmentName, equipmentType, acquisitionDate) VALUES('Kayak', 'Outdoors', '2020-01-01');
INSERT INTO equipment(equipmentName, equipmentType, acquisitionDate) VALUES('Surfboard', 'Outdoors', '2023-01-01');

-- Insert destination records
INSERT INTO destination(continent, region, startDate, endDate) VALUES('Africa', 'West', '2023-01-25', '2023-02-07');
INSERT INTO destination(continent, region, startDate, endDate) VALUES('Asia', 'North', '2021-06-18', '2021-06-21');
INSERT INTO destination(continent, region, startDate, endDate) VALUES('Europe', 'South', '2009-09-01', '2009-09-07');
INSERT INTO destination(continent, region, startDate, endDate) VALUES('Africa', 'West', '2023-03-10', '2023-04-10');
INSERT INTO destination(continent, region, startDate, endDate) VALUES('Asia', 'North', '2022-02-01', '2023-02-07');
INSERT INTO destination(continent, region, startDate, endDate) VALUES('Asia', 'East', '2023-11-01', '2023-11-14');

-- Insert customer records
INSERT INTO customer(fname, lname, destination, equipUsed, equipStatus) VALUES('Jennifer', 'Lane', '1', '6', 'Purchase');
INSERT INTO customer(fname, lname, destination, equipUsed, equipStatus) VALUES('Bella', 'Goth', '2', '5', 'Rental');
INSERT INTO customer(fname, lname, destination, equipUsed, equipStatus) VALUES('Albert', 'Jones', '3', '4', 'Purchase');
INSERT INTO customer(fname, lname, destination, equipUsed, equipStatus) VALUES('Thomas', 'Green', '4', '3', 'Purchase');
INSERT INTO customer(fname, lname, destination, equipUsed, equipStatus) VALUES('John', 'Bell', '5', '2', 'Purchase');
INSERT INTO customer(fname, lname, destination, equipUsed, equipStatus) VALUES('Zoe', 'Ronda', '6', '1', 'Purchase');
