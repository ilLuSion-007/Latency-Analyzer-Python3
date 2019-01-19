-- phpMyAdmin SQL Dump
-- version 4.8.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jul 22, 2018 at 10:48 AM
-- Server version: 5.5.40-0ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.22

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `latency`
--

-- --------------------------------------------------------

--
-- Table structure for table `domains`
--

CREATE TABLE `domains` (
  `Id` int(11) NOT NULL,
  `Domain` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `domains`
--

INSERT INTO `domains` (`Id`, `Domain`) VALUES
(1, 'nike.com'),
(2, 'google.com'),
(3, 'instagram.com'),
(4, 'ebay.in'),
(5, 'gmail.com'),
(6, 'youtube.com'),
(7, 'linkedin.com'),
(8, 'twitter.com'),
(9, 'facebook.com'),
(10, 'amazon.com'),
(11, 'flipkart.com'),
(12, 'cricbuzz.com'),
(13, 'quora.com'),
(14, 'hotstar.com'),
(15, 'jeevansathi.com'),
(16, 'olacabs.com'),
(17, 'uber.com'),
(18, 'shopclues.com'),
(19, 'grammarly.com'),
(20, 'shopperstop.com'),
(21, 'paytm.com'),
(22, 'shaadi.com'),
(23, 'bookmyshow.com'),
(24, 'indiabix.com'),
(25, 'twitter.com'),
(26, 'lifestyle.com'),
(27, 'puma.com'),
(28, 'fastrack.com'),
(29, 'netflix.com'),
(30, 'paisabazar.com'),
(31, 'snapdeal.com'),
(32, 'whatsapp.com'),
(33, 'mba.com'),
(34, 'jio.com'),
(35, 'olx.com'),
(36, 'mygov.in'),
(37, 'redbus.com'),
(38, 'pantaloons.com'),
(39, 'myantra.com'),
(40, 'edwisor.com'),
(41, 'godaddy.com'),
(42, 'swd.com'),
(43, 'udemy.com'),
(44, 'jetairways.com'),
(45, 'indigo.com'),
(46, 'airindia.com'),
(47, 'duke.com'),
(48, 'tatacliq.com'),
(49, 'elisa.fi'),
(50, 'amazon.in'),
(51, 'aliexpress.com'),
(52, 'suomi.fi'),
(53, 'mtv.fi'),
(54, 'sanakirja.org'),
(55, 'mail.ru'),
(56, 'hs.fi'),
(57, 'yandex.ru'),
(58, 'tori.fi'),
(59, 'live.com'),
(60, 'dailymail.co.uk'),
(61, 'messenger.com'),
(62, 'anz.com'),
(63, 'theguardian.com'),
(64, 'providr.com'),
(65, 'smh.com.au'),
(66, 'ladbible.com'),
(67, 't.co'),
(68, 'seek.com.au'),
(69, 'edx.com'),
(70, 'policybazzar.com'),
(71, 'diply.com'),
(72, 'twitch.tv'),
(73, 'lenskart.com'),
(74, 'upschoolarship.com'),
(75, 'imgur.com'),
(76, 'office.com'),
(77, 'github.com'),
(78, 'aparat.com'),
(79, 'blogspot.com'),
(80, 'freejobalerts.com'),
(81, 'imdb.com'),
(82, 'softonic.com'),
(83, 'moneycontrol.com'),
(84, 'onlinesbi.com'),
(85, 'indiatimes.com'),
(86, 'irctc.co.in'),
(87, 'myntra.com'),
(88, 'popads.net'),
(89, 'hdfcbank.com'),
(90, 'uidai.gov.in'),
(91, 'livejasmin.com'),
(92, 'stackoverflow.com'),
(93, 'shine.com'),
(94, 'Billdesk.com'),
(95, 'Rediff.com'),
(96, 'ndtv.in'),
(97, 'alibaba.com'),
(98, 'mohanitea.com'),
(99, 'sunrise.com'),
(100, 'ajanta.com');

-- --------------------------------------------------------

--
-- Table structure for table `ipasnlat`
--

CREATE TABLE `ipasnlat` (
  `id` int(11) NOT NULL,
  `domain` varchar(255) DEFAULT NULL,
  `ip` varchar(255) DEFAULT NULL,
  `ASN` varchar(255) DEFAULT NULL,
  `Latency` varchar(255) DEFAULT NULL,
  `d_latitude` varchar(11) DEFAULT NULL,
  `d_longitude` varchar(11) DEFAULT NULL,
  `d_city` varchar(30) DEFAULT NULL,
  `d_country` varchar(30) DEFAULT NULL,
  `d_country_code` varchar(11) DEFAULT NULL,
  `c_asn` varchar(11) DEFAULT NULL,
  `client_ip` varchar(255) DEFAULT NULL,
  `c_country` varchar(50) DEFAULT NULL,
  `c_country_code` varchar(5) DEFAULT NULL,
  `c_city` varchar(50) DEFAULT NULL,
  `c_longitude` varchar(255) DEFAULT NULL,
  `c_latitude` varchar(255) DEFAULT NULL,
  `date_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `domains`
--
ALTER TABLE `domains`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `ipasnlat`
--
ALTER TABLE `ipasnlat`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `domains`
--
ALTER TABLE `domains`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=101;

--
-- AUTO_INCREMENT for table `ipasnlat`
--
ALTER TABLE `ipasnlat`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
