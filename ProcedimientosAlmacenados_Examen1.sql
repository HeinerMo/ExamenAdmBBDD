
--ADD LOGIN
USE master
GO
CREATE PROCEDURE sp_AddLoggin
@param_Name VARCHAR(50) = NULL 
,@param_Password VARCHAR(50) = NULL 
AS
BEGIN
	PRINT 'PROBANDO addLogin'

	--Se crea un login
		DECLARE @t nvarchar(4000)
			SET @t = N'CREATE LOGIN ' + QUOTENAME(@param_Name,'[]') + 'WITH PASSWORD=' + QUOTENAME(@param_Password,'''') + ', DEFAULT_DATABASE=' + QUOTENAME('AdventureWorks2019','[]')
		EXEC(@t)
	PRINT 'LISTO addLogin'

END

--ADD USER
USE AdventureWorks2019
GO
CREATE PROCEDURE sp_AddUsers
@param_Name VARCHAR(50) = NULL 
AS
BEGIN
PRINT 'PROBANDO addUser'
DECLARE @t nvarchar(4000)
			SET @t = N'CREATE USER ' + QUOTENAME(@param_Name,'[]') + 'FOR LOGIN ' + QUOTENAME(@param_Name,'[]') 
		EXEC(@t)
	PRINT 'LISTO addUser'

END


