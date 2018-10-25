-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 25, 2018 at 06:20 PM
-- Server version: 10.1.28-MariaDB
-- PHP Version: 7.1.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `fruit_stole`
--

-- --------------------------------------------------------

--
-- Table structure for table `dearjay22`
--

CREATE TABLE `dearjay22` (
  `order_id` int(11) NOT NULL,
  `order_date` date DEFAULT NULL,
  `item_list` text,
  `total_pay` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dearjay22`
--

INSERT INTO `dearjay22` (`order_id`, `order_date`, `item_list`, `total_pay`) VALUES
(1, '2018-10-20', '{\'watermelon\': \'30 ( 0.5Kg ) = 15.0\', \'mango\': \'70 ( 1Kg ) = 70.0\', \'Kiwi\': \'50 ( 2Kg ) = 100.0\'}', '185.0');

-- --------------------------------------------------------

--
-- Table structure for table `fruits`
--

CREATE TABLE `fruits` (
  `fruit_id` int(255) NOT NULL,
  `fruit_name` varchar(255) NOT NULL,
  `fruit_prise` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `fruits`
--

INSERT INTO `fruits` (`fruit_id`, `fruit_name`, `fruit_prise`) VALUES
(1, 'watermelon', '30'),
(2, 'mango', '70'),
(3, 'Kiwi', '50'),
(4, 'banana', '40'),
(5, 'Chikku', '150');

-- --------------------------------------------------------

--
-- Table structure for table `hatt_123`
--

CREATE TABLE `hatt_123` (
  `order_id` int(11) NOT NULL,
  `order_date` date DEFAULT NULL,
  `item_list` text,
  `total_pay` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hatt_123`
--

INSERT INTO `hatt_123` (`order_id`, `order_date`, `item_list`, `total_pay`) VALUES
(1, '2018-10-21', '{\'Chikku\': \'150 ( 3Kg ) = 450.0\'}', '450.0');

-- --------------------------------------------------------

--
-- Table structure for table `kajolp550`
--

CREATE TABLE `kajolp550` (
  `order_id` int(11) NOT NULL,
  `order_date` date DEFAULT NULL,
  `item_list` text,
  `total_pay` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `kajolp550`
--

INSERT INTO `kajolp550` (`order_id`, `order_date`, `item_list`, `total_pay`) VALUES
(1, '2018-10-20', '{\'watermelon\': \'30 ( 3Kg ) = 90.0\', \'mango\': \'70 ( 1Kg ) = 70.0\', \'Kiwi\': \'50 ( 2Kg ) = 100.0\'}', '260.0'),
(2, '2018-10-20', '{\'watermelon\': \'30 ( 3Kg ) = 90.0\', \'mango\': \'70 ( 1Kg ) = 70.0\', \'Kiwi\': \'50 ( 2Kg ) = 100.0\'}', '260.0'),
(3, '2018-10-20', '{\'watermelon\': \'30 ( 3Kg ) = 90.0\', \'mango\': \'70 ( 1Kg ) = 70.0\', \'Kiwi\': \'50 ( 2Kg ) = 100.0\'}', '260.0'),
(4, '2018-10-20', '{\'Chikku\': \'150 ( 3Kg ) = 450.0\'}', '450.0');

-- --------------------------------------------------------

--
-- Table structure for table `meena`
--

CREATE TABLE `meena` (
  `order_id` int(11) NOT NULL,
  `order_date` date DEFAULT NULL,
  `item_list` text,
  `total_pay` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `meena`
--

INSERT INTO `meena` (`order_id`, `order_date`, `item_list`, `total_pay`) VALUES
(1, '2018-10-20', '{\'banana\': \'40 ( 1Kg ) = 40.0\'}', '40.0'),
(2, '2018-10-20', '{\'watermelon\': \'30 ( 1Kg ) = 30.0\', \'mango\': \'70 ( 1Kg ) = 70.0\', \'Kiwi\': \'50 ( 1Kg ) = 50.0\'}', '150.0'),
(3, '2018-10-20', '{\'watermelon\': \'30 ( 1Kg ) = 30.0\', \'mango\': \'70 ( 1Kg ) = 70.0\', \'Kiwi\': \'50 ( 1Kg ) = 50.0\'}', '150.0');

-- --------------------------------------------------------

--
-- Table structure for table `mitulp236`
--

CREATE TABLE `mitulp236` (
  `order_id` int(11) NOT NULL,
  `order_date` date DEFAULT NULL,
  `item_list` text,
  `total_pay` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `mitulp236`
--

INSERT INTO `mitulp236` (`order_id`, `order_date`, `item_list`, `total_pay`) VALUES
(77, '2018-10-20', '{\'watermelon\': \'30 ( 1Kg ) = 30.0\', \'mango\': \'70 ( 1Kg ) = 70.0\', \'Kiwi\': \'50 ( 1Kg ) = 50.0\'}', '150.0'),
(78, '2018-10-20', '{\'mango\': \'70 ( 1Kg ) = 70.0\'}', '70.0'),
(79, '2018-10-20', '{\'mango\': \'70 ( 1Kg ) = 70.0\'}', '70.0'),
(80, '2018-10-21', '{\'banana\': \'40 ( 2Kg ) = 80.0\', \'Chikku\': \'150 ( 2Kg ) = 300.0\'}', '380.0'),
(81, '2018-10-21', '{\'mango\': \'70 ( 1Kg ) = 70.0\', \'Kiwi\': \'50 ( 1Kg ) = 50.0\'}', '120.0'),
(82, '2018-10-21', '{\'mango\': \'70 ( 1Kg ) = 70.0\', \'Kiwi\': \'50 ( 1Kg ) = 50.0\'}', '120.0');

-- --------------------------------------------------------

--
-- Table structure for table `regester`
--

CREATE TABLE `regester` (
  `id` int(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `contact` varchar(255) NOT NULL,
  `address` text NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `regester`
--

INSERT INTO `regester` (`id`, `name`, `username`, `email`, `contact`, `address`, `password`) VALUES
(20, 'Mitul Patel', 'mitulp236', 'mitulp236@gmail.com', '8140850797', 'Mehsana\r\nShahibaug township,radhanpur road', '123'),
(21, 'meena patel', 'meena', 'meenapatel280674@gmail.com', '9998362935', 'c-7\r\ntirupati shahibaug township radhanpur road mehsana-2\r\nmehsana', '123'),
(23, 'rozzy desuza', 'rozzy', 'rozzydesuza@gmail.com', '12345678', 'Mehsana\r\nShahibaug township,radhanpur road', '123'),
(24, 'test', 'test', 'test@gmail.com', '789654123', 'dafaf', '123'),
(25, 'kajol', 'kajolp550', 'kajolp550@gmail.com', '7575002454', 'somewhere on amdavad !', '123'),
(26, 'jay patel', 'dearjay22', 'dearjayu22@gmail.com', '3e11313', 'somewhere on mehona', '123'),
(27, 'hatt', 'hatt_123', 'dhfjgd@gmail.com', '5641578576868', 'dgrfyhytuj', 'hatt');

-- --------------------------------------------------------

--
-- Table structure for table `rozzy`
--

CREATE TABLE `rozzy` (
  `order_id` int(11) NOT NULL,
  `order_date` date DEFAULT NULL,
  `item_list` text,
  `total_pay` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `test`
--

CREATE TABLE `test` (
  `order_id` int(11) NOT NULL,
  `order_date` date DEFAULT NULL,
  `item_list` text,
  `total_pay` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `dearjay22`
--
ALTER TABLE `dearjay22`
  ADD PRIMARY KEY (`order_id`);

--
-- Indexes for table `fruits`
--
ALTER TABLE `fruits`
  ADD PRIMARY KEY (`fruit_id`);

--
-- Indexes for table `hatt_123`
--
ALTER TABLE `hatt_123`
  ADD PRIMARY KEY (`order_id`);

--
-- Indexes for table `kajolp550`
--
ALTER TABLE `kajolp550`
  ADD PRIMARY KEY (`order_id`);

--
-- Indexes for table `meena`
--
ALTER TABLE `meena`
  ADD PRIMARY KEY (`order_id`);

--
-- Indexes for table `mitulp236`
--
ALTER TABLE `mitulp236`
  ADD PRIMARY KEY (`order_id`);

--
-- Indexes for table `regester`
--
ALTER TABLE `regester`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `rozzy`
--
ALTER TABLE `rozzy`
  ADD PRIMARY KEY (`order_id`);

--
-- Indexes for table `test`
--
ALTER TABLE `test`
  ADD PRIMARY KEY (`order_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `dearjay22`
--
ALTER TABLE `dearjay22`
  MODIFY `order_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `fruits`
--
ALTER TABLE `fruits`
  MODIFY `fruit_id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `hatt_123`
--
ALTER TABLE `hatt_123`
  MODIFY `order_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `kajolp550`
--
ALTER TABLE `kajolp550`
  MODIFY `order_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `meena`
--
ALTER TABLE `meena`
  MODIFY `order_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `mitulp236`
--
ALTER TABLE `mitulp236`
  MODIFY `order_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=83;

--
-- AUTO_INCREMENT for table `regester`
--
ALTER TABLE `regester`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `rozzy`
--
ALTER TABLE `rozzy`
  MODIFY `order_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `test`
--
ALTER TABLE `test`
  MODIFY `order_id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
