/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - hospitals
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`hospitals` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `hospitals`;

/*Table structure for table `ambulance_request` */

DROP TABLE IF EXISTS `ambulance_request`;

CREATE TABLE `ambulance_request` (
  `ambulance_request_id` int(11) NOT NULL AUTO_INCREMENT,
  `patient_id` int(11) DEFAULT NULL,
  `ambulance_id` int(11) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `date` varchar(225) DEFAULT NULL,
  `time` varchar(225) DEFAULT NULL,
  PRIMARY KEY (`ambulance_request_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `ambulance_request` */

insert  into `ambulance_request`(`ambulance_request_id`,`patient_id`,`ambulance_id`,`status`,`date`,`time`) values 
(1,1,1,'completed','2023-12-14','16:37:32');

/*Table structure for table `ambulances` */

DROP TABLE IF EXISTS `ambulances`;

CREATE TABLE `ambulances` (
  `ambulance_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `ambulance_number` varchar(255) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  `capacity` varchar(255) DEFAULT NULL,
  `equipments` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `driver_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ambulance_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `ambulances` */

insert  into `ambulances`(`ambulance_id`,`login_id`,`ambulance_number`,`type`,`capacity`,`equipments`,`status`,`driver_name`) values 
(1,11,'kl 01 j 8987','Neonatal Ambulance','6','ECG monitor, Ambulance Chair, Oxygen Supply Units','active','kuttapan');

/*Table structure for table `booking` */

DROP TABLE IF EXISTS `booking`;

CREATE TABLE `booking` (
  `booking_id` int(11) NOT NULL AUTO_INCREMENT,
  `schedule_id` int(11) DEFAULT NULL,
  `patient_id` int(11) DEFAULT NULL,
  `date_time` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`booking_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `booking` */

insert  into `booking`(`booking_id`,`schedule_id`,`patient_id`,`date_time`,`status`) values 
(1,1,1,'2023-12-13','paid');

/*Table structure for table `chats` */

DROP TABLE IF EXISTS `chats`;

CREATE TABLE `chats` (
  `chat_id` int(11) NOT NULL AUTO_INCREMENT,
  `sender_id` int(11) DEFAULT NULL,
  `receiver_id` int(11) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  `messages` varchar(255) DEFAULT NULL,
  `date_time` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`chat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

/*Data for the table `chats` */

insert  into `chats`(`chat_id`,`sender_id`,`receiver_id`,`type`,`messages`,`date_time`) values 
(1,2,7,'patient_to_doctor','hi doctor','2023-12-14 09:02:12'),
(2,7,2,'doctor to patient','hi','2023-12-14 09:10:21'),
(3,7,2,'doctor to patient','how are you now','2023-12-14 09:10:33'),
(4,2,7,'patient_to_doctor','im tottaly fine doctor','2023-12-14 09:12:58');

/*Table structure for table `departments` */

DROP TABLE IF EXISTS `departments`;

CREATE TABLE `departments` (
  `dept_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `dept_name` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`dept_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `departments` */

insert  into `departments`(`dept_id`,`login_id`,`dept_name`,`phone`,`email`,`description`) values 
(1,3,'ortho','1234567890','ortho@gmail.com','for all purpose');

/*Table structure for table `doctors` */

DROP TABLE IF EXISTS `doctors`;

CREATE TABLE `doctors` (
  `doctor_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `place` varchar(255) DEFAULT NULL,
  `qualification` varchar(255) DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`doctor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `doctors` */

insert  into `doctors`(`doctor_id`,`login_id`,`first_name`,`last_name`,`phone`,`email`,`place`,`qualification`,`image`) values 
(1,7,'Deepu','Paul','5678765434','deepu@gmail.com','thrissur','mbbs','static/438777b1-b457-49bc-bebb-420ac81f68d0nurse-2019420.jpg'),
(2,8,'shyam','raj','8376543456','shyam@gmail.com','tvm','md','static/c4e4fda9-1bf4-4820-a38f-8e65eca7c73dLaser-therapy.jpg'),
(3,9,'mani','a','7654323456','mani@gmail.com','idduki','mbbs md','static/da9bd7d1-bf06-44aa-898c-1313f6935d5bdesktop-wallpaper-here-s-the-best-ever-copy-paste-if-u-can-internet-explorer-jokes-physical-comedy-the-meta.jpg');

/*Table structure for table `inpatients` */

DROP TABLE IF EXISTS `inpatients`;

CREATE TABLE `inpatients` (
  `in_id` int(11) NOT NULL AUTO_INCREMENT,
  `patient_id` int(11) DEFAULT NULL,
  `admission_date` varchar(255) DEFAULT NULL,
  `purpose` varchar(255) DEFAULT NULL,
  `discharge_date` varchar(255) DEFAULT NULL,
  `admitting_relative` varchar(255) DEFAULT NULL,
  `contact` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`in_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `inpatients` */

insert  into `inpatients`(`in_id`,`patient_id`,`admission_date`,`purpose`,`discharge_date`,`admitting_relative`,`contact`,`status`) values 
(1,1,'2023-12-14','leg injury','pending','usman','3456789876','admitted');

/*Table structure for table `lab_test` */

DROP TABLE IF EXISTS `lab_test`;

CREATE TABLE `lab_test` (
  `test_id` int(11) NOT NULL AUTO_INCREMENT,
  `lab_id` int(11) DEFAULT NULL,
  `test_name` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `rate` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`test_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `lab_test` */

insert  into `lab_test`(`test_id`,`lab_id`,`test_name`,`description`,`rate`) values 
(1,1,'ortho test','used for finding fracture','400'),
(2,1,'ent','used for ear test','200');

/*Table structure for table `laboratory` */

DROP TABLE IF EXISTS `laboratory`;

CREATE TABLE `laboratory` (
  `lab_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `lab_name` varchar(255) DEFAULT NULL,
  `category` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`lab_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `laboratory` */

insert  into `laboratory`(`lab_id`,`login_id`,`lab_name`,`category`,`phone`,`email`) values 
(1,6,'lab','Clinical Chemistry Laboratories','1234567890','lab@gmail.com');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `usertype` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values 
(1,'admin','admin','admin'),
(2,'john','John12345','patients'),
(3,'ortho','Ortho123','department'),
(4,'reception','Recep123','reception'),
(5,'pharmacy','Pharm123','pharmacy'),
(6,'lab','Lab12345','laboratory'),
(7,'deepu','Deepu123','doctor'),
(8,'shyam','Shyam1234','doctor'),
(9,'mani','Mani1234','doctor'),
(10,'maniyan','Maniyan123','specialist'),
(11,'kuttapan','Kuttapan123','ambulance');

/*Table structure for table `medical_notes` */

DROP TABLE IF EXISTS `medical_notes`;

CREATE TABLE `medical_notes` (
  `note_id` int(11) NOT NULL AUTO_INCREMENT,
  `booking_id` int(11) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `date_time` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`note_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `medical_notes` */

insert  into `medical_notes`(`note_id`,`booking_id`,`description`,`date_time`) values 
(1,1,'big disease but sheriyakam','2023-12-13'),
(2,1,'eth simple ppdi\r\n','2023-12-14');

/*Table structure for table `medicine_stock` */

DROP TABLE IF EXISTS `medicine_stock`;

CREATE TABLE `medicine_stock` (
  `stock_id` int(11) NOT NULL AUTO_INCREMENT,
  `medicine_id` int(11) DEFAULT NULL,
  `quantity` varchar(255) DEFAULT NULL,
  `total` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`stock_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `medicine_stock` */

insert  into `medicine_stock`(`stock_id`,`medicine_id`,`quantity`,`total`,`status`) values 
(1,1,'18','1800','paid'),
(2,2,'9','700','paid'),
(3,3,'11','960','paid');

/*Table structure for table `medicines` */

DROP TABLE IF EXISTS `medicines`;

CREATE TABLE `medicines` (
  `medicine_id` int(11) NOT NULL AUTO_INCREMENT,
  `pharmacy_id` int(11) DEFAULT NULL,
  `medicine_name` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `available_qty` varchar(255) DEFAULT NULL,
  `expiry_date` varchar(255) DEFAULT NULL,
  `rate` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`medicine_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `medicines` */

insert  into `medicines`(`medicine_id`,`pharmacy_id`,`medicine_name`,`description`,`available_qty`,`expiry_date`,`rate`) values 
(1,1,'dolo','used for small thalavedhana and fever','18','2024-06-27','100'),
(2,1,'paracetamol','used for chomma','9','2024-12-05','70'),
(3,1,'tiger bam','used for vedhana','11','2028-12-31','80');

/*Table structure for table `patients` */

DROP TABLE IF EXISTS `patients`;

CREATE TABLE `patients` (
  `patient_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `house_name` varchar(255) DEFAULT NULL,
  `place` varchar(255) DEFAULT NULL,
  `gender` varchar(255) DEFAULT NULL,
  `blood_group` varchar(255) DEFAULT NULL,
  `dob` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`patient_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `patients` */

insert  into `patients`(`patient_id`,`login_id`,`first_name`,`last_name`,`phone`,`email`,`house_name`,`place`,`gender`,`blood_group`,`dob`) values 
(1,2,'john','smith','8330805387','deepupauly03@gmail.com','esdfghjbknl','down town','on','AB+','2023-12-01');

/*Table structure for table `payments` */

DROP TABLE IF EXISTS `payments`;

CREATE TABLE `payments` (
  `pay_id` int(11) NOT NULL AUTO_INCREMENT,
  `booking_id` int(11) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `payment_date` varchar(255) DEFAULT NULL,
  `payment_type` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`pay_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `payments` */

insert  into `payments`(`pay_id`,`booking_id`,`amount`,`payment_date`,`payment_type`,`status`) values 
(1,1,'100','2023-12-13','doctor_payment','paid'),
(2,1,'70','2023-12-13','prescription_payment','paid'),
(3,1,'400','2023-12-13','test_prescription_payment','paid');

/*Table structure for table `pharmacy` */

DROP TABLE IF EXISTS `pharmacy`;

CREATE TABLE `pharmacy` (
  `pharmacy_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `pharmacy_name` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `floor` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`pharmacy_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `pharmacy` */

insert  into `pharmacy`(`pharmacy_id`,`login_id`,`pharmacy_name`,`phone`,`email`,`floor`) values 
(1,5,'pharmacy','1234567890','pharmacy@gmail.com','0');

/*Table structure for table `physical_conditions` */

DROP TABLE IF EXISTS `physical_conditions`;

CREATE TABLE `physical_conditions` (
  `physical_condition_id` int(11) NOT NULL AUTO_INCREMENT,
  `patient_id` int(11) DEFAULT NULL,
  `blood_pressure` varchar(255) DEFAULT NULL,
  `sugar` varchar(255) DEFAULT NULL,
  `cholesterol` varchar(255) DEFAULT NULL,
  `height` varchar(255) DEFAULT NULL,
  `weight` varchar(255) DEFAULT NULL,
  `date_time` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`physical_condition_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `physical_conditions` */

/*Table structure for table `prescription` */

DROP TABLE IF EXISTS `prescription`;

CREATE TABLE `prescription` (
  `prescription_id` int(11) NOT NULL AUTO_INCREMENT,
  `booking_id` int(11) DEFAULT NULL,
  `medicine_id` int(11) DEFAULT NULL,
  `date_time` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `status` varchar(225) DEFAULT NULL,
  PRIMARY KEY (`prescription_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `prescription` */

insert  into `prescription`(`prescription_id`,`booking_id`,`medicine_id`,`date_time`,`description`,`status`) values 
(1,1,2,'2023-12-13','3 times per day after food','forward'),
(2,1,3,'2023-12-14','kurach aduth vedhana olla placeil apply cheyitha marum\r\n','pending');

/*Table structure for table `receptions` */

DROP TABLE IF EXISTS `receptions`;

CREATE TABLE `receptions` (
  `reception_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `floor` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`reception_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `receptions` */

insert  into `receptions`(`reception_id`,`login_id`,`first_name`,`last_name`,`phone`,`email`,`floor`) values 
(1,4,'reception','s','3456789876','reception@gmail.com','0');

/*Table structure for table `request` */

DROP TABLE IF EXISTS `request`;

CREATE TABLE `request` (
  `request_id` int(11) NOT NULL AUTO_INCREMENT,
  `specialist_id` int(11) DEFAULT NULL,
  `booking_id` int(11) DEFAULT NULL,
  `date_time` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`request_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `request` */

insert  into `request`(`request_id`,`specialist_id`,`booking_id`,`date_time`,`status`) values 
(1,1,1,'2023-12-13','accepted');

/*Table structure for table `schedule` */

DROP TABLE IF EXISTS `schedule`;

CREATE TABLE `schedule` (
  `schedule_id` int(11) NOT NULL AUTO_INCREMENT,
  `start_time` varchar(255) DEFAULT NULL,
  `end_time` varchar(255) DEFAULT NULL,
  `date` varchar(255) DEFAULT NULL,
  `doctor_id` int(11) DEFAULT NULL,
  `fee_amount` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`schedule_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `schedule` */

insert  into `schedule`(`schedule_id`,`start_time`,`end_time`,`date`,`doctor_id`,`fee_amount`) values 
(1,'10:30','11:30','2023-12-14',1,'100'),
(2,'12:30','13:30','2023-12-14',2,'200'),
(3,'14:00','15:00','2023-12-22',3,'250');

/*Table structure for table `specialist` */

DROP TABLE IF EXISTS `specialist`;

CREATE TABLE `specialist` (
  `specialist_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `doctor_id` int(11) DEFAULT NULL,
  `speciality` varchar(255) DEFAULT NULL,
  `certifications` varchar(255) DEFAULT NULL,
  `experience` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`specialist_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `specialist` */

insert  into `specialist`(`specialist_id`,`login_id`,`doctor_id`,`speciality`,`certifications`,`experience`) values 
(1,10,3,'cardio','mbbs md phd','7');

/*Table structure for table `stocks` */

DROP TABLE IF EXISTS `stocks`;

CREATE TABLE `stocks` (
  `stock_id` int(11) NOT NULL AUTO_INCREMENT,
  `medicine_id` int(11) DEFAULT NULL,
  `quantity` varchar(100) DEFAULT NULL,
  `total` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`stock_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `stocks` */

/*Table structure for table `test_prescription` */

DROP TABLE IF EXISTS `test_prescription`;

CREATE TABLE `test_prescription` (
  `test_pres_id` int(11) NOT NULL AUTO_INCREMENT,
  `booking_id` int(11) DEFAULT NULL,
  `test_id` int(11) DEFAULT NULL,
  `lab_description` varchar(255) DEFAULT NULL,
  `report_file` varchar(255) DEFAULT NULL,
  `rate` varchar(255) DEFAULT NULL,
  `date_time` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`test_pres_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `test_prescription` */

insert  into `test_prescription`(`test_pres_id`,`booking_id`,`test_id`,`lab_description`,`report_file`,`rate`,`date_time`) values 
(1,1,1,'left leg test','static/72f7eacd-e7c8-46c5-a119-c56a8bb411a7blur.jpg','500','2023-12-14');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
