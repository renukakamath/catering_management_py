/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 10.4.27-MariaDB : Database - catering
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`catering` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;

USE `catering`;

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `Username` varchar(50) NOT NULL,
  `Password` varchar(10) DEFAULT NULL,
  `User_type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `login` */

insert  into `login`(`Username`,`Password`,`User_type`) values 
('admin','admin','admin'),
('amal','amal','staff'),
('ccc','ccc','customer'),
('hari@gmail.com','hari','staff'),
('new@gmail.com','new','customer'),
('staff','staff','staff'),
('test1@gmail.com','123456','customer'),
('test2@gamil.com','test','customer');

/*Table structure for table `tbl_card` */

DROP TABLE IF EXISTS `tbl_card`;

CREATE TABLE `tbl_card` (
  `card_id` int(11) NOT NULL AUTO_INCREMENT,
  `cus_id` int(11) DEFAULT NULL,
  `card_no` int(16) DEFAULT NULL,
  `card_name` varchar(30) DEFAULT NULL,
  `card_expiry` date DEFAULT NULL,
  `status` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`card_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `tbl_card` */

/*Table structure for table `tbl_cart_child` */

DROP TABLE IF EXISTS `tbl_cart_child`;

CREATE TABLE `tbl_cart_child` (
  `cartC_id` int(11) NOT NULL AUTO_INCREMENT,
  `cartM_id` int(11) DEFAULT NULL,
  `item_id` int(11) DEFAULT NULL,
  `qty` int(10) DEFAULT NULL,
  `place` varchar(15) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`cartC_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `tbl_cart_child` */

/*Table structure for table `tbl_cart_master` */

DROP TABLE IF EXISTS `tbl_cart_master`;

CREATE TABLE `tbl_cart_master` (
  `cartM_id` int(11) NOT NULL AUTO_INCREMENT,
  `cus_id` int(11) DEFAULT NULL,
  `event_id` int(11) DEFAULT NULL,
  `total_price` int(10) DEFAULT NULL,
  `status` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`cartM_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `tbl_cart_master` */

/*Table structure for table `tbl_category` */

DROP TABLE IF EXISTS `tbl_category`;

CREATE TABLE `tbl_category` (
  `cat_id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) DEFAULT NULL,
  `Description` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`cat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `tbl_category` */

insert  into `tbl_category`(`cat_id`,`Name`,`Description`) values 
(1,'drinks','test'),
(2,'starter','french fries,paneer tikka,chicken 65'),
(3,'main course','briyani,fried rice,noodles'),
(4,'deserts','ice cream,carrot halwa,gulab jammun'),
(5,'food','foodfoodfood\r\n');

/*Table structure for table `tbl_customer` */

DROP TABLE IF EXISTS `tbl_customer`;

CREATE TABLE `tbl_customer` (
  `cus_id` int(11) NOT NULL AUTO_INCREMENT,
  `Email` varchar(20) DEFAULT NULL,
  `Firstname` varchar(20) DEFAULT NULL,
  `Lastname` varchar(20) DEFAULT NULL,
  `Phone_number` varchar(10) DEFAULT NULL,
  `House_name` varchar(15) DEFAULT NULL,
  `State` varchar(15) DEFAULT NULL,
  `District` varchar(15) DEFAULT NULL,
  `Pincode` varchar(7) DEFAULT NULL,
  `Password` varchar(8) DEFAULT NULL,
  `Status` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`cus_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `tbl_customer` */

insert  into `tbl_customer`(`cus_id`,`Email`,`Firstname`,`Lastname`,`Phone_number`,`House_name`,`State`,`District`,`Pincode`,`Password`,`Status`) values 
(1,'gopika','gopika','g','1234567890','heritage villag','kerala','ernakulam','683009',NULL,1),
(2,'staff1@gmail.com','robin','Stinson','7890567890','staff1@gmail.co','hertiage villag','kerala','ernakul','683009',1),
(3,'test1@gmail.com','test','test2','1234567890','test1@gmail.com','name','kerala','ernakul','683009',1),
(4,'test2@gamil.com','test1','test2','8905890457','test','test','test','682002','test',1),
(5,'ccc','cc','cc','cccc','cc','cc','cc','cc','cc',1),
(6,'new@gmail.com','new','nn','1234567890','name','kerala','ernakulam','683009','new',1);

/*Table structure for table `tbl_event` */

DROP TABLE IF EXISTS `tbl_event`;

CREATE TABLE `tbl_event` (
  `event_id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(20) DEFAULT NULL,
  `Description` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`event_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `tbl_event` */

insert  into `tbl_event`(`event_id`,`Name`,`Description`) values 
(12,'wedding1','dda'),
(13,'wedding','mchdjddska\r\n\r\n'),
(14,'hdgjdhfk','kkdsnkdnfk');

/*Table structure for table `tbl_item` */

DROP TABLE IF EXISTS `tbl_item`;

CREATE TABLE `tbl_item` (
  `item_id` int(11) NOT NULL AUTO_INCREMENT,
  `cat_id` int(11) DEFAULT NULL,
  `Iname` varchar(30) DEFAULT NULL,
  `Description` text DEFAULT NULL,
  `Image` varchar(500) DEFAULT NULL,
  `Price` decimal(10,0) DEFAULT NULL,
  `Status` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`item_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `tbl_item` */

insert  into `tbl_item`(`item_id`,`cat_id`,`Iname`,`Description`,`Image`,`Price`,`Status`) values 
(1,2,'paneer tikka','french fries,paneer tikka,chicken 65','static/uploads/73550a79-d68c-4216-8fbe-5f531d262daaScreenshot_20230220_161034.png',23,'0'),
(2,2,'paneer tikka','french fries,paneer tikka,chicken 65','static/uploads/a35a784a-9a18-4124-9053-e4023fbeacf4Screenshot 2023-02-20 161038.png',23,'1');

/*Table structure for table `tbl_payment` */

DROP TABLE IF EXISTS `tbl_payment`;

CREATE TABLE `tbl_payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `card_id` int(11) DEFAULT NULL,
  `cartM_id` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `tbl_payment` */

/*Table structure for table `tbl_staff` */

DROP TABLE IF EXISTS `tbl_staff`;

CREATE TABLE `tbl_staff` (
  `staff_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `Firstname` varchar(50) DEFAULT NULL,
  `Lastname` varchar(50) DEFAULT NULL,
  `Phone_number` varchar(10) DEFAULT NULL,
  `House_name` varchar(50) DEFAULT NULL,
  `State` varchar(50) DEFAULT NULL,
  `District` varchar(50) DEFAULT NULL,
  `Pincode` varchar(7) NOT NULL,
  `Date` date DEFAULT NULL,
  `Status` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`staff_id`,`Pincode`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `tbl_staff` */

insert  into `tbl_staff`(`staff_id`,`username`,`Firstname`,`Lastname`,`Phone_number`,`House_name`,`State`,`District`,`Pincode`,`Date`,`Status`) values 
(13,'staff1@gmail.com','robin','Stinson','7890567890','hertiage village','kerala','ernakulam','683005','2023-01-19',1),
(14,'staff2@gmail.com','harvey','robert','907356789','peace villa','kerala','kannur','672190','2023-01-22',1),
(15,'staff2@gmail.com','harvey','robert','907356789','peace villa','kerala','kannur','672190','2023-01-22',1),
(16,'staff2@gmail.com','harvey','robert','907356789','peace villa','kerala','kannur','672190','2023-01-22',1),
(17,'staff2@gmail.com','harvey','robert','907356789','peace villa','kerala','kannur','672190','2023-01-22',1),
(18,'staff2@gmail.com','harvey','robert','907356789','peace villa','kerala','kannur','672190','2023-01-22',1),
(19,'staff2@gmail.com','harvey','robert','907356789','peace villa','kerala','kannur','672190','2023-01-22',1),
(20,'amal','uhdfiudh','ijhdsihf','1234567890','jdshjdnc','hdsbdhgfk','hdkhsjhj','123456','2023-02-13',1),
(21,'hari@gmail.com','uhdfiudh','ijhdsihf','1234567890','jdshjdnc','hdsbdhgfk','hdkhsjhj','123456','2023-02-13',1);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
