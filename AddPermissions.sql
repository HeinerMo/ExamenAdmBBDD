


USE AdventureWorks2019
GO
ALTER PROCEDURE sp_AddPermissions
@param_Name VARCHAR(50) = NULL 
,@param_Table_Name VARCHAR(50) = NULL 
,@param_Permission_Read INT = NULL
,@param_Permission_Write INT = NULL
,@param_Permission_AddUsers INT = NULL
AS
BEGIN
PRINT 'PROBANDO AddPermissions'

IF(@param_Permission_Read LIKE 1)
BEGIN
PRINT 'Permiso leer'

DECLARE @r nvarchar(4000)
			SET @r = N'GRANT SELECT ON ' + @param_Table_Name + ' TO ' + QUOTENAME(@param_Name,'[]') 
		EXEC(@r)
END
IF(@param_Permission_Write LIKE 2)
BEGIN
PRINT 'Permiso escribir'
DECLARE @w nvarchar(4000)
			SET @w = N'GRANT INSERT ON ' + @param_Table_Name  + ' TO ' + QUOTENAME(@param_Name,'[]') 
		EXEC(@w)
END
IF(@param_Permission_AddUsers LIKE 3)
BEGIN
PRINT 'Permiso usuarios'
END

	PRINT 'LISTO AddPermissions'

END