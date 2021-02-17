-- Create database
CREATE DATABASE MessagingApp;

-- Use database
USE MessagingApp;

-- Create table
CREATE TABLE Messages (
  id int not null auto_increment,
  message varchar(255) not null,
  primary key (id)
);
