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
-- Database: `ubereat`
--

-- --------------------------------------------------------

--
-- Table structure for table `member_address`
--

CREATE TABLE `member_address` (
  `Address` char(150) NOT NULL,
  `address_id` int(10) NOT NULL,
  `member_id` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `member_address`
--

INSERT INTO `member_address` (`Address`, `address_id`, `member_id`) VALUES
('SHOP', 0, 0),
('flat x, 32/f, blk 127, happy plaza. diamond road, nt, hk', 1, 1),
('test', 2, 2),
('flat z, 66/f, blk 127, sad plaza. diamond road, kln, hk', 3, 1),
('flat y, 32/f, blk 127, happy plaza. diamond road, kln, hk', 4, 1),
('flat z, 32/f, blk 127, happy plaza. diamond road, kln, hk', 5, 2),
('test1234', 6, 1),
('hi', 7, 1),
('yo', 8, 1),
('t', 9, 1);

-- --------------------------------------------------------

--
-- Table structure for table `member_data`
--

CREATE TABLE `member_data` (
  `PHONE_NUMBER` int(40) DEFAULT NULL,
  `CUSTOMER_SURNAME` varchar(40) NOT NULL,
  `MEMBER_ID` int(100) NOT NULL,
  `EMAIL` varchar(80) NOT NULL,
  `PASSWORD` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `member_data`
--

INSERT INTO `member_data` (`PHONE_NUMBER`, `CUSTOMER_SURNAME`, `MEMBER_ID`, `EMAIL`, `PASSWORD`) VALUES
(123, 'Li', 1, '123@gmail.com', '123'),
(12345678, 'Wong', 2, 'kenton@kmail.com', '12345678'),
(87654321, 'Poon', 3, 'panda@pmail.com', '12345678'),
(88888888, 'Ma', 4, 'mky@monkey.com', '88888888'),
(99998888, 'Lam', 5, 'timmy@tmail.com', '12345678');

-- --------------------------------------------------------

--
-- Table structure for table `member_payment`
--

CREATE TABLE `member_payment` (
  `Credit_card_number` char(16) NOT NULL,
  `CSV` char(3) NOT NULL,
  `Expiry_date` char(5) NOT NULL,
  `Credit_card_name` char(50) NOT NULL,
  `member_id` int(100) NOT NULL,
  `payment_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `member_payment`
--

INSERT INTO `member_payment` (`Credit_card_number`, `CSV`, `Expiry_date`, `Credit_card_name`, `member_id`, `payment_id`) VALUES
('cash', '', '', '', 0, 0),
('1234432112344321', '240', '12/22', 'Li Yat Long', 1, 1),
('1233455633221442', '134', '22/44', 'hehshethesh', 1, 3),
('123123132131213', '123', '123', '123', 1, 4);

-- --------------------------------------------------------

--
-- Table structure for table `order`
--

CREATE TABLE `order` (
  `ORDER_ID` int(10) NOT NULL,
  `ORDER_STATUS` char(10) NOT NULL,
  `SHOP_ID` char(10) NOT NULL,
  `ORDER_DATE_TIME` varchar(40) NOT NULL,
  `address_id` int(10) NOT NULL,
  `payment_id` int(10) NOT NULL,
  `MEMBER_ID` int(100) NOT NULL,
  `DELIVERY_FEE` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `order`
--

INSERT INTO `order` (`ORDER_ID`, `ORDER_STATUS`, `SHOP_ID`, `ORDER_DATE_TIME`, `address_id`, `payment_id`, `MEMBER_ID`, `DELIVERY_FEE`) VALUES
(1, '1', 'S0001', '2019-12-02', 0, 0, 0, 0),
(12, 's', '', '123', 0, 0, 0, 0),
(13, 's', '', '123', 0, 0, 0, 0),
(14, 's', '', '123', 0, 0, 0, 0),
(15, 's', '', '123', 0, 0, 0, 0),
(26, 'Prepared', 'S0002', '2020/04/12 19:23:30', 1, 1, 1, 0),
(27, 'submit', 'S0002', '2020/04/12 19:33:40', 0, 1, 1, 0),
(28, 'submit', 'S0001', '2020/04/12 21:20:20', 1, 1, 1, 20),
(29, 'submit', 'S0002', '2020/04/12 21:35:30', 0, 1, 1, 0),
(30, 'submit', 'S0002', '2020/04/12 21:36:04', 0, 0, 1, 0),
(31, 'submit', 'S0002', '2020/04/12 21:36:37', 3, 0, 1, 10),
(32, 'submit', 'S0002', '2020/04/12 23:43:29', 1, 1, 1, 10),
(33, 'submit', 'S0002', '2020/04/12 23:45:35', 1, 1, 1, 10);

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
(26, '109B', 3, 450, 68, '/'),
(26, 'C102', 3, 0, 69, '109B'),
(27, '107B', 2, 320, 70, '/'),
(27, 'C102', 2, 0, 71, '107B'),
(28, '107A', 3, 402, 72, '/'),
(28, 'C102', 3, 0, 73, '107A'),
(29, '107A', 5, 670, 74, '/'),
(29, 'C101', 5, 0, 75, '107A'),
(30, '104A', 1, 162, 76, '/'),
(30, 'C101', 1, 0, 77, '104A'),
(31, '106B', 2, 320, 78, '/'),
(31, 'C102', 2, 0, 79, '106B'),
(32, '104A', 4, 648, 80, '/'),
(32, 'C101', 4, 0, 81, '104A'),
(33, '107B', 4, 640, 82, '/'),
(33, 'C101', 4, 0, 83, '107B');

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
('201A', 'Spaghetti Americana', 70, 'RICE/PASTA'),
('202A', 'Spaghetti Bolognese (Beef)', 80, 'RICE/PASTA'),
('203A', 'Lasagne', 90, 'RICE/PASTA'),
('204A', 'Spanish Seafood Fried Rice', 80, 'RICE/PASTA'),
('205A', 'Seafood Rice Doria', 80, 'RICE/PASTA'),
('206A', 'BBQ Ribs Fried Rice', 90, 'RICE/PASTA'),
('207A', 'ITALIAN CHICKEN RICE', 66, 'RICE/PASTA'),
('208A', 'PRAWNS AND BABY SCALLOP RICE', 72, 'RICE/PASTA'),
('209A', 'ITALIAN CHICKEN SPAGHETTI', 66, 'RICE/PASTA'),
('210A', 'BAKED SPINACH AND MUSHROOM PENNE WITH CHEESE', 59, 'RICE/PASTA'),
('301A', 'Crispy Shrimps Platter', 55, 'STARTER'),
('302A', 'BBQ Ribs Platter', 65, 'STARTER'),
('303A', 'Garlic Bread', 20, 'STARTER'),
('304A', 'Minestrone', 20, 'STARTER'),
('305A', 'Pumpkin Quinoa Soup', 20, 'STARTER'),
('306A', 'Chicken Mushroom Soup', 20, 'STARTER'),
('307A', 'Lobster Bisque', 30, 'STARTER'),
('308A', 'Avocado Quinoa Salad', 25, 'STARTER'),
('309A', 'Caesar Salad', 25, 'STARTER'),
('310A', 'Grilled Chicken Caesar Salad', 35, 'STARTER'),
('311A', 'Chef’s Salad', 50, 'STARTER'),
('400A', 'No Drink', 0, 'DRINK'),
('401A', 'Pespi', 9, 'DRINK'),
('401B', 'Pespi (2)', 16, 'DRINK'),
('402A', 'Lemon Tea (can)', 10, 'DRINK'),
('402B', 'Lemon Tea (2 cans)', 18, 'DRINK'),
('403A', 'Fanta', 9, 'DRINK'),
('403B', 'Fanta (2)', 16, 'DRINK'),
('404A', 'PEPSI -BOTTLE', 28, 'DRINK'),
('405A', '7 UP -BOTTLE', 28, 'DRINK'),
('501A', 'SOUFFL? CHEESE CAKE', 32, 'DESSERT'),
('502A', 'OREO CHOCOLATE PARFAIT', 25, 'DESSERT'),
('503A', 'VENETO LAYER PASTRY', 54, 'DESSERT'),
('504A', 'CINNAMON APPLE CRUMBLE PIE', 34, 'DESERT'),
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
-- Table structure for table `shop`
--

CREATE TABLE `shop` (
  `SHOP_ID` char(10) NOT NULL,
  `SHOP_NAME` char(30) NOT NULL,
  `SHOP_LOCATION` char(150) NOT NULL,
  `SHOP_TEL_NUMBER` char(8) NOT NULL,
  `DELIVERY_FEE` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `shop`
--

INSERT INTO `shop` (`SHOP_ID`, `SHOP_NAME`, `SHOP_LOCATION`, `SHOP_TEL_NUMBER`, `DELIVERY_FEE`) VALUES
('S0001', 'PizzaHut Metro City Phase 2', 'Shop No 2071-72, Level 2, Metro City Phase II, Tseung Kwan O, NT', '31945010', 20),
('S0002', 'PizzaHut Apm Millennium City 5', 'Shop No. L2-1, Level 2, APM, Millennium City 5, 418 Kwun Tong Road, Kwun Tong, Kln.', '25929368', 10);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `member_address`
--
ALTER TABLE `member_address`
  ADD PRIMARY KEY (`address_id`),
  ADD UNIQUE KEY `address_id` (`address_id`);

--
-- Indexes for table `member_data`
--
ALTER TABLE `member_data`
  ADD PRIMARY KEY (`MEMBER_ID`),
  ADD UNIQUE KEY `MEMBER_ID` (`MEMBER_ID`),
  ADD UNIQUE KEY `EMAIL` (`EMAIL`),
  ADD UNIQUE KEY `PHONE_NUMBER` (`PHONE_NUMBER`);

--
-- Indexes for table `member_payment`
--
ALTER TABLE `member_payment`
  ADD PRIMARY KEY (`payment_id`),
  ADD UNIQUE KEY `payment_id` (`payment_id`);

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
  ADD PRIMARY KEY (`ORDER_PRODUCT_ID`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`PRODUCT_ID`),
  ADD UNIQUE KEY `PRODUCT_ID` (`PRODUCT_ID`);

--
-- Indexes for table `shop`
--
ALTER TABLE `shop`
  ADD PRIMARY KEY (`SHOP_ID`),
  ADD UNIQUE KEY `SHOP_ID` (`SHOP_ID`),
  ADD UNIQUE KEY `SHOP_TEL_NUMBER` (`SHOP_TEL_NUMBER`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `member_address`
--
ALTER TABLE `member_address`
  MODIFY `address_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `member_data`
--
ALTER TABLE `member_data`
  MODIFY `MEMBER_ID` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `member_payment`
--
ALTER TABLE `member_payment`
  MODIFY `payment_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `order`
--
ALTER TABLE `order`
  MODIFY `ORDER_ID` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT for table `order_product`
--
ALTER TABLE `order_product`
  MODIFY `ORDER_PRODUCT_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=84;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
