CREATE DATABASE IF NOT EXISTS `MMs`;

USE `MMs`;

CREATE TABLE IF NOT EXISTS `Evaluator` (
  `idEvaluator` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(45) NOT NULL,
  `scoreResult` int(11) NOT NULL,
  `timeToSolve` time NOT NULL,
  `simulator` int(11) NOT NULL,
  PRIMARY KEY (`idEvaluator`)
);

CREATE TABLE IF NOT EXISTS `Maze` (
  `idMaze` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(45) NOT NULL,
  `xSize` bigint(20) NOT NULL,
  `ySize` int(11) NOT NULL,
  `startCellX` int(11) NOT NULL,
  `startCellY` int(11) NOT NULL,
  `endCell1X` int(11) NOT NULL,
  `endCell1Y` int(11) NOT NULL,
  `endCell2X` int(11) NOT NULL,
  `endCell2Y` int(11) NOT NULL,
  `simulator` int(11) NOT NULL,
  PRIMARY KEY (`idMaze`)
);

CREATE TABLE IF NOT EXISTS `Mouse` (
  `idMouse` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(45) NOT NULL,
  `seed` bigint(20) NOT NULL,
  `simulator` int(11) NOT NULL,
  PRIMARY KEY (`idMouse`)
);

CREATE TABLE IF NOT EXISTS `Simulation` (
  `idSimulation` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(45) NOT NULL,
  PRIMARY KEY (`idSimulation`)
);

