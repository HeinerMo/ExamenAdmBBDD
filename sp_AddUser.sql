--ADD LOGIN
USE TRANSACTION_PROCESSING_EXAMEN
GO

CREATE OR ALTER PROCEDURE sp_CreateLogin
	@param_Name VARCHAR(50) = NULL 
	,@param_Password VARCHAR(50) = NULL 
AS
	BEGIN
		--Se crea un login
			DECLARE @t nvarchar(4000)
		BEGIN TRY
			SET @t = N'CREATE LOGIN ' + QUOTENAME(@param_Name,'[]') + 'WITH PASSWORD=' + QUOTENAME(@param_Password,'''') + ', DEFAULT_DATABASE=' + QUOTENAME('TRANSACTION_PROCESSING_EXAMEN','[]')
			EXEC(@t)
			PRINT 'Login creado'
		END TRY
		BEGIN CATCH
			PRINT 'No se ha podido crear el login'
		END CATCH
	END
GO

--ADD USER TO DATABASE
USE TRANSACTION_PROCESSING_EXAMEN
GO

CREATE OR ALTER PROCEDURE sp_AddUsers
@param_Name VARCHAR(50) = NULL 
AS
	BEGIN
		DECLARE @t nvarchar(4000)
		BEGIN TRY
			SET @t = N'CREATE USER ' + QUOTENAME(@param_Name,'[]') + 'FOR LOGIN ' + QUOTENAME(@param_Name,'[]') 
			EXEC(@t)
			PRINT 'Usuario agregado a la base de datos TRANSACTION_PROCESSING_EXAMEN'
		END TRY
		BEGIN CATCH
			PRINT 'Usuario agregado a la base de datos TRANSACTION_PROCESSING_EXAMEN'
		END CATCH
	END
GO

--EXEC sp_CreateLogin 'Heiner', '12345'
--EXEC sp_AddUsers 'Heiner'