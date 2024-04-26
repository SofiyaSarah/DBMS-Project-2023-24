-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Mar 03, 2024 at 04:26 AM
-- Server version: 8.2.0
-- PHP Version: 8.2.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `lms`
--

-- --------------------------------------------------------

--
-- Table structure for table `course`
--

DROP TABLE IF EXISTS `course`;
CREATE TABLE IF NOT EXISTS `course` (
  `cname` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `cid` varchar(50) NOT NULL,
  `credits` int NOT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `course`
--

INSERT INTO `course` (`cname`, `cid`, `credits`) VALUES
('gsgra', '0', 4),
('ash', '2', 2024),
('DBMS', '21', 2024);

-- --------------------------------------------------------

--
-- Table structure for table `instructor`
--

DROP TABLE IF EXISTS `instructor`;
CREATE TABLE IF NOT EXISTS `instructor` (
  `name` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `email` text NOT NULL,
  `pwd` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `qual` text NOT NULL,
  `pno` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `instructor`
--

INSERT INTO `instructor` (`name`, `email`, `pwd`, `qual`, `pno`) VALUES
('ada', 'a@b.com', 'c83b2d5bb1fb4d93d9d064593ed6eea2', 'BE', 1236547896),
('aaaa', 'aa@b.com', 'a25e0e62a4702353f399953579424997', 'BE', 1236547892);

-- --------------------------------------------------------

--
-- Table structure for table `learning_module`
--

DROP TABLE IF EXISTS `learning_module`;
CREATE TABLE IF NOT EXISTS `learning_module` (
  `module_name` text NOT NULL,
  `module_type` text NOT NULL,
  `module_content` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `learning_module`
--

INSERT INTO `learning_module` (`module_name`, `module_type`, `module_content`) VALUES
('frwg', 'tgeh3', '        ghghfdtfdg');

-- --------------------------------------------------------

--
-- Table structure for table `learning_type`
--

DROP TABLE IF EXISTS `learning_type`;
CREATE TABLE IF NOT EXISTS `learning_type` (
  `t_id` int NOT NULL,
  `t_name` text NOT NULL,
  `t_type` text NOT NULL,
  `rtype` text NOT NULL,
  `file` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `learning_type`
--

INSERT INTO `learning_type` (`t_id`, `t_name`, `t_type`, `rtype`, `file`) VALUES
(5, 'hdk', '   jyf     ', 'null', 0);

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
CREATE TABLE IF NOT EXISTS `student` (
  `name` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `uname` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `email` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `pno` bigint NOT NULL,
  `branch` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `pwd` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`uname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`name`, `uname`, `email`, `pno`, `branch`, `pwd`) VALUES
('', '', '', 0, '', 'd41d8cd98f00b204e9800998ecf8427e'),
('aaa', '4JNAI125', 'tanishahosur1@gmail.com', 1254789563, 'aiml', '19e09d526af9bf98eabdd4a76ed180d1'),
('aaa', 'aaa', 'a@b.com', 9900920001, 'cse', '9990775155c3518a0d7917f7780b24aa'),
('vatrsha', 'ajashdkjsdhjsdhf', 'a@bbb.com', 366563565526, 'aiml', '9b7626c55112e4a7834826923132bc70');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
