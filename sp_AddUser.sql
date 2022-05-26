
--ADD LOGIN
CREATE OR ALTER PROCEDURE sp_AddUsers
	@param_Name VARCHAR(50) = NULL 
	,@param_Password VARCHAR(50) = NULL 
AS
	BEGIN
		PRINT 'PROBANDO addLogin'
		--Se crea un login
			DECLARE @t nvarchar(4000)
				SET @t = N'CREATE LOGIN ' + QUOTENAME(@param_Name,'[]') + 'WITH PASSWORD=' + QUOTENAME(@param_Password,'''') + ', DEFAULT_DATABASE=' + QUOTENAME('TRANSACTION_PROCESSING_EXAMEN','[]')
			EXEC(@t)
		PRINT 'LISTO addLogin'
	END
GO

--ADD USER
USE TRANSACTION_PROCESSING_EXAMEN
GO

CREATE OR ALTER PROCEDURE sp_AddUsers
@param_Name VARCHAR(50) = NULL 
AS
	BEGIN
		PRINT 'PROBANDO addUser'
		DECLARE @t nvarchar(4000)
		SET @t = N'CREATE USER ' + QUOTENAME(@param_Name,'[]') + 'FOR LOGIN ' + QUOTENAME(@param_Name,'[]') 
		EXEC(@t)
		PRINT 'LISTO addUser'
	END
GO

