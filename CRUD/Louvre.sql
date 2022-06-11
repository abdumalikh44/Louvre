-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema louvre
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema louvre
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `louvre` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `louvre` ;

-- -----------------------------------------------------
-- Table `louvre`.`customer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `louvre`.`customer` (
  `no_pelanggan` INT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(45) NULL DEFAULT NULL,
  `nomor_telepon` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`no_pelanggan`))
ENGINE = InnoDB
AUTO_INCREMENT = 19
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `louvre`.`booking`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `louvre`.`booking` (
  `booking_id` INT NOT NULL AUTO_INCREMENT,
  `booking_date` DATE NULL DEFAULT NULL,
  `metode_pembayaran` VARCHAR(45) NULL DEFAULT NULL,
  `jenis_kamar` VARCHAR(45) NULL DEFAULT NULL,
  `nomor_kamar` VARCHAR(45) NULL DEFAULT NULL,
  `customer_no_pelanggan` INT NOT NULL,
  PRIMARY KEY (`booking_id`, `customer_no_pelanggan`),
  INDEX `fk_Booking_customer_idx` (`customer_no_pelanggan` ASC) VISIBLE,
  CONSTRAINT `fk_Booking_customer`
    FOREIGN KEY (`customer_no_pelanggan`)
    REFERENCES `louvre`.`customer` (`no_pelanggan`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
