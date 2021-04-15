CREATE TABLE PARCIAL 
(
ID INT NOT NULL AUTO_INCREMENT, 
DATE DATETIME NOT NULL, 
SIZE NVARCHAR(50) NOT NULL,
TIEMPO_AGUA INT,
TIEMPO_SHAMPOO INT,
TIEMPO_RODILLOS INT,
TIEMPO_ESCOBAS INT,
TIEMPO_AGUA2 INT,
TIEMPO_SECADO INT,
PRIMARY KEY (ID)
);

INSERT INTO PARCIAL (DATE, SIZE, TIEMPO_AGUA, TIEMPO_SHAMPOO, TIEMPO_RODILLOS, TIEMPO_ESCOBAS, TIEMPO_AGUA2, TIEMPO_SECADO) VALUES ("2021-04-14 19:20:30", "GRANDE", 1, 1, 1, 1, 1, 1)

TRUNCATE TABLE PARCIAL

SELECT * FROM PARCIAL