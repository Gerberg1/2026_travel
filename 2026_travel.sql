-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Host: mariadb
-- Generation Time: Mar 12, 2026 at 09:12 PM
-- Server version: 10.6.20-MariaDB-ubu2004
-- PHP Version: 8.3.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `2026_travel`
--

-- --------------------------------------------------------

--
-- Table structure for table `destinations`
--

CREATE TABLE `destinations` (
  `destination_pk` char(32) NOT NULL,
  `destination_name` varchar(50) NOT NULL,
  `destination_description` varchar(255) NOT NULL,
  `destination_city` varchar(40) NOT NULL,
  `destination_country` varchar(40) NOT NULL,
  `user_pk` char(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `destinations`
--

INSERT INTO `destinations` (`destination_pk`, `destination_name`, `destination_description`, `destination_city`, `destination_country`, `user_pk`) VALUES
('02e74f10e0327ad868d138f2b4fdd6f0', 'Table Mountain', 'Flat-topped mountain overlooking Cape Town.', 'Cape Town', 'South Africa', '58b30c329be24c99aa40a56381716ad8'),
('03c7c0ace395d80182db07ae2c30f034', 'Neuschwanstein Castle', 'Fairy-tale castle in Bavaria, Germany.', 'Schwangau', 'Germany', '11d710f7682e41868350c4324605b2b4'),
('0a1b2c3d4e5f67890123456789abcdef', 'The Little Mermaid', 'Famous bronze statue based on Hans Christian Andersen\'s fairy tale.', 'Copenhagen', 'Denmark', '11d710f7682e41868350c4324605b2b4'),
('0d61f8370cad1d412f80b84d143e1257', 'Sydney Opera House', 'Famous performing arts center with unique architecture.', 'Sydney', 'Australia', 'e0470417fa6042cba182e75bb48446a7'),
('11111111111111111111111111111111', 'Amalienborg Palace', 'The home of the Danish royal family with beautiful square and guards.', 'Copenhagen', 'Denmark', '11d710f7682e41868350c4324605b2b4'),
('1234567890abcdef1234567890abcdef', 'Nyhavn Harbor', 'Colorful waterfront area with historic buildings, restaurants, and boats.', 'Copenhagen', 'Denmark', '58b30c329be24c99aa40a56381716ad8'),
('1f0e3dad99908345f7439f8ffabdffc4', 'Colosseum', 'Ancient Roman amphitheater in the heart of Rome.', 'Rome', 'Italy', '11d710f7682e41868350c4324605b2b4'),
('1ff1de774005f8da13f42943881c655f', 'Niagara Falls', 'Famous waterfalls on the US-Canada border.', 'Niagara Falls', 'Canada', '58b30c329be24c99aa40a56381716ad8'),
('22222222222222222222222222222222', 'Copenhagen Zoo', 'One of Europe\'s oldest zoos with a wide variety of animals.', 'Copenhagen', 'Denmark', '58b30c329be24c99aa40a56381716ad8'),
('33333333333333333333333333333333', 'Christianshavn Canal', 'Picturesque canal neighborhood with colorful houses and boats.', 'Copenhagen', 'Denmark', 'e0470417fa6042cba182e75bb48446a7'),
('33e75ff09dd601bbe69f351039152189', 'Stanley Park', 'Beautiful urban park surrounded by water in Vancouver.', 'Vancouver', 'Canada', 'e0470417fa6042cba182e75bb48446a7'),
('37693cfc748049e45d87b8c7d8b9aacd', 'Acropolis', 'Historic citadel with the Parthenon in Athens.', 'Athens', 'Greece', '11d710f7682e41868350c4324605b2b4'),
('3c59dc048e8850243be8079a5c74d079', 'Bondi Beach', 'Popular beach in Sydney with surf culture.', 'Sydney', 'Australia', 'e0470417fa6042cba182e75bb48446a7'),
('44444444444444444444444444444444', 'National Museum of Denmark', 'Museum showcasing Danish history, culture, and artifacts.', 'Copenhagen', 'Denmark', '018cefac58154d209e35672a3000c6c1'),
('45c48cce2e2d7fbdea1afc51c7c6ad26', 'Bondi Icebergs Pool', 'Iconic ocean-side pool near Bondi Beach.', 'Sydney', 'Australia', 'e0470417fa6042cba182e75bb48446a7'),
('4b43b0aee35624cd95b910189b3dc231', 'Tower of London', 'Historic castle and former royal palace.', 'London', 'UK', '018cefac58154d209e35672a3000c6c1'),
('4e732ced3463d06de0ca9a15b6153677', 'Sagrada Familia', 'Famous basilica designed by Gaudí in Barcelona.', 'Barcelona', 'Spain', '11d710f7682e41868350c4324605b2b4'),
('55555555555555555555555555555555', 'Round Tower', 'Historic tower offering panoramic city views and exhibitions.', 'Copenhagen', 'Denmark', '11d710f7682e41868350c4324605b2b4'),
('6512bd43d9caa6e02c990b0a82652dca', 'Louvre Museum', 'Famous art museum housing the Mona Lisa.', 'Paris', 'France', '018cefac58154d209e35672a3000c6c1'),
('66666666666666666666666666666666', 'Copenhagen Opera House', 'Modern opera house located on the waterfront with stunning architecture.', 'Copenhagen', 'Denmark', '58b30c329be24c99aa40a56381716ad8'),
('6f4922f45568161a8cdf4ad2299f6d23', 'Big Ben', 'Iconic clock tower in London\'s Westminster.', 'London', 'UK', '018cefac58154d209e35672a3000c6c1'),
('77777777777777777777777777777777', 'Botanical Garden', 'Beautiful garden with diverse plant collections and greenhouses.', 'Copenhagen', 'Denmark', 'e0470417fa6042cba182e75bb48446a7'),
('7b8b965ad4bca0e41ab51de7b31363a1', 'Shibuya Crossing', 'Famous busy intersection and shopping area in Tokyo.', 'Tokyo', 'Japan', '11d710f7682e41868350c4324605b2b4'),
('88888888888888888888888888888888', 'Copenhagen City Hall', 'Historic city hall building with a large tower and public square.', 'Copenhagen', 'Denmark', '018cefac58154d209e35672a3000c6c1'),
('8e296a067a37563370ded05f5a3bf3ec', 'Great Barrier Reef', 'Largest coral reef system in the world.', 'Cairns', 'Australia', 'e0470417fa6042cba182e75bb48446a7'),
('92eb5ffee6ae2fec3ad71c777531578f', 'Christ the Redeemer', 'Massive statue overlooking Rio de Janeiro.', 'Rio de Janeiro', 'Brazil', '018cefac58154d209e35672a3000c6c1'),
('98f13708210194c475687be6106a3b84', 'Golden Gate Bridge', 'Famous suspension bridge in San Francisco.', 'San Francisco', 'USA', '58b30c329be24c99aa40a56381716ad8'),
('99999999999999999999999999999999', 'Glyptoteket', 'Art museum with classical sculptures and modern art collections.', 'Copenhagen', 'Denmark', '11d710f7682e41868350c4324605b2b4'),
('9ae0ea9e3c9c6e1b9b6252c8395efdc1', 'Statue of Liberty', 'Iconic symbol of freedom in New York Harbor.', 'New York', 'USA', '58b30c329be24c99aa40a56381716ad8'),
('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'Superkilen Park', 'Urban park with global art, playgrounds, and vibrant installations.', 'Copenhagen', 'Denmark', '58b30c329be24c99aa40a56381716ad8'),
('aab3238922bcc25a6f606eb525ffdc56', 'Harbour Bridge', 'Iconic steel arch bridge in Sydney.', 'Sydney', 'Australia', 'e0470417fa6042cba182e75bb48446a7'),
('abcdef1234567890abcdef1234567890', 'Rosenborg Castle', 'Renaissance castle housing royal artifacts and the Danish crown jewels.', 'Copenhagen', 'Denmark', 'e0470417fa6042cba182e75bb48446a7'),
('b6d767d2f8ed5d21a44b0e5886680cb9', 'Machu Picchu', 'Ancient Incan city high in the Andes.', 'Cusco', 'Peru', '018cefac58154d209e35672a3000c6c1'),
('bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb', 'Amager Strandpark', 'Popular beach park with sandy shores, lagoons, and walking paths.', 'Copenhagen', 'Denmark', 'e0470417fa6042cba182e75bb48446a7'),
('c20ad4d76fe97759aa27a0c99bff6710', 'Meiji Shrine', 'Historic Shinto shrine surrounded by forest.', 'Tokyo', 'Japan', '11d710f7682e41868350c4324605b2b4'),
('c51ce410c124a10e0db5e4b97fc2af39', 'Empire State Building', 'Famous skyscraper in Manhattan.', 'New York', 'USA', '58b30c329be24c99aa40a56381716ad8'),
('c9f0f895fb98ab9159f51fd0297e236d', 'Central Park', 'Huge urban park in Manhattan, New York City.', 'New York', 'USA', '58b30c329be24c99aa40a56381716ad8'),
('cccccccccccccccccccccccccccccccc', 'Frederiksberg Gardens', 'Large landscaped park with canals, fountains, and palace views.', 'Copenhagen', 'Denmark', '018cefac58154d209e35672a3000c6c1'),
('d3b07384d113edec49eaa6238ad5ff00', 'Eiffel Tower', 'Iconic iron tower with stunning views over Paris.', 'Paris', 'France', '018cefac58154d209e35672a3000c6c1'),
('dddddddddddddddddddddddddddddddd', 'Experimentarium', 'Interactive science and technology museum for all ages.', 'Copenhagen', 'Denmark', '11d710f7682e41868350c4324605b2b4'),
('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee', 'Cisternerne', 'Underground former water reservoir converted into art exhibition space.', 'Copenhagen', 'Denmark', '58b30c329be24c99aa40a56381716ad8'),
('f1a2b3c4d5e67890123456789abcdef0', 'Tivoli Gardens', 'Historic amusement park with rides, gardens, and live performances.', 'Copenhagen', 'Denmark', '018cefac58154d209e35672a3000c6c1'),
('fedcba0987654321fedcba0987654321', 'Christiansborg Palace', 'Historic palace on Slotsholmen island, home to the Danish Parliament.', 'Copenhagen', 'Denmark', '018cefac58154d209e35672a3000c6c1'),
('ffffffffffffffffffffffffffffffff', 'Assistens Cemetery', 'Historic cemetery and park, final resting place of famous Danes.', 'Copenhagen', 'Denmark', 'e0470417fa6042cba182e75bb48446a7');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_pk` char(32) NOT NULL,
  `user_first_name` varchar(20) NOT NULL,
  `user_last_name` varchar(20) NOT NULL,
  `user_email` varchar(100) NOT NULL,
  `user_password` varchar(255) NOT NULL,
  `user_created_at` bigint(20) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_pk`, `user_first_name`, `user_last_name`, `user_email`, `user_password`, `user_created_at`) VALUES
('018cefac58154d209e35672a3000c6c1', 'bob', 'bobsen', 'bob@mail.com', 'scrypt:32768:8:1$ZG4WPmqr29gQtYgf$c88e932eec2860ae60473145dd4980472af92a8dfd8fd20c77afc2df85d652f8f0cdeb67daf789046871dcef7fa6e8dded7ca6f44f45c721065b5d4cd0a80911', 1773348313),
('11d710f7682e41868350c4324605b2b4', 'john', 'johnson', 'john@mail.com', 'scrypt:32768:8:1$1J9umLbKxxeUUKE5$6fe73bcbf3ba30aa649370ebfbbc551a18c1d1a6a1b63d4ae0bc8abc923e7449869293ceefa360de7d59f73837137bcb253c0bd8104ac502fec4cc33b1d8c6c1', 1773165582),
('58b30c329be24c99aa40a56381716ad8', 'tom', 'tomson', 'tom@mail.com', 'scrypt:32768:8:1$NNzvVDxNtQoP7Hfr$ef401ed912744ae963ac1f760410942de5502f483d96af6a491be9c13ff3fc502d0fda9dc582e1f9a63002a2b8c0c1f57e91d81c8578b8b8ae7a44ee9cff7e37', 1773348327),
('e0470417fa6042cba182e75bb48446a7', 'Jack', 'Jackson', 'jack@mail.com', 'scrypt:32768:8:1$PzWMX6Yb5VLyY8Ui$d8f1f637ac43747cea2b5725d9c927c07c87fc61b65d15b051e2ed926a9137dc43e85b6bf1cc1e3db70ce1089aae35189b7529809d7b79f42841255809cd8479', 1773348287);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `destinations`
--
ALTER TABLE `destinations`
  ADD PRIMARY KEY (`destination_pk`),
  ADD KEY `fk_user` (`user_pk`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_pk`),
  ADD UNIQUE KEY `user_email` (`user_email`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `destinations`
--
ALTER TABLE `destinations`
  ADD CONSTRAINT `fk_user` FOREIGN KEY (`user_pk`) REFERENCES `users` (`user_pk`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
