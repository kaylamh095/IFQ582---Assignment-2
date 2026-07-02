CREATE DATABASE  IF NOT EXISTS `library_database` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `library_database`;
-- MySQL dump 10.13  Distrib 8.0.46, for Win64 (x86_64)
--
-- Host: localhost    Database: library_database
-- ------------------------------------------------------
-- Server version	8.0.46

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `access_request`
--

DROP TABLE IF EXISTS `access_request`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `access_request` (
  `request_ID` int NOT NULL AUTO_INCREMENT,
  `item_ID` int NOT NULL,
  `member_ID` int NOT NULL,
  `request_status` varchar(15) NOT NULL,
  `review_timestamp` datetime DEFAULT NULL,
  PRIMARY KEY (`request_ID`),
  KEY `item_ID` (`item_ID`),
  KEY `member_ID` (`member_ID`),
  CONSTRAINT `access_request_ibfk_1` FOREIGN KEY (`item_ID`) REFERENCES `collection_items` (`item_ID`),
  CONSTRAINT `access_request_ibfk_2` FOREIGN KEY (`member_ID`) REFERENCES `public_user` (`member_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `access_request`
--

LOCK TABLES `access_request` WRITE;
/*!40000 ALTER TABLE `access_request` DISABLE KEYS */;
INSERT INTO `access_request` VALUES (1,15,1,'pending','2026-07-01 00:00:00');
/*!40000 ALTER TABLE `access_request` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `access_review`
--

DROP TABLE IF EXISTS `access_review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `access_review` (
  `review_ID` int NOT NULL AUTO_INCREMENT,
  `item_ID` int NOT NULL,
  `elder_ID` int NOT NULL,
  `review_notes` varchar(500) DEFAULT NULL,
  `access_outcome` varchar(15) DEFAULT NULL,
  `review_timestamp` datetime DEFAULT NULL,
  `sensitivity_level` text,
  `conditions_of_use` text,
  PRIMARY KEY (`review_ID`),
  KEY `item_ID` (`item_ID`),
  KEY `elder_ID` (`elder_ID`),
  CONSTRAINT `access_review_ibfk_1` FOREIGN KEY (`item_ID`) REFERENCES `collection_items` (`item_ID`),
  CONSTRAINT `access_review_ibfk_2` FOREIGN KEY (`elder_ID`) REFERENCES `community_elder` (`elder_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `access_review`
--

LOCK TABLES `access_review` WRITE;
/*!40000 ALTER TABLE `access_review` DISABLE KEYS */;
/*!40000 ALTER TABLE `access_review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `collection_items`
--

DROP TABLE IF EXISTS `collection_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `collection_items` (
  `item_ID` int NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `description` text,
  `image_link` varchar(40) DEFAULT NULL,
  `item_category` varchar(40) NOT NULL,
  `cultural_group` varchar(30) DEFAULT NULL,
  `sensitivity_notes` varchar(30) DEFAULT NULL,
  `review_status` varchar(20) NOT NULL,
  `access_level` varchar(20) NOT NULL DEFAULT 'Private',
  PRIMARY KEY (`item_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `collection_items`
--

LOCK TABLES `collection_items` WRITE;
/*!40000 ALTER TABLE `collection_items` DISABLE KEYS */;
INSERT INTO `collection_items` VALUES (1,'The Sunrise','The Sunrise is a piece of indigenous artwork by artist \'William Long\' from 1977.  The Sunrise depicts the first light of sunrise spreading across ancient mountains, bringing warmth and renewal to Country. Flowing snake motifs weave through the landscape, symbolising connection, movement, creation, and the enduring relationship between people, land, and spirit.','img/artwork_1.png','Artwork created by Indigenous artists','Yuggera People','None','Completed','Public'),(2,'River Runs','River Runs is a piece of indigenous artwork by artist \'Betty Small\' from 1954.  This Australian Indigenous artwork features flowing river pathways in rich blue tones winding through the landscape, connecting a series of concentric circles that represent meeting places and waterholes. Earthy brown colours reflect the land, Country, and ancestral connections, while the intertwining designs symbolise journeys, relationships, knowledge sharing, and the enduring bond between people and place.','img/artwork_2.png','Artwork created by Indigenous artists','Turrbal People','None','Under Review','Private'),(3,'The Devil','The Devil is a piece of indigenous artwork by artist \'Jimmy Fall\' from 1928.  The Devil depicts native devil-like animals moving across Country, surrounded by traditional circles and dot motifs. Earthy brown tones reflect the land, while the design symbolises movement, connection, survival, and ancestral stories.','img/artwork_3.png','Artwork created by Indigenous artists','Kabi Kabi People','Men\'s Business','Completed','Restricted'),(4,'Gathering','Gathering is a piece of indigenous artwork by artist \'Betty Simons\' from 1980.  Bursting with energy and colour, this vibrant Australian Indigenous artwork celebrates connection, community, and Country. A large central circle represents a gathering place, surrounded by intricate dot pattern. The playful colours evoke sunshine, water, warmth, and storytelling, creating a joyful journey across the landscape that connects community at its heart.','img/artwork_4.png','Artwork created by Indigenous artists','Turrbal People','Corroboree','Completed','Public'),(5,'Story Time','Listen to a captivating Indigenous story that shares the rich history, traditions, and knowledge of Aboriginal peoples. Through storytelling, explore connections to Country, culture, community, and generations past.','img/audio_recording.png','Audio recordings of oral histories','Turrbal People','Sorry Business','Completed','Restricted'),(6,'Turtle Wisdom','This beautifully crafted boomerang features a turtle design, symbolising wisdom, endurance, and a deep connection to water and Country. Traditional patterns decorate the surface, celebrating Aboriginal culture, storytelling, and the enduring relationship between people, animals, and the natural world.','img/boomerang_1.png','Cultural artefact records','Yugambeh People','None','Pending','Private'),(7,'Survival','This striking boomerang showcases lizard motifs woven into traditional Aboriginal-inspired patterns. Lizards are often associated with adaptability, survival, and a close connection to the land. The detailed artwork reflects journeys across Country, the sharing of knowledge, and the importance of native wildlife. Rich earthy tones and intricate designs celebrate culture, storytelling, and the enduring relationship between people and nature.','img/boomerang_2.png','Cultural artefact records','Jinibara People','Men\'s Business','Completed','Public'),(8,'Didgeridoo','This beautifully crafted didgeridoo features intricate artwork inspired by the landscapes, stories, and traditions of Aboriginal Australia. Detailed patterns flow along its length, creating a captivating visual journey that reflects connection to Country, culture, and community. Both a musical instrument and a work of art, it celebrates the richness of Indigenous storytelling and creative expression..','img/didgeridoo_1.png','Cultural artefact records','Turrbal People','Ceremony','Completed','Public'),(9,'Flowering Didgeridoo','This vibrant didgeridoo features a striking flower motif at its centre, surrounded by colourful artwork that flows along the instrument’s length. Bright patterns in warm and cool tones celebrate the beauty of nature, growth, and renewal. The intricate designs evoke stories of Country, seasons, and connection, transforming the didgeridoo into both a musical instrument and a captivating piece of artistic expression.','img/didgeridoo_2.png','Cultural artefact records','Ningy Ningy People','Men\'s Business','Completed','Public'),(10,'Corroboree','This historical photograph captures an Indigenous Australian ceremony featuring traditional dancing, offering a glimpse into the rich cultural practices of Aboriginal communities. The image reflects the importance of ceremony, storytelling, connection to Country, and the passing of knowledge through generations, preserving a valuable moment in Australia\'s cultural history.','img/historical_photograph_1.png','Historical Photographs','Ningy Ningy People','Corroboree','Completed','Public'),(11,'Stories of the Land','This historical photograph depicts an Indigenous Australian man gazing across the landscape, capturing a powerful moment of reflection and connection to Country. The image highlights the deep relationship between Aboriginal peoples and the land, shaped by thousands of years of knowledge, culture, and stewardship. It serves as a reminder of enduring traditions, identity, and the significance of place in Indigenous history and storytelling.','img/historical_photograph_2.png','Historical Photographs','Yuggera People','None','Completed','Public'),(12,'The Heart','This archival document examines the rights of Indigenous peoples, recording important discussions on recognition, land, culture, and self-determination. Preserved as a valuable historical record, it reflects ongoing efforts to advocate for justice, equality, and the protection of Indigenous communities. The manuscript provides insight into the social and political movements that have shaped Indigenous rights and contributed to broader conversations about reconciliation and human rights.','img/language_material.png','Language preservation materials','Yugambeh People','None','Completed','Public'),(13,'Care and Family Ties','This archival manuscript explores knowledge, responsibilities, ceremonies, and traditions that have been passed through generations of Aboriginal women. The document highlights the important roles women play in caring for family, community and Country. As a historical record, it offers valuable insight into Indigenous knowledge systems, cultural practices, and the strength and continuity of women’s cultural leadership.','img/manuscript_1.png','Archival manuscripts or documents','Jinibara People','Women\'s business','Completed','Restricted'),(14,'Yarning with the Aunties','Join a delightful storytelling journey that shares Indigenous stories, traditions, and insights into Women’s Business. Filled with wisdom, laughter, and cultural knowledge, this audio recording celebrates community, connection, and the passing of stories from one generation to the next.','img/audio_recording_2.png','Audio recordings of oral histories','Turrbal People','Women\'s business','Pending','Private'),(15,'Gathering of Stories','This archival manuscript preserves valuable cultural knowledge, stories, and historical perspectives passed down through generations. Offering a unique window into Indigenous traditions and experiences, the document invites readers to explore the rich heritage, wisdom, and enduring connections that continue to shape Aboriginal culture today.','img/manuscript_2.png','Archival manuscripts or documents','Yuggera People','Ceremony','Pending','Private'),(17,'new item','This is a new item',NULL,'this is a category','culture','nope','Under Review','Private');
/*!40000 ALTER TABLE `collection_items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `community_elder`
--

DROP TABLE IF EXISTS `community_elder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `community_elder` (
  `elder_ID` int NOT NULL AUTO_INCREMENT,
  `community_name` varchar(30) DEFAULT NULL,
  `user_ID` int NOT NULL,
  PRIMARY KEY (`elder_ID`),
  KEY `user_ID` (`user_ID`),
  CONSTRAINT `community_elder_ibfk_1` FOREIGN KEY (`user_ID`) REFERENCES `user` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `community_elder`
--

LOCK TABLES `community_elder` WRITE;
/*!40000 ALTER TABLE `community_elder` DISABLE KEYS */;
INSERT INTO `community_elder` VALUES (1,'Turrbal People',5),(2,'Ningy Ningy People',6),(3,'Turrbal People',14);
/*!40000 ALTER TABLE `community_elder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `library_staff`
--

DROP TABLE IF EXISTS `library_staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `library_staff` (
  `employee_ID` int NOT NULL AUTO_INCREMENT,
  `position_title` varchar(50) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `user_ID` int NOT NULL,
  `is_admin` int NOT NULL,
  PRIMARY KEY (`employee_ID`),
  KEY `user_ID` (`user_ID`),
  CONSTRAINT `library_staff_ibfk_1` FOREIGN KEY (`user_ID`) REFERENCES `user` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `library_staff`
--

LOCK TABLES `library_staff` WRITE;
/*!40000 ALTER TABLE `library_staff` DISABLE KEYS */;
INSERT INTO `library_staff` VALUES (1,'Library Director','2026-02-02',1,1),(2,'Librarian','2026-04-13',2,0),(3,'Admin','2026-01-01',13,1),(4,'Librarian','2026-04-26',12,0);
/*!40000 ALTER TABLE `library_staff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `public_user`
--

DROP TABLE IF EXISTS `public_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `public_user` (
  `member_ID` int NOT NULL AUTO_INCREMENT,
  `user_ID` int NOT NULL,
  PRIMARY KEY (`member_ID`),
  KEY `user_ID` (`user_ID`),
  CONSTRAINT `public_user_ibfk_1` FOREIGN KEY (`user_ID`) REFERENCES `user` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `public_user`
--

LOCK TABLES `public_user` WRITE;
/*!40000 ALTER TABLE `public_user` DISABLE KEYS */;
INSERT INTO `public_user` VALUES (1,3),(2,4),(3,11);
/*!40000 ALTER TABLE `public_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(10) DEFAULT NULL,
  `password` varchar(100) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Mary','Oliver','mary.oliver@gmail.com','0432998447','pa$$Word'),(2,'Kate','Brown','kbrown@hotmail.com','0405668776','123456789'),(3,'Alex','Smith','smithy@yahoo.com','0400443887','apple123'),(4,'Peter','Piper','ppiper@live.com','0433887998','password'),(5,'Timothy','McFee','timm@gmail.com','0498123456','timothymcfee'),(6,'Marlene','Monty','marlee3@gmail.com','0455332332','passwOrd1'),(11,'Public','User','publicuser@qut.edu.au','1234567890','42b3d38af5c3c9c3d3efbbe29db460fa1414c5320eb7b88ab057320d344ec038'),(12,'Library','Staff','librarystaff@qut.edu.au','0412345678','583424474c6a095be1140cdf8e4dbad292160a7b71e88810ed1e03eb467d3107'),(13,'Library','Admin','libraryadmin@qut.edu.au','0498765432','35581b9672e8d299b690bcd04f0cd011ba0537a347779ecfe5c7c4b1d5178874'),(14,'Comunity','Elder','elder@qut.edu.au','0400990099','63e44d74ae7218c30cb5c6077800e66900a65aca4739ead391aaf09fa66ec4cf');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-07-01 20:16:17
