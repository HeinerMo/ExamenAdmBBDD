--Encriptacion de tarjetas

--Se crea la master key
USE TRANSACTION_PROCESSING_EXAMEN;
GO
CREATE MASTER KEY ENCRYPTION BY PASSWORD = 'Examen1';

--Se crea un certificado
USE TRANSACTION_PROCESSING_EXAMEN;
GO
CREATE CERTIFICATE Certificado_Examen WITH SUBJECT = 'Encripta una tarjetas';
GO

--Se crea la llave simetrica
CREATE SYMMETRIC KEY LlaveSimetrica_Examen 
WITH ALGORITHM = AES_256 ENCRYPTION BY CERTIFICATE Certificado_examen;

--Se le agrega una columna extra
ALTER TABLE [CUSTOMERS].[tb_CREDIT_CARD] ADD [CREDIT_CARD_NUMBER_ENCRYPTED] varbinary(MAX)

OPEN SYMMETRIC KEY LlaveSimetrica_Examen 
DECRYPTION BY CERTIFICATE Certificado_Examen;

--Almacenamos la data encriptada en la nueva columna 
UPDATE [CUSTOMERS].[tb_CREDIT_CARD]
SET [CREDIT_CARD_NUMBER_ENCRYPTED] = ENCRYPTBYKEY(Key_GUID('LlaveSimetrica_Examen'), CREDIT_CARD_NUMBER) FROM  [CUSTOMERS].[tb_CREDIT_CARD];


--Cerramos la llave simétrica después de haberla usado
CLOSE SYMMETRIC KEY LlaveSimetrica_Examen;
GO
