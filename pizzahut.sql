-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 12, 2020 at 05:56 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pizzahut`
--

-- --------------------------------------------------------

--
-- Table structure for table `order`
--

CREATE TABLE `order` (
  `ORDER_ID` int(10) NOT NULL,
  `SHOP_ID` char(10) NOT NULL,
  `ORDER_DATE_TIME` date NOT NULL,
  `ADDRESS_ID` int(10) NOT NULL,
  `STATUS` char(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `order`
--

INSERT INTO `order` (`ORDER_ID`, `SHOP_ID`, `ORDER_DATE_TIME`, `ADDRESS_ID`, `STATUS`) VALUES
(1, 'S0001', '2019-10-29', 0, 'submit'),
(19, 'S0001', '2020-04-10', 0, 'submit'),
(20, 'S0001', '2020-04-10', 0, 'submit'),
(21, 'S0001', '2020-04-11', 0, 'submit'),
(22, 'S0001', '2020-04-11', 0, ''),
(23, 'S0001', '2020-04-11', 1, 'submit'),
(24, 'S0001', '2020-04-11', 1, 'submit'),
(25, 'S0001', '2020-04-11', 1, 'Shipped'),
(26, 'S0001', '2020-04-09', 0, 'Prepared'),
(33, 'S0002', '2020-04-12', 1, 'submit');

-- --------------------------------------------------------

--
-- Table structure for table `order_product`
--

CREATE TABLE `order_product` (
  `ORDER_ID` int(10) NOT NULL,
  `PRODUCT_ID` char(10) NOT NULL,
  `QUANTITY` int(11) NOT NULL,
  `PRICE` int(11) NOT NULL,
  `ORDER_PRODUCT_ID` int(11) NOT NULL,
  `LINK_PRODUCT` char(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `order_product`
--

INSERT INTO `order_product` (`ORDER_ID`, `PRODUCT_ID`, `QUANTITY`, `PRICE`, `ORDER_PRODUCT_ID`, `LINK_PRODUCT`) VALUES
(26, '106B', 3, 480, 1, '/'),
(26, 'C101', 3, 0, 2, '0'),
(19, '109B', 3, 450, 3, '/'),
(19, 'C101', 3, 0, 4, '0'),
(20, '106B', 6, 960, 5, '/'),
(20, 'C101', 6, 0, 6, '0'),
(20, '108A', 1, 131, 7, '/'),
(20, 'C103', 1, 19, 8, '2'),
(21, '109A', 3, 318, 9, '/'),
(21, 'C101', 3, 0, 10, '0'),
(21, '105B', 7, 1120, 11, '/'),
(21, 'C103', 7, 133, 12, '2'),
(22, '104A', 3, 486, 13, '/'),
(22, 'C102', 3, 0, 14, '0'),
(23, '109B', 6, 900, 15, '/'),
(23, 'C102', 6, 0, 16, '0'),
(24, '107B', 6, 960, 17, '/'),
(24, 'C102', 6, 0, 18, '0'),
(25, '107A', 3, 402, 19, '/'),
(25, 'C101', 3, 0, 20, '0'),
(33, '107B', 4, 640, 21, '/'),
(33, 'C101', 4, 0, 22, '0');

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `PRODUCT_ID` char(10) NOT NULL,
  `PRODUCT_NAME` char(100) NOT NULL,
  `PRODUCT_PRICE` int(11) NOT NULL,
  `PRODUCT_CATEGORY` char(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`PRODUCT_ID`, `PRODUCT_NAME`, `PRODUCT_PRICE`, `PRODUCT_CATEGORY`) VALUES
('101B', 'SUPER SUPREME (L)', 186, 'PIZZA'),
('102A', 'SEAFOOD SUPREME (R)', 160, 'PIZZA'),
('102B', 'SEAFOOD SUPREME (L)', 196, 'PIZZA'),
('103A', 'WICKED CHICKEN (R)', 159, 'PIZZA'),
('103B', 'WICKED CHICKEN (L)', 195, 'PIZZA'),
('104A', 'DEVILISH SCALLOPS (R)', 162, 'PIZZA'),
('104B', 'DEVILISH SCALLOPS (L)', 201, 'PIZZA'),
('105A', 'MEAT SUPREME (R)', 134, 'PIZZA'),
('105B', 'MEAT SUPREME (L)', 160, 'PIZZA'),
('106A', 'VEGGIE SUPREME (R)', 134, 'PIZZA'),
('106B', 'VEGGIE SUPREME (L)', 160, 'PIZZA'),
('107A', 'CHICKEN SUPREME (R)', 134, 'PIZZA'),
('107B', 'CHICKEN SUPREME (L)', 160, 'PIZZA'),
('108A', 'SUPREME (R)', 131, 'PIZZA'),
('108B', 'SUPREME (L)', 160, 'PIZZA'),
('109A', 'CHEESE LOVER (R)', 106, 'PIZZA'),
('109B', 'CHEESE LOVER (L)', 150, 'PIZZA'),
('110A', 'THOUSAND ISLAND SEAFOOD (R)', 150, 'PIZZA'),
('110B', 'THOUSAND ISLAND SEAFOOD (L)', 180, 'PIZZA'),
('201', 'Spaghetti Americana', 70, 'RICE/PASTA'),
('202', 'Spaghetti Bolognese (Beef)', 80, 'RICE/PASTA'),
('203', 'Lasagne', 90, 'RICE/PASTA'),
('204', 'Spanish Seafood Fried Rice', 80, 'RICE/PASTA'),
('205', 'Seafood Rice Doria', 80, 'RICE/PASTA'),
('206', 'BBQ Ribs Fried Rice', 90, 'RICE/PASTA'),
('207', 'ITALIAN CHICKEN RICE', 66, 'RICE/PASTA'),
('208', 'PRAWNS AND BABY SCALLOP RICE', 72, 'RICE/PASTA'),
('209', 'ITALIAN CHICKEN SPAGHETTI', 66, 'RICE/PASTA'),
('210', 'BAKED SPINACH AND MUSHROOM PENNE WITH CHEESE', 59, 'RICE/PASTA'),
('301', 'Crispy Shrimps Platter', 55, 'STARTER'),
('302', 'BBQ Ribs Platter', 65, 'STARTER'),
('303', 'Garlic Bread', 20, 'STARTER'),
('304', 'Minestrone', 20, 'STARTER'),
('305', 'Pumpkin Quinoa Soup', 20, 'STARTER'),
('306', 'Chicken Mushroom Soup', 20, 'STARTER'),
('307', 'Lobster Bisque', 30, 'STARTER'),
('308', 'Avocado Quinoa Salad', 25, 'STARTER'),
('309', 'Caesar Salad', 25, 'STARTER'),
('310', 'Grilled Chicken Caesar Salad', 35, 'STARTER'),
('311', 'Chef’s Salad', 50, 'STARTER'),
('400A', 'No Drink', 0, 'DRINK'),
('401A', 'Pespi', 9, 'DRINK'),
('401B', 'Pespi (2)', 16, 'DRINK'),
('402A', 'Lemon Tea (can)', 10, 'DRINK'),
('402B', 'Lemon Tea (2 cans)', 18, 'DRINK'),
('403A', 'Fanta', 9, 'DRINK'),
('403B', 'Fanta (2)', 16, 'DRINK'),
('404', 'PEPSI -BOTTLE', 28, 'DRINK'),
('405', '7 UP -BOTTLE', 28, 'DRINK'),
('501', 'SOUFFL? CHEESE CAKE', 32, 'DESSERT'),
('502', 'OREO CHOCOLATE PARFAIT', 25, 'DESSERT'),
('503', 'VENETO LAYER PASTRY', 54, 'DESSERT'),
('504', 'CINNAMON APPLE CRUMBLE PIE', 34, 'DESERT'),
('701A', 'DEVILISH SCALLOPS (R)', 162, 'SPECIAL'),
('701B', 'DEVILISH SCALLOPS (R)', 192, 'SPECIAL'),
('901A', 'PIZZA CREATOR (R)', 115, 'CREATE'),
('901B', 'PIZZA CREATOR (L)', 151, 'CREATE'),
('A101', 'Set A', 459, 'SET'),
('A102', 'Set B', 250, 'SET'),
('A103', 'Set C', 233, 'SET'),
('C101', 'PAN', 0, 'CRUST'),
('C102', 'THIN\' N', 0, 'CRUST'),
('C103', 'STUFFED', 19, 'CRUST'),
('C201', 'Spaghetti Americana', 15, 'RICE/PASTA'),
('C202', 'Spaghetti Bolognese (Beef)', 15, 'RICE/PASTA'),
('C203', 'Lasagne', 25, 'RICE/PASTA'),
('C204', 'Spanish Seafood Fried Rice', 15, 'RICE/PASTA'),
('C205', 'Seafood Rice Doria', 15, 'RICE/PASTA'),
('C206', 'BBQ Ribs Fried Rice', 25, 'RICE/PASTA'),
('C301', 'MASHED POTATO WITH CLAMS', 10, 'STARTER'),
('C302', 'BBQ Ribs Platter', 20, 'STARTER'),
('C303', 'CHICKEN WINGS', 0, 'STARTER'),
('C901', 'TUNA', 18, 'CREATECHOICE'),
('C902', 'BEEF', 18, 'CREATECHOICE'),
('C903', 'BACON', 18, 'CREATECHOICE'),
('C904', 'CORN', 18, 'CREATECHOICE'),
('C905', 'CHICKEN', 18, 'CREATECHOICE'),
('C906', 'HAM', 18, 'CREATECHOICE'),
('C907', 'EXTRA CHEESE', 18, 'CREATECHOICE'),
('C908', 'PORK', 18, 'CREATECHOICE');

-- --------------------------------------------------------

--
-- Table structure for table `shop_login`
--

CREATE TABLE `shop_login` (
  `Shop_id` char(10) NOT NULL,
  `username` varchar(10) NOT NULL,
  `password` varchar(10) NOT NULL,
  `Shop_name` char(30) NOT NULL,
  `Shop_location` char(150) NOT NULL,
  `Shop_tel` char(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `shop_login`
--

INSERT INTO `shop_login` (`Shop_id`, `username`, `password`, `Shop_name`, `Shop_location`, `Shop_tel`) VALUES
('S0001', 'asd', '123', 'PizzaHut Metro City Phase 2', 'Shop No 2071-72, Level 2, Metro City Phase II, Tseung Kwan O, NT', '31945010'),
('S0002', 'qwe', '123', 'PizzaHut Apm Millennium City 5', 'Shop No. L2-1, Level 2, APM, Millennium City 5, 418 Kwun Tong Road, Kwun Tong, Kln.', '25929368');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `order`
--
ALTER TABLE `order`
  ADD PRIMARY KEY (`ORDER_ID`),
  ADD UNIQUE KEY `ORDER_ID` (`ORDER_ID`);

--
-- Indexes for table `order_product`
--
ALTER TABLE `order_product`
  ADD PRIMARY KEY (`ORDER_PRODUCT_ID`),
  ADD UNIQUE KEY `ORDER_PRODUCT_ID` (`ORDER_PRODUCT_ID`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`PRODUCT_ID`),
  ADD UNIQUE KEY `PRODUCT_ID` (`PRODUCT_ID`);

--
-- Indexes for table `shop_login`
--
ALTER TABLE `shop_login`
  ADD PRIMARY KEY (`Shop_id`),
  ADD UNIQUE KEY `Shop_id` (`Shop_id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `Shop_name` (`Shop_name`),
  ADD UNIQUE KEY `Shop_location` (`Shop_location`),
  ADD UNIQUE KEY `Shop_tel` (`Shop_tel`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `order`
--
ALTER TABLE `order`
  MODIFY `ORDER_ID` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
