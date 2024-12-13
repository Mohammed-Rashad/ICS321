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
  CONSTRAINT `dependent_ibfk_1` FOREIGN KEY (`GuardianID`) REFERENCES `passenger` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dependent`
--

LOCK TABLES `dependent` WRITE;
/*!40000 ALTER TABLE `dependent` DISABLE KEYS */;
/*!40000 ALTER TABLE `dependent` ENABLE KEYS */;
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
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `passenger`
--

LOCK TABLES `passenger` WRITE;
/*!40000 ALTER TABLE `passenger` DISABLE KEYS */;
/*!40000 ALTER TABLE `passenger` ENABLE KEYS */;
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
  `FirstStation` int NOT NULL,
  `LastStation` int NOT NULL,
  `SeatNumber` int NOT NULL,
  PRIMARY KEY (`PassengerID`,`TripNumber`,`Date`,`FirstStation`,`LastStation`),
  KEY `TripNumber` (`TripNumber`,`Date`,`FirstStation`),
  KEY `TripNumber_2` (`TripNumber`,`Date`,`LastStation`),
  CONSTRAINT `reservation_ibfk_1` FOREIGN KEY (`PassengerID`) REFERENCES `passenger` (`ID`),
  CONSTRAINT `reservation_ibfk_2` FOREIGN KEY (`TripNumber`, `Date`, `FirstStation`) REFERENCES `trip_stop` (`TripNumber`, `Date`, `StopOrder`),
  CONSTRAINT `reservation_ibfk_3` FOREIGN KEY (`TripNumber`, `Date`, `LastStation`) REFERENCES `trip_stop` (`TripNumber`, `Date`, `StopOrder`)
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
  PRIMARY KEY (`TrainNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `train`
--

LOCK TABLES `train` WRITE;
/*!40000 ALTER TABLE `train` DISABLE KEYS */;
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
  `StopOrder` int NOT NULL,
  `StationName` varchar(15) NOT NULL,
  `SeatsAvailable` int NOT NULL,
  PRIMARY KEY (`TripNumber`,`Date`,`StopOrder`),
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
  `FirstStation` int NOT NULL,
  `LastStation` int NOT NULL,
  PRIMARY KEY (`PassengerID`,`TripNumber`,`Date`,`FirstStation`,`LastStation`),
  KEY `TripNumber` (`TripNumber`,`Date`,`FirstStation`),
  KEY `TripNumber_2` (`TripNumber`,`Date`,`LastStation`),
  CONSTRAINT `waitlist_ibfk_1` FOREIGN KEY (`PassengerID`) REFERENCES `passenger` (`ID`),
  CONSTRAINT `waitlist_ibfk_2` FOREIGN KEY (`TripNumber`, `Date`, `FirstStation`) REFERENCES `trip_stop` (`TripNumber`, `Date`, `StopOrder`),
  CONSTRAINT `waitlist_ibfk_3` FOREIGN KEY (`TripNumber`, `Date`, `LastStation`) REFERENCES `trip_stop` (`TripNumber`, `Date`, `StopOrder`)
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

-- Dump completed on 2024-12-12 17:51:12

CREATE TABLE admin (
    ID INT AUTO_INCREMENT NOT NULL,           -- Automatically incremented primary key
    email VARCHAR(100) NOT NULL,              -- Email cannot be null
    password VARCHAR(255) NOT NULL,           -- Sufficient space for hashed passwords
    Name VARCHAR(30) NOT NULL,                -- Name of the admin, cannot be null
    Salary DECIMAL(10, 2),                    -- Salary with 2 decimal places
    PRIMARY KEY (ID),                        -- Primary key on ID
    UNIQUE (email)                           -- Ensure email is unique across all records
);
