-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: TRAIN_MANAGEMENT_SYSTEM
-- ------------------------------------------------------
-- Server version	8.0.40

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `ID` int NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Salary` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (1122334455,'eng.mrwanm@gmail.com','password1','Marwan',999999.00);
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `assigned`
--

DROP TABLE IF EXISTS `assigned`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `assigned` (
  `employeeID` int NOT NULL,
  `date` date NOT NULL,
  `trainNumber` int NOT NULL,
  PRIMARY KEY (`employeeID`,`date`),
  KEY `trainNumber` (`trainNumber`),
  CONSTRAINT `assigned_ibfk_1` FOREIGN KEY (`employeeID`) REFERENCES `employee` (`id`),
  CONSTRAINT `assigned_ibfk_2` FOREIGN KEY (`trainNumber`) REFERENCES `train` (`TrainNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `assigned`
--

LOCK TABLES `assigned` WRITE;
/*!40000 ALTER TABLE `assigned` DISABLE KEYS */;
/*!40000 ALTER TABLE `assigned` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dependent`
--

DROP TABLE IF EXISTS `dependent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dependent` (
  `ID` int NOT NULL,
  `Name` varchar(15) NOT NULL,
  `GuardianID` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `GuardianID` (`GuardianID`),
  CONSTRAINT `dependent_ibfk_1` FOREIGN KEY (`GuardianID`) REFERENCES `passenger` (`ID`),
  CONSTRAINT `dependent_ibfk_2` FOREIGN KEY (`ID`) REFERENCES `person` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dependent`
--

LOCK TABLES `dependent` WRITE;
/*!40000 ALTER TABLE `dependent` DISABLE KEYS */;
INSERT INTO `dependent` VALUES (101,'Suhail',1111100000),(102,'Aziz',1110000000),(103,'Jamal',1110000000),(104,'Trevok',1110000000),(105,'Takashi',1100000000);
/*!40000 ALTER TABLE `dependent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `id` int NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(20) NOT NULL,
  `Name` varchar(20) NOT NULL,
  `Salary` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (202246240,'202246240@kfupm.edu.sa','password1','Jaddoua',20000.00),(202252120,'202252120@kfupm.edu.sa','password1','Rashad',19999.99);
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `passenger`
--

DROP TABLE IF EXISTS `passenger`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `passenger` (
  `ID` int NOT NULL,
  `Name` varchar(15) NOT NULL,
  `Balance` int NOT NULL,
  `password` varchar(20) NOT NULL,
  `email` varchar(30) NOT NULL,
  `phone` varchar(14) NOT NULL,
  `isLoyalty` tinyint(1) NOT NULL,
  PRIMARY KEY (`ID`),
  CONSTRAINT `passenger_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `person` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `passenger`
--

LOCK TABLES `passenger` WRITE;
/*!40000 ALTER TABLE `passenger` DISABLE KEYS */;
INSERT INTO `passenger` VALUES (1000000000,'Mohammed',60,'password1','b@gmail.com','0550001234',1),(1100000000,'Husam',0,'password1','c@gmail.com','0555000000',0),(1110000000,'Ammar',300,'password1','d@gmail.com','0555500000',1),(1111000000,'Ali',40,'password1','e@gmail.com','0555550000',0),(1111100000,'Ziad',60,'password1','f@gmail.com','0555555000',0),(1111110000,'Bassam',150,'password1','g@gmail.com','0555555500',1),(1111111000,'Yousef',90,'password1','h@gmail.com','0555555550',0),(1234567890,'Ahmed',100,'password1','a@gmail.com','0505550000',0);
/*!40000 ALTER TABLE `passenger` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `person`
--

DROP TABLE IF EXISTS `person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `person` (
  `id` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `person`
--

LOCK TABLES `person` WRITE;
/*!40000 ALTER TABLE `person` DISABLE KEYS */;
INSERT INTO `person` VALUES (101),(102),(103),(104),(105),(1000000000),(1100000000),(1110000000),(1111000000),(1111100000),(1111110000),(1111111000),(1234567890);
/*!40000 ALTER TABLE `person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservation`
--

DROP TABLE IF EXISTS `reservation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservation` (
  `PassengerID` int NOT NULL,
  `TripNumber` int NOT NULL,
  `Date` date NOT NULL,
  `firstStation` time NOT NULL,
  `lastStation` time NOT NULL,
  `SeatNumber` int NOT NULL,
  `hasPaid` tinyint(1) NOT NULL,
  PRIMARY KEY (`PassengerID`,`TripNumber`,`Date`,`firstStation`,`lastStation`),
  KEY `TripNumber` (`TripNumber`,`Date`,`firstStation`),
  KEY `TripNumber_2` (`TripNumber`,`Date`,`lastStation`),
  CONSTRAINT `reservation_ibfk_1` FOREIGN KEY (`TripNumber`, `Date`, `firstStation`) REFERENCES `trip_stop` (`TripNumber`, `Date`, `Time`),
  CONSTRAINT `reservation_ibfk_2` FOREIGN KEY (`TripNumber`, `Date`, `lastStation`) REFERENCES `trip_stop` (`TripNumber`, `Date`, `Time`),
  CONSTRAINT `reservation_ibfk_3` FOREIGN KEY (`PassengerID`) REFERENCES `person` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservation`
--

LOCK TABLES `reservation` WRITE;
/*!40000 ALTER TABLE `reservation` DISABLE KEYS */;
/*!40000 ALTER TABLE `reservation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `station`
--

DROP TABLE IF EXISTS `station`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `station` (
  `Name` varchar(15) NOT NULL,
  `City` varchar(15) NOT NULL,
  PRIMARY KEY (`Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `station`
--

LOCK TABLES `station` WRITE;
/*!40000 ALTER TABLE `station` DISABLE KEYS */;
INSERT INTO `station` VALUES ('Aramco','Dammam'),('Central Station','Riyadh'),('Haram','Makkah'),('JED Airport','Jeddah'),('KFUPM','Dharan'),('Mountain','Abha'),('Port','Jeddah'),('School','Makkah'),('Tala Mall','Riyadh'),('Tower','Riyadh');
/*!40000 ALTER TABLE `station` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `train`
--

DROP TABLE IF EXISTS `train`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `train` (
  `TrainNumber` int NOT NULL,
  `MaxPassenger` int NOT NULL,
  `cost` int NOT NULL,
  PRIMARY KEY (`TrainNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `train`
--

LOCK TABLES `train` WRITE;
/*!40000 ALTER TABLE `train` DISABLE KEYS */;
INSERT INTO `train` VALUES (1,30,10),(2,25,15),(3,30,20),(4,50,30),(5,60,25);
/*!40000 ALTER TABLE `train` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trip`
--

DROP TABLE IF EXISTS `trip`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trip` (
  `TripNumber` int NOT NULL,
  `Date` date NOT NULL,
  `TrainNumber` int NOT NULL,
  PRIMARY KEY (`TripNumber`,`Date`),
  KEY `TrainNumber` (`TrainNumber`),
  CONSTRAINT `trip_ibfk_1` FOREIGN KEY (`TrainNumber`) REFERENCES `train` (`TrainNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trip`
--

LOCK TABLES `trip` WRITE;
/*!40000 ALTER TABLE `trip` DISABLE KEYS */;
/*!40000 ALTER TABLE `trip` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trip_stop`
--

DROP TABLE IF EXISTS `trip_stop`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trip_stop` (
  `TripNumber` int NOT NULL,
  `Date` date NOT NULL,
  `StationName` varchar(15) NOT NULL,
  `Time` time NOT NULL,
  PRIMARY KEY (`TripNumber`,`Date`,`Time`),
  KEY `StationName` (`StationName`),
  CONSTRAINT `trip_stop_ibfk_1` FOREIGN KEY (`TripNumber`, `Date`) REFERENCES `trip` (`TripNumber`, `Date`),
  CONSTRAINT `trip_stop_ibfk_2` FOREIGN KEY (`StationName`) REFERENCES `station` (`Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trip_stop`
--

LOCK TABLES `trip_stop` WRITE;
/*!40000 ALTER TABLE `trip_stop` DISABLE KEYS */;
/*!40000 ALTER TABLE `trip_stop` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `waitlist`
--

DROP TABLE IF EXISTS `waitlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `waitlist` (
  `PassengerID` int NOT NULL,
  `TripNumber` int NOT NULL,
  `Date` date NOT NULL,
  `firstStation` time NOT NULL,
  `lastStation` time NOT NULL,
  PRIMARY KEY (`PassengerID`,`TripNumber`,`Date`,`firstStation`,`lastStation`),
  KEY `TripNumber` (`TripNumber`,`Date`,`firstStation`),
  KEY `TripNumber_2` (`TripNumber`,`Date`,`lastStation`),
  CONSTRAINT `waitlist_ibfk_1` FOREIGN KEY (`TripNumber`, `Date`, `firstStation`) REFERENCES `trip_stop` (`TripNumber`, `Date`, `Time`),
  CONSTRAINT `waitlist_ibfk_2` FOREIGN KEY (`PassengerID`) REFERENCES `person` (`id`),
  CONSTRAINT `waitlist_ibfk_3` FOREIGN KEY (`TripNumber`, `Date`, `lastStation`) REFERENCES `trip_stop` (`TripNumber`, `Date`, `Time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `waitlist`
--

LOCK TABLES `waitlist` WRITE;
/*!40000 ALTER TABLE `waitlist` DISABLE KEYS */;
/*!40000 ALTER TABLE `waitlist` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-14 20:30:49
