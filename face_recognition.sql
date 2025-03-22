-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 06, 2025 at 06:49 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `face_recognition`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `fname` varchar(1000) NOT NULL,
  `lname` varchar(1000) NOT NULL,
  `cnum` int(225) NOT NULL,
  `email` varchar(1000) NOT NULL,
  `ssq` varchar(1000) NOT NULL,
  `sa` varchar(1000) NOT NULL,
  `pwd` int(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Table structure for table `stdattendance`
--

CREATE TABLE attendance (
    atten_id INT AUTO_INCREMENT PRIMARY KEY,
    Student_ID INT,
    atten_time TIME(6),
    atten_date DATE,
    atten_status VARCHAR(20),
    FOREIGN KEY (Student_ID) REFERENCES student(Student_ID) ON DELETE CASCADE
);
CREATE TABLE `stdattendance` (
  `std_id` int(225) NOT NULL,
  `std_roll_no` int(225) NOT NULL,
  `std_name` varchar(1000) NOT NULL,
  `std_time` time(6) NOT NULL,
  `std_date` date NOT NULL,
  `std_attendance` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `stdattendance`
--

INSERT INTO `stdattendance` (`std_id`, `std_roll_no`, `std_name`, `std_time`, `std_date`, `std_attendance`) VALUES
(1, 1, 'jyoti', '12:12:00.000000', '2025-03-05', 'Present'),
(1, 1, 'jyoti', '12:12:00.000000', '2025-03-05', 'Present');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `Student_ID` int(225) NOT NULL,
  `Name` varchar(1000) NOT NULL,
  `Department` varchar(1000) NOT NULL,
  `Course` varchar(1000) NOT NULL,
  `Year` varchar(1000) NOT NULL,
  `Semester` varchar(1000) NOT NULL,
  `Division` varchar(1000) NOT NULL,
  `Gender` varchar(1000) NOT NULL,
  `DOB` date NOT NULL,
  `Mobile_No` bigint(225) NOT NULL,
  `Address` varchar(1000) NOT NULL,
  `Roll_No` varchar(1000) NOT NULL,
  `Email` varchar(1000) NOT NULL,
  `Teacher_Name` varchar(1000) NOT NULL,
  `PhotoSample` blob NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`Student_ID`, `Name`, `Department`, `Course`, `Year`, `Semester`, `Division`, `Gender`, `DOB`, `Mobile_No`, `Address`, `Roll_No`, `Email`, `Teacher_Name`, `PhotoSample`) VALUES
(1, 'jyoti', 'BSIT', 'TE', '2018-22', 'Semester-4', 'Morning', 'Male', '0000-00-00', 9888888888, 'koteshwor', '1', 'jyotigmail', 'nun', 0x596573);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
